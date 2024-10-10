{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización de la parametrización de perfiles de usuario en Odoo',
    'description': """
        <h2>Características:</h2>
        <ul>
            <li>Crear perfiles predefinidos con acceso a módulos y permisos específicos.</li>
            <li>Asignar automáticamente a los usuarios los grupos de permisos basados en perfiles definidos.</li>
            <li>Asegurar que el tipo de usuario "Interno" se preserve al asignar un perfil.</li>
            <li>Flexibilidad para editar perfiles existentes y asignarlos a usuarios sin pérdida de configuración.</li>
        </ul>
        <h2>Instalación:</h2>
        <p>
            - Clona este módulo en tu directorio <code>addons</code> y reinicia el servidor de Odoo.<br/>
            - Actualiza la lista de aplicaciones en Odoo e instala el módulo desde el backend.
        </p>
        <h2>Uso:</h2>
        <ul>
            <li>Crea perfiles desde el menú <strong>Ajustes > Perfiles de Usuario</strong>.</li>
            <li>Asigna perfiles a usuarios desde la vista de <strong>Usuarios</strong> en <strong>Ajustes > Usuarios y Compañías</strong>.</li>
            <li>Modifica perfiles existentes y actualiza los permisos para los usuarios asignados.</li>
        </ul>
        <h2>Autor:</h2>
        <p>Desarrollado por Antony Castillo.</p>
    """,
    'author': 'Antony Castillo',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/user_profile_kanban.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 49.99,  # Precio del módulo
    'currency': 'USD',  # Moneda en la que se vende (EUR o USD)
    'license': 'LGPL-3',  # Licencia del módulo
}
