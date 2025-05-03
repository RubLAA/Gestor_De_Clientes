# Gestor de Clientes en Python

Un gestor de clientes con interfaz gráfica (GUI) desarrollado en Python, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) y guarda los datos en un archivo CSV. Ideal para gestionar información básica de clientes de forma local y organizada.

## Características

- **Interfaz gráfica intuitiva** construida con Tkinter.
- **Operaciones CRUD**:
  - Crear clientes con validación de datos.
  - Editar clientes existentes.
  - Eliminar clientes con confirmación.
  - Listar todos los clientes.
- **Validación automática**:
  - Formato de DNI: `2 números + 1 letra mayúscula` (ej: `31D`).
  - Nombre y apellido: solo letras (2-30 caracteres).
- **Persistencia en CSV**: Los datos se guardan en `clientes.csv`.
- **Mensajes de feedback**: Confirmación de acciones exitosas/errores.

## Requisitos

- Python 3.7 o superior.
- Módulos estándar de Python:
  - `tkinter`
  - `csv`
  - `re`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/rubences/Gestor_Clientes.git
   cd Gestor_Clientes
