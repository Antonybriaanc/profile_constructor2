{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización de la parametrización de perfiles de usuario en Odoo',
    'description': """
        El módulo **Profile Constructor** para Odoo 17 permite automatizar la gestión de perfiles de usuario.
        
        ## Características:
        - Crear perfiles predefinidos con acceso a módulos y permisos específicos.
        - Asignar automáticamente a los usuarios los grupos de permisos basados en perfiles definidos.
        - Asegurar que el tipo de usuario "Interno" se preserve al asignar un perfil.
        - Flexibilidad para editar perfiles existentes y asignarlos a usuarios sin pérdida de configuración.

        ## Instalación:
        - Clona este módulo en tu directorio `addons` y reinicia el servidor de Odoo.
        - Actualiza la lista de aplicaciones en Odoo e instala el módulo desde el backend.

        ## Uso:
        - Crea perfiles desde el menú **Ajustes** > **Perfiles de Usuario**.
        - Asigna perfiles a usuarios desde la vista de **Usuarios** en **Ajustes** > **Usuarios y Compañías**.
        - Modifica perfiles existentes y actualiza los permisos para los usuarios asignados.

        ## Autor:
        Desarrollado por Antony Castillo.
    """,
    'author': 'Antony Castillo',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/user_profile_kanban.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
