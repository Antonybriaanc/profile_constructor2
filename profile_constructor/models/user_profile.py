from odoo import models, fields, api

class UserProfile(models.Model):
    _name = 'user.profile'
    _description = 'User Profile Management'
    _inherit = ['mail.thread']  # Heredamos para tener el chatter

    name = fields.Char(string='Profile Name', required=True, track_visibility='onchange')
    module_access_ids = fields.Many2many('ir.module.module', string='Module Access', track_visibility='onchange')
    user_group_ids = fields.Many2many('res.groups', string='User Groups', track_visibility='onchange')
    menu_ids = fields.Many2many('ir.ui.menu', string='Menus to Hide', track_visibility='onchange')

    @api.model
    def create(self, vals):
        profile = super(UserProfile, self).create(vals)
        profile.apply_to_users_in_batches()
        return profile

    def write(self, vals):
        for profile in self:
            users = self.env['res.users'].search([('profile_id', '=', profile.id)])
            for user in users:
                # Guardamos solo los cambios relevantes
                self._store_user_profile_history(user, vals)

        res = super(UserProfile, self).write(vals)
        self.apply_to_users_in_batches()
        return res

    def apply_to_users_in_batches(self, batch_size=1):
        """Aplica los cambios del perfil a los usuarios asociados en bloques"""
        users = self.env['res.users'].search([('profile_id', 'in', self.ids)])
        for i in range(0, len(users), batch_size):
            user_batch = users[i:i + batch_size]
            user_batch.apply_profile_batch()
            self.env.cr.commit()  # Realiza un commit después de cada bloque

    def _store_user_profile_history(self, user, vals):
        """Registra los cambios precisos del perfil del usuario en el historial."""

        # Cambios en los grupos
        previous_groups = set(user.groups_id.ids)
        new_groups = previous_groups
        if 'user_group_ids' in vals and isinstance(vals['user_group_ids'], list) and len(vals['user_group_ids']) > 0 and len(vals['user_group_ids'][0]) > 2:
            new_groups = set(vals['user_group_ids'][0][2])

        added_groups = new_groups - previous_groups
        removed_groups = previous_groups - new_groups

        # Cambios en los menús
        previous_menus = set(user.profile_id.menu_ids.ids)
        new_menus = previous_menus
        if 'menu_ids' in vals and isinstance(vals['menu_ids'], list) and len(vals['menu_ids']) > 0 and len(vals['menu_ids'][0]) > 2:
            new_menus = set(vals['menu_ids'][0][2])

        added_menus = new_menus - previous_menus
        removed_menus = previous_menus - new_menus

        # Mensajes en el chatter
        if added_groups:
            group_names = ', '.join(self.env['res.groups'].browse(added_groups).mapped('name'))
            user.message_post(body=f"Se agregaron los siguientes grupos: {group_names}")

        if removed_groups:
            group_names = ', '.join(self.env['res.groups'].browse(removed_groups).mapped('name'))
            user.message_post(body=f"Se eliminaron los siguientes grupos: {group_names}")

        if added_menus:
            menu_names = ', '.join(self.env['ir.ui.menu'].browse(added_menus).mapped('name'))
            user.message_post(body=f"Se agregaron los siguientes menús: {menu_names}")

        if removed_menus:
            menu_names = ', '.join(self.env['ir.ui.menu'].browse(removed_menus).mapped('name'))
            user.message_post(body=f"Se eliminaron los siguientes menús: {menu_names}")

class ResUsers(models.Model):
    _inherit = 'res.users'

    profile_id = fields.Many2one('user.profile', string='Profile')

    def apply_profile_batch(self):
        """Aplica el perfil seleccionado a los usuarios de este lote."""
        for user in self:
            if user.profile_id:
                # Obtener los grupos "Usuario Interno" y "Usuario Portal"
                internal_user_group = self.env.ref('base.group_user').id
                portal_user_group = self.env.ref('base.group_portal').id

                # Grupos del perfil seleccionado
                profile_groups = user.profile_id.user_group_ids

                # Verificar si el perfil asigna el grupo de "Usuario Portal"
                if portal_user_group in profile_groups.ids:
                    # Eliminar el grupo "Usuario Interno" si se asigna "Usuario Portal"
                    profile_groups = profile_groups.filtered(lambda g: g.id != internal_user_group)

                # Si no es un usuario de tipo portal, asegurarse de que tenga el grupo "Usuario Interno"
                elif internal_user_group not in profile_groups.ids:
                    profile_groups |= self.env['res.groups'].browse(internal_user_group)

                # Solo si los grupos cambian, los actualizamos
                if set(user.groups_id.ids) != set(profile_groups.ids):
                    user.write({'groups_id': [(6, 0, profile_groups.ids)]})

                # Aplicar los menús ocultos solo si cambian
                user._apply_menu_visibility()

    def _apply_menu_visibility(self):
        """Oculta o muestra menús según el perfil del usuario."""
        if self.profile_id:
            menus_to_hide = self.profile_id.menu_ids
            user_menu_access = self.env['ir.ui.menu'].search([])

            for menu in user_menu_access:
                if menu in menus_to_hide:
                    menu.write({'groups_id': [(3, g.id) for g in self.groups_id]})
                else:
                    menu.write({'groups_id': [(4, g.id) for g in self.groups_id]})

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        if 'profile_id' in vals and user.profile_id:
            user.apply_profile_batch()
        return user

    def write(self, vals):
        # Solo aplicar cambios al perfil si realmente se modificó el campo `profile_id`
        res = super(ResUsers, self).write(vals)
        if 'profile_id' in vals:
            self.apply_profile_batch()
        return res
