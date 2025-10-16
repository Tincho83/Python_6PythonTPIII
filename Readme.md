# TP III de Python para CoderHouse

## Descripción
Proyecto eCommerce en Python usando Django. 

# Proyecto Django - eCommerce

## Obtencion del proyecto e instalacion de componentes:
1. Descargar o clonar el proyecto 
   - "https://github.com/Tincho83/Python_6PythonTPIII.git".

2. Abrir VS Code, luego abrir la carpeta del proyecto, ejemplo "Python_6PythonTPIII"

3. En VS Code:
   - Ir a Ver/Terminal, para visualizar la consola.
   - En la pestaña "Terminal" debemos estar ubicados en la carpeta del proyecto "c:\proy\Python_6PythonTPIII".

4. Crear entorno virtual: 
   -  python -m venv ent_virt_ecommerce

5. Habilitar la ejecucion de scripts en windows: 
   -  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

6. Ingresar al entorno virtual:
   -  ent_virt_ecommerce/Scripts/Activate

7. Instalar Django o los Requerimientos (requeriments.txt) del proyecto:
   -  pip install django
   -  o
   -  pip install -r requeriments.txt

## Cómo probar:
1. Dentro de la consola de comandos de VS Code:
   -  python manage.py runserver

2. Abrir un navegador Web, ingresar a la direccion:
   -  http://localhost:8000/

3. Desde la barra de navegacion (navbar) superior se puede:
   - Agregar Clientes (`/cliente/`)
   - Agregar Tipos de Documentos (`/tipodoc/`)
   - Agregar Productos (`/producto/`)
   - Crear Pedidos (`/pedido/`)
   - Crear Categorias (`/categoria/`)
   - Buscar clientes (`/buscar/`)

4. Panel Administracion, ingresar a la direccion:
   -  http://localhost:8000/admin
   -  
   -  user: super
   -  pass: super


Consigna
Crea una web en Django utilizando Herencia de plantillas, con un modelo de por lo menos 3 clases, un formulario para ingresar datos a las 3 clases y un formulario para buscar algo en la BD, no hace falta que sea sobre las tres clases, con realizar búsqueda sobre una alcanzará.

Te sugerimos que hagas  una web estilo blog para ir preparando en la entrega final.

Objetivos
[]Desarrollar tu primer WEB en Django utilizando patrón MVT

Requisitos
Link de GitHub con el proyecto totalmente subido a la plataforma.

[]Proyecto Web Django con patrón MVT que incluya:

[]Herencia de HTML.

[]Desarrollo WEB en Django utilizando patrón MVT

[]Por lo menos 3 clases en models.

[]Un formulario para insertar datos a por cada model creado.

[]Un formulario para buscar informacion en la BD (segun los models que se hayan creado)

[]Readme.md, que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.


Formato
Link al repositorio de GitHub con el nombre “TuPrimeraPagina+Apellido”  por ejemplo “TuPrimeraPagina+Fernandez”
