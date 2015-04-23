# android_app
A simple app for andoid to read/write data from server.

##  Linux

### Instalación

Es necesario instalar pip:

```sh
$ apt-get install python-pip
```

Instalamos virtualenv con el siguiente comando:

```sh
$ pip install virtualenv
```

Establecemos nuestro ambiente de desarrollo:


```sh
$ mkdir project
$ cd project
$ virtualenv --no-site-packages env
$ cd env
$ source bin/activate
```

Se debería ver (env) ante de tu prompt, (env)$, indicando que estamos corriendo en el ambiente virtual ‘env’.
Para salir del virtual env, tipeamos:

```sh
$ deactivate
```

Ahora clonamos el proyecto, dentro de la carpeta env:

```sh
$ git clone https://github.com/jjrevilla/android_app.git
```

Entramos a la carpeta del repositorio e instalamos Django y todas las dependencias para el proyecto:

```sh
$ pip instal -r requirements.txt
```

Ahora solo ejecutamos el servidor

```sh
$ python manage.py runserver 
```

Revisamos las tablas de las bases de datos:

 - localhost:8000/api/articulos
 - localhost:8000/api/pedidos
