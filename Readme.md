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


## Orden de pruebas y funcionalidades principales

1.Inicio
- URL: /
- Muestra la página principal del proyecto con acceso al resto de las secciones desde la barra de navegación superior.

2.Clientes
- URL: /cliente/
- Formulario para agregar clientes asociados a un tipo de documento.

3.Tipos de Documentos
- URL: /tipodoc/
- Permite crear, los tipos de documento (por ejemplo: DNI, Pasaporte).

4.Productos
-  URL: /producto/
-  Permite crear productos asociados a una categoría.
-  Si no se carga imagen, se muestra una imagen por defecto (no_image.jpg).

5.Pedidos
- URL: /pedido/
- Formulario que permite seleccionar un cliente y un producto para registrar un pedido.


6.Categorias
- URL: /categoria/
- Permite crear categorías para los productos (por ejemplo: Electrónica, Ropa, etc.).

7.Búsqueda de clientes
- URL: /buscar/
- Permite buscar clientes por nombre o documento en la base de datos.

8.Panel de administración
-URL: /admin/
-Usuario: super
-Contraseña: super
- Desde aquí se pueden gestionar todos los modelos: Clientes, Categorías, Productos, Pedidos, Tipos de Documento, etc.


#Prueba sugerida
- 1. Crear Tipo de Documento (DNI ya esta creado, puede crear LC o LE).
- 2. Crear Cliente
- 3. Crear Categoria (TV Led, TV Smart y Radio ya estan creados, se puede crear Climatizacion, Pequeños Electrodomesticos, etc)
- 4. Crear Productos
- 5. buscar los productos (por nombre o descripcion)
- 6. Crear Pedidos
- 7. Revisar todo desde el panel de administracion.


##Consigna sobre trabajo Prctico
- Crea una web en Django utilizando Herencia de plantillas, con un modelo de por lo menos 3 clases, un formulario para ingresar datos a las 3 clases y un formulario para buscar algo en la BD, no hace falta que sea sobre las tres clases, con realizar búsqueda sobre una alcanzará. Te sugerimos que hagas  una web estilo blog para ir preparando en la entrega final.

##Objetivos
- []Desarrollar tu primer WEB en Django utilizando patrón MVT

##Requisitos:
- []Proyecto Web Django con patrón MVT que incluya:

- []Herencia de HTML. (las paginas webs heredan de base.htm)
- []Desarrollo WEB en Django utilizando patrón MVT (se uso: Template > URL > View (Logica) )
- []Por lo menos 3 clases en models. (se crean 6: "TipoDoc", "Cliente", "Categoria", "Producto", "Pedido", "ContadorVisitas")
- []Un formulario para insertar datos a por cada model creado. (se crean para "TipoDoc", "Cliente", "Categoria", "Producto", "Pedido")
- []Un formulario para buscar informacion en la BD (segun los models que se hayan creado). (El buscador busca productos por nombre y descripcion)
- []Readme.md, que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades. 
- []Link de GitHub con el proyecto totalmente subido a la plataforma.

##Formato
- Link al repositorio de GitHub con el nombre “TuPrimeraPagina+Apellido”  por ejemplo “TuPrimeraPagina+Fernandez” (Dentro del link del proyecto se deja un .zip con TuPrimeraPagina+MartinHernandez)
