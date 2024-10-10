{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización avanzada de perfiles de usuario en Odoo',
    'description': (
        "<h2>Descripción General</h2>"
        "<p>El módulo <strong>Profile Constructor</strong> para Odoo 17 simplifica y automatiza la creación y gestión de perfiles de usuario, permitiendo a los administradores configurar roles y permisos de manera rápida y eficiente.</p>"
        "<h2>Características Principales</h2>"
        "<ul>"
        "<li>Crea perfiles con accesos y permisos específicos de manera estructurada.</li>"
        "<li>Asigna automáticamente grupos de permisos y accesos basados en los perfiles definidos.</li>"
        "<li>Asegura que los usuarios internos conserven su rol al aplicar perfiles.</li>"
        "<li>Modifica fácilmente perfiles existentes y actualiza configuraciones sin afectar a los usuarios asignados.</li>"
        "</ul>"
        "<h2>Beneficios</h2>"
        "<ul>"
        "<li>Ahorra tiempo al evitar la configuración manual de permisos para cada usuario.</li>"
        "<li>Garantiza una correcta asignación de permisos en función de los roles empresariales, evitando errores manuales.</li>"
        "<li>Gestiona usuarios de manera eficiente incluso en grandes equipos.</li>"
        "</ul>"
        "<h2>Instalación</h2>"
        "<p>Sigue estos pasos para instalar el módulo:</p>"
        "<ol>"
        "<li>Clona este módulo en tu directorio de addons de Odoo.</li>"
        "<li>Reinicia el servidor de Odoo.</li>"
        "<li>Actualiza la lista de aplicaciones desde el backend y busca <strong>Profile Constructor</strong> para instalarlo.</li>"
        "</ol>"
        "<h2>Guía de Uso</h2>"
        "<ol>"
        "<li>Accede al menú Ajustes > Perfiles de Usuario para crear nuevos perfiles.</li>"
        "<li>Asigna perfiles a usuarios desde Ajustes > Usuarios y Compañías > Usuarios.</li>"
        "<li>Modifica perfiles para ajustar permisos y actualiza automáticamente los perfiles asignados.</li>"
        "</ol>"
        "<h2>Soporte y Contacto</h2>"
        "<p>Desarrollado por Antony Castillo. Para soporte técnico, contacta a: <a href='mailto:abcy775@gmail.com'>abcy775@gmail.com</a>.</p>"
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
