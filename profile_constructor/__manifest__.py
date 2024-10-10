{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización avanzada de perfiles de usuario en Odoo',
    'description': (
        '<p>El módulo Profile Constructor para Odoo 17 simplifica y automatiza la creación y gestión de perfiles de usuario, permitiendo a los administradores configurar roles y permisos de manera rápida y eficiente.</p>'
        '<p>Características Principales:</p>'
        '<ul>'
        '<li>Crea perfiles con accesos y permisos específicos de manera estructurada.</li>'
        '<li>Asigna automáticamente grupos de permisos y accesos basados en los perfiles definidos.</li>'
        '<li>Asegura que los usuarios internos conserven su rol al aplicar perfiles.</li>'
        '<li>Modifica fácilmente perfiles existentes y actualiza configuraciones sin afectar a los usuarios asignados.</li>'
        '</ul>'
        '<p>Beneficios:</p>'
        '<ul>'
        '<li>Ahorra tiempo al evitar la configuración manual de permisos para cada usuario.</li>'
        '<li>Garantiza una correcta asignación de permisos en función de los roles empresariales, evitando errores manuales.</li>'
        '<li>Gestiona usuarios de manera eficiente incluso en grandes equipos.</li>'
        '</ul>'
        '<p>Instalación:</p>'
        '<ol>'
        '<li>Clona este módulo en tu directorio de addons de Odoo.</li>'
        '<li>Reinicia el servidor de Odoo.</li>'
        '<li>Actualiza la lista de aplicaciones desde el backend y busca Profile Constructor para instalarlo.</li>'
        '</ol>'
        '<p>Guía de Uso:</p>'
        '<ol>'
        '<li>Accede al menú Ajustes > Perfiles de Usuario para crear nuevos perfiles.</li>'
        '<li>Asigna perfiles a usuarios desde Ajustes > Usuarios y Compañías > Usuarios.</li>'
        '<li>Modifica perfiles para ajustar permisos y actualiza automáticamente los perfiles asignados.</li>'
        '</ol>'
        '<p>Soporte y Contacto:</p>'
        '<p>Desarrollado por Antony Castillo. Para soporte técnico, contacta a: <a href="mailto:abcy775@gmail.com">abcy775@gmail.com</a>.</p>'
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
