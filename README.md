# Bitácora de Cerámica 🏺

Aplicación web tipo blog desarrollada con Python y Django como proyecto final del curso. Permite a usuarias/os compartir sus piezas de cerámica, gestionar un perfil personal y enviar mensajes entre usuarios.

## 🌐 Funcionalidades principales

- Registro, login y logout de usuarios.
- Vista de perfil con edición y avatar.
- Creación, edición y eliminación de piezas (solo para el autor).
- Visualización de piezas y detalles (incluye imagen y descripción con texto enriquecido).
- Página "Acerca de mí".
- Búsqueda por título de piezas.
- Sistema de mensajería entre usuarios con bandeja de entrada.
- Feedback visual para acciones (mensajes de éxito o error).
- Protección de vistas mediante login y mixins.

## 🧱 Modelo principal: Pieza de cerámica

- `titulo` (CharField)
- `tecnica` (CharField)
- `descripcion` (RichText usando CKEditor)
- `imagen` (ImageField)
- `fecha` (DateTimeField auto generado)
- `autor` (ForeignKey al usuario)

## 👤 Gestión de usuarios

- App `accounts` para login, logout, signup, perfil, edición y cambio de contraseña.
- Vista protegida con login y decoradores.
- Uso de formularios personalizados.
- Se guarda avatar, biografía y otros datos opcionales.

## 📩 Sistema de mensajes

- App `mensajes` con inbox y formulario para enviar mensajes entre usuarios.
- Cada mensaje guarda remitente, destinatario, contenido y timestamp.
- Posibilidad de eliminar mensajes recibidos.

## 🧩 Tecnologías utilizadas

- Python 3.13
- Django 5.2
- SQLite (modo local)
- Bootstrap y CSS custom
- CKEditor (para descripción enriquecida)
- Git y GitHub

## 🧪 Cómo correr el proyecto localmente

```bash
git clone https://github.com/ElianaGalzerano/Bitacora_de_Ceramica.git
cd Bitacora_de_Ceramica
python -m venv env
source env/bin/activate  # en Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver






