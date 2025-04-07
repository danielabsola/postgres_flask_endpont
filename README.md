# 🐍 PostgreSQL + Flask API Endpoint

Este proyecto es una API RESTful simple creada con Flask que se conecta a una base de datos PostgreSQL para exponer información mediante endpoints.

> 🔧 Ideal para pruebas, entrenamiento y ejemplos de conexión entre backends livianos y bases de datos SQL.

---

## 🚀 ¿Qué hace esta API?

- Se conecta a una base de datos PostgreSQL.
- Expone un endpoint para obtener datos de una tabla específica.
- Utiliza SQLAlchemy para la conexión a la base.
- Devuelve los resultados en formato JSON.

---

## 📁 Estructura del proyecto

```
├── app.py                  # App principal de Flask
├── config.py               # Configuración de conexión a la DB
├── requirements.txt        # Dependencias del entorno
├── .gitignore              # Archivos a ignorar
```

---

## 🛠️ Cómo correrlo localmente

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/danielabsola/postgres_flask_endpont.git
   cd postgres_flask_endpont
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar tu base de datos en `config.py`**

   Editá `config.py` con tus credenciales de PostgreSQL:

   ```python
   DATABASE_CONFIG = {
       'host': 'localhost',
       'port': 5432,
       'dbname': 'nombre_de_tu_db',
       'user': 'tu_usuario',
       'password': 'tu_contraseña'
   }
   ```

5. **Correr el servidor:**

   ```bash
   python app.py
   ```

   La API estará disponible en `http://127.0.0.1:5000/`.

---

## 📌 Ejemplo de uso

Una vez corriendo, podés consultar los datos desde el navegador o con curl:

```
GET http://127.0.0.1:5000/datos
```

La API devolverá los registros en formato JSON.

---

## 💡 Motivación

Este proyecto fue desarrollado para experimentar con la creación rápida de APIs que interactúan con bases de datos, ideal para integraciones o tests en proyectos más grandes.

---

## 📬 Contacto

[Gmail] (dbshoy@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/daniela-beatriz-sola-587b902b)  
[GitHub](https://github.com/danielabsola)
[Malt](https://www.malt.es/profile/danielabeatrizsola)

---

> Si este proyecto te resulta útil o interesante, ¡no olvides dejar una ⭐️!
v
🌐 Disponible para proyectos freelance y colaboraciones tech.
