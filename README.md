# Gestión de Perfiles de Usuario - Módulo Odoo

Este módulo de Odoo permite gestionar perfiles de usuario, asignar grupos de usuarios, controlar el acceso a módulos y ocultar menús basados en perfiles definidos.

## Características

- Crear perfiles de usuario con acceso personalizado a grupos, módulos y menús.
- Aplicar automáticamente los perfiles a los usuarios cuando se crean o actualizan.
- Registrar los cambios en los perfiles (grupos y menús) en el chatter (sistema de mensajería de Odoo).
- Solo se registran los cambios relevantes (grupos o menús agregados o eliminados) sin recalcular todo el perfil.
- Seguimiento granular de cambios en grupos y menús.

## Modelos

### 1. `user.profile`

Este es el modelo principal para gestionar los perfiles de usuario. Permite a los administradores definir:

- Nombre del perfil
- Acceso a Módulos (campo Many2many relacionado con `ir.module.module`)
- Grupos de Usuarios (campo Many2many relacionado con `res.groups`)
- Menús a Ocultar (campo Many2many relacionado con `ir.ui.menu`)

Los perfiles se pueden aplicar a varios usuarios, y cuando se modifica un perfil, los usuarios asociados tendrán su acceso actualizado automáticamente.

### 2. `res.users`

Este modelo ha sido extendido para incluir:

- Un campo `profile_id` (relación Many2one con `user.profile`).

Los grupos y el acceso a menús del usuario se actualizarán según el perfil asociado. Si el perfil es actualizado, el acceso de los usuarios asociados también se actualizará automáticamente.

## Métodos

### `apply_profile()`

Este método se llama cuando se aplica un perfil a un usuario. Elimina todos los grupos actuales del usuario y asigna solo los grupos definidos en el perfil. Además, gestiona qué menús se ocultan o muestran según el perfil.

### `apply_to_users()`

Este método se encarga de aplicar los cambios del perfil a todos los usuarios asociados con el perfil dado.

### `_store_user_profile_history(user, vals)`

Este método registra los cambios precisos en el perfil del usuario, registrando solo las diferencias (grupos y menús agregados o eliminados) en el chatter para mayor claridad.

## Instalación

1. Copia el módulo en el directorio `addons` de tu instalación de Odoo.
2. Instala el módulo desde el menú de aplicaciones de Odoo.
3. Después de la instalación, verás un nuevo menú bajo **Ajustes > Perfiles de Usuario**.

## Uso

1. **Crear un Perfil de Usuario:**
   - Navega a **Ajustes > Perfiles de Usuario**.
   - Haz clic en el botón "Crear".
   - Introduce el nombre del perfil, selecciona los grupos de usuarios, el acceso a módulos y define qué menús deben ser ocultados.
   - Guarda el perfil.
  
2. **Asignar Perfiles a los Usuarios:**
   - Ve a **Ajustes > Usuarios y Compañías > Usuarios**.
   - Abre el formulario de un usuario y asigna un perfil en el campo **Perfil**.
   - Los grupos y el acceso a menús del usuario se actualizarán según el perfil.

3. **Actualización de Perfiles:**
   - Cualquier cambio realizado en un perfil se propagará automáticamente a todos los usuarios asignados a dicho perfil.
   - El sistema registrará solo los cambios (grupos y menús agregados/eliminados) en el chatter.

## Mejoras Futuras

- Agregar una interfaz más amigable para la actualización masiva de usuarios.
- Implementar filtros avanzados para gestionar un gran número de usuarios y perfiles.

## Licencia

Este módulo está licenciado bajo la licencia propietaria de Odoo. Consulta el archivo LICENSE para más detalles.
