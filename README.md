Comandos:

- flask run
    - Inicia la app

- flask db init
    - Genera una carpeta migrations, al ser codigo generado no es recomendado modificar ese codigo manualmente.
      Solo ejecutar este comando una vez.

- flask db migrate -m "descripcion_de_la_migracion"
    - Crea una nueva migracion con una descripcion dada.
      A pesar de codigo autogenerado y no es recomendable modiicarlo, en la documentacion se comenta que hay veces que
      Flask-Migrate no reconoce todos los tipos de cambios automaticamente siempre, asi que luego de crear una migracion
      hay que revisarla en detalle para validar que todos los cambios de la migracion estan sienndo aplicados, en caso
      de que no, agregarlos manualmente.

- flask db upgrade
    - Aplica la siguiente migracion aun no aplicada

- flask db downgrade
    - Revierte la ultima migracion aplicada

- flask data:download
    - Descarga los archivos de The Movies Dataset desde una carpeta publica en Google Drive en la carpeta data
      Este comando limpiara la carpeta antes de volver a descargar los archivos, si se hizo algun cambio al dataset
      descargado previamente, se perdera

- flask seed
    - Formatea los datos de los archivos csv de The Movies Dataset y los ingresa a la base de datos.
      Este comando eliminato todos los datos existentes de la base de datos antes de ingresar los de los CSV.
      Ejecutar este comando solo si se tiene los csv de The Movies Dataset
