{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización avanzada de perfiles de usuario en Odoo',
    'description': (
        'Descripción General: '
        'El módulo Profile Constructor para Odoo 17 simplifica y automatiza la creación y gestión de perfiles de usuario, permitiendo a los administradores configurar roles y permisos de manera rápida y eficiente.\n\n'
        'Características Principales:\n'
        '- Crea perfiles con accesos y permisos específicos de manera estructurada.\n'
        '- Asigna automáticamente grupos de permisos y accesos basados en los perfiles definidos.\n'
        '- Asegura que los usuarios internos conserven su rol al aplicar perfiles.\n'
        '- Modifica fácilmente perfiles existentes y actualiza configuraciones sin afectar a los usuarios asignados.\n\n'
        'Beneficios:\n'
        '- Ahorra tiempo al evitar la configuración manual de permisos para cada usuario.\n'
        '- Garantiza una correcta asignación de permisos en función de los roles empresariales, evitando errores manuales.\n'
        '- Gestiona usuarios de manera eficiente incluso en grandes equipos.\n\n'
        'Instalación:\n'
        '1. Clona este módulo en tu directorio de addons de Odoo.\n'
        '2. Reinicia el servidor de Odoo.\n'
        '3. Actualiza la lista de aplicaciones desde el backend y busca Profile Constructor para instalarlo.\n\n'
        'Guía de Uso:\n'
        '1. Accede al menú Ajustes > Perfiles de Usuario para crear nuevos perfiles.\n'
        '2. Asigna perfiles a usuarios desde Ajustes > Usuarios y Compañías > Usuarios.\n'
        '3. Modifica perfiles para ajustar permisos y actualiza automáticamente los perfiles asignados.\n\n'
        'Soporte y Contacto: '
        'Desarrollado por Antony Castillo. Para soporte técnico, contacta a: abcy775@gmail.com.'
    ),
    'author': 'Antony Castillo',
    'maintainer': 'Antony Castillo',
    'website': 'https://github.com/Antonybriaanc',
    'category': 'Administration/User Profiles',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/user_profile_kanban.xml',
    ],
    'images': ['static/description/screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 49.99,
    'currency': 'USD',
    'license': 'LGPL-3',
}
