# 👺 Demon Slayer RESTful API

![Demon Slayer Logo](static/Img/Demon-Slayer-Logo.png)

Una API RESTful ligera y sencilla construida con **Flask** (Python) para acceder a datos de personajes, estilos de respiración y roles del universo de *Kimetsu No Yaiba*.

Este proyecto sirve como una excelente plantilla para aprender a crear APIs básicas utilizando archivos **JSON** para la persistencia de datos.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión Requerida | Propósito |
| :--- | :--- | :--- | :--- |
| **Backend** | Python (Flask) | 3.x | Servidor RESTful y lógica de datos. |
| **Base de Datos** | JSON | N/A | Almacenamiento simple de los datos de personajes. |
| **Frontend** | HTML, CSS | N/A | Página de bienvenida y documentación. |
| **Estilos** | CSS Custom Props | N/A | Manejo centralizado de colores y tipografía. |

---

| Componente | Tecnología | Propósito |
| :--- | :---| :--- |
| **Backend** | [![My Skills](https://skillicons.dev/icons?i=py,flask)](https://github.com/DaniDevGS/Demon-Slayer-API)| Servidor RESTful y lógica de datos. |
| **Base de Datos** | <img src="https://cdn-icons-png.flaticon.com/128/136/136525.png" width="40"> | Almacenamiento simple de los datos de personajes. |
| **Frontend** | [![My Skills](https://skillicons.dev/icons?i=html,css)](https://github.com/DaniDevGS/Demon-Slayer-API) | Página de bienvenida y documentación. |
---



## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar la API en tu entorno local.

### Prerequisitos

* **Python 3+**
* **`pip`** (Python package installer)

### 1. Clonar el Repositorio

```bash
git clone https://github.com/DaniDevGS/Demon-Slayer-API
cd Demon-Slayer-API
```

### 2. Crear Entorno Virtual e Instalar Dependencias

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto.

```bash

# Crear entorno virtual (ej. venv)
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar Flask
pip install Flask
```
### 3. Ejecutar la Aplicación

Ejecuta el servidor Flask:

```bash

python app.py
```

## 📚 Endpoints de la API

La API expone los siguientes puntos de conexión REST (actualmente solo soporta GET):

---
| Metodo | Endpoint | Descripción |
| :--- | :---| :--- |
| **GET** | **/api/characters** | Obtiene la lista completa de todos los personajes.	 |
| **GET** | **/api/characters/id** | Obtiene un personaje específico por su id. |
---

### Ejemplo: Obtener un Personaje
Para obtener la información de Tanjiro Kamado (ID 1), haz una solicitud a:

```bash

GET [http://127.0.0.1:5000/api/characters/1](http://127.0.0.1:5000/api/characters/1)
```

### Respuesta (JSON):
```json
{
        "id": 1,
        "name": "Tanjiro Kamado",
        "breathing_style": "Water Breathing",
        "role": "Demon Slayer",
        "image": "https://static.wikia.nocookie.net/kimetsu-no-yaiba/images/5/56/Final_Selection_Tanjiro_design.png/revision/latest?cb=20251002050645",
        "season": "Arch of Unbreakable Resolve"
}
```

👥 Colaboradores

---
| NameDev | Image | Descripción |
| :--- | :---| :--- |
| **DaniDev:** | <img src="https://avatars.githubusercontent.com/u/186916190?v=4" width="40"> | Desarrollador Backend y Mantenedor principal. |
| **charlesworer-png:** | <img src="https://avatars.githubusercontent.com/u/236681250?v=4" width="40"> | Investigador sobre los datos para el JSON. |
---