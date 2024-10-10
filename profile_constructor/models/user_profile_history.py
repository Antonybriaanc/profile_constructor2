from odoo import models, fields

class UserProfileHistory(models.Model):
    _name = 'user.profile.history'
    _description = 'Historical data of profile changes'

    user_id = fields.Many2one('res.users', string="User", required=True)
    profile_id = fields.Many2one('user.profile', string="Profile", required=True)
    previous_groups = fields.Many2many('res.groups', string="Previous Groups")
    previous_modules = fields.Many2many('ir.module.module', string="Previous Modules")
    change_date = fields.Datetime(string="Change Date", default=fields.Datetime.now)
