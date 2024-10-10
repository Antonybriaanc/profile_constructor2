{
    'name': 'Profile Constructor',
    'version': '1.0',
    'summary': 'Automatización avanzada de perfiles de usuario en Odoo',
    'description': """
        <h2>Descripción General:</h2>
        <p>El módulo <strong>Profile Constructor</strong> para Odoo 17 simplifica y automatiza la creación y gestión de perfiles de usuario, permitiendo a los administradores configurar roles y permisos de manera rápida y eficiente.</p>

        <h2>Características Principales:</h2>
        <ul>
            <li><strong>Perfiles Predefinidos:</strong> Crea perfiles con accesos y permisos específicos de manera estructurada.</li>
            <li><strong>Asignación Automática:</strong> Asigna automáticamente grupos de permisos y accesos basados en los perfiles definidos.</li>
            <li><strong>Preservación de Tipos de Usuario:</strong> Asegura que los usuarios internos conserven su rol al aplicar perfiles.</li>
            <li><strong>Edición y Flexibilidad:</strong> Modifica fácilmente perfiles existentes y actualiza configuraciones sin afectar a los usuarios asignados.</li>
        </ul>

        <h2>Beneficios:</h2>
        <ul>
            <li><strong>Eficiencia en la Administración de Usuarios:</strong> Ahorra tiempo al evitar la configuración manual de permisos para cada usuario.</li>
            <li><strong>Seguridad Mejorada:</strong> Garantiza una correcta asignación de permisos en función de los roles empresariales, evitando errores manuales.</li>
            <li><strong>Escalabilidad:</strong> Gestiona usuarios de manera eficiente incluso en grandes equipos, manteniendo una estructura clara y organizada de permisos.</li>
        </ul>

        <h2>Instalación:</h2>
        <p>Sigue estos pasos para instalar el módulo:</p>
        <ol>
            <li>Clona este módulo en tu directorio de addons de Odoo: <code>addons</code>.</li>
            <li>Reinicia el servidor de Odoo.</li>
            <li>Actualiza la lista de aplicaciones desde el backend de Odoo y busca <strong>Profile Constructor</strong> para instalarlo.</li>
        </ol>

        <h2>Guía de Uso:</h2>
        <ol>
            <li>Accede al menú <strong>Ajustes > Perfiles de Usuario</strong> para crear nuevos perfiles.</li>
            <li>Asigna perfiles a usuarios desde <strong>Ajustes > Usuarios y Compañías > Usuarios</strong>.</li>
            <li>Modifica perfiles según sea necesario para ajustar permisos y actualiza automáticamente los perfiles asignados a los usuarios.</li>
        </ol>

        <h2>Soporte y Contacto:</h2>
        <p>Desarrollado por <strong>Antony Castillo</strong>. Para soporte técnico, contacta a través de: <a href="mailto:abcy775@gmail.com">abcy775@gmail.com</a>.</p>
    """,
    'author': 'Antony Castillo',
    'maintainer': 'Antony Castillo',
    'website': 'https://github.com/Antonybriaanc',  # Añade la URL si tienes un repositorio público
    'category': 'Administration/User Profiles',  # Categoría para que los usuarios lo encuentren más fácilmente
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_profile_views.xml',
        'views/user_profile_kanban.xml',
    ],
    'images': ['static/description/screenshot.png'],  # Agrega la ruta de la imagen de captura de pantalla si la tienes
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 49.99,  # Precio del módulo
    'currency': 'USD',  # Moneda en la que se vende (EUR o USD)
    'license': 'LGPL-3',  # Licencia del módulo
}
