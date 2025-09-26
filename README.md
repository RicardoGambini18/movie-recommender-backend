Iniciar app:

- flask run (CLI)
- python3 app.py (Python)

Migraciones:

- flask db init (Inicializar migraciones)
    - Genera una carpeta migrations, al ser codigo generado no es recomendado modificar ese codigo manualmente.

- flask db migrate -m "descripcion_de_la_migracion"
    - A pesar de codigo autogenerado y no es recomendable modiicarlo, en la documentacion se comenta que hay veces que
      Flask-Migrate no reconoce todos los tipos de cambios automaticamente siempre, asi que luego de crear una migracion
      hay que revisarla en detalle para validar que todos los cambios de la migracion estan sienndo aplicados, en caso
      de que no, agregarlos manualmente.

- flask db upgrade
    - Aplica la siguiente migracion aun no aplicada

- flask db downgrade
    - Revierte la ultima migracion aplicada