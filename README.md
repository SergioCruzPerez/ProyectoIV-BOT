[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.org/natalia2911/ProyectoIV-BOT.svg?branch=master)](https://travis-ci.org/natalia2911/ProyectoIV-BOT)

# Proyecto IV : Bot Noticiero

Repositorio creado para la asignatura de Infraestructura Virtual, de 4º curso, en el grado de Ingeniería Informática (GII) de la Universidad de Granada (UGR) en el curso 2018-2019

## Descripción

Mi proyecto para este curso se basará en crear un micro-servicio en la nube el cual será usado por un bot de Telegram que nos indique las noticias del día o de días anteriores.
Nuestro usuario podrá consultar las noticias de diferentes días, según la petición propia del usuario.

## Herramientas

- El lenguaje en que programaremos nuestro proyecto será en Python. He decidido usar este lenguaje ya que es un lenguaje que actualmente está en auge y creo que podría aportarme muchas cosas aprenderlo en profundidad.

- Para realizar este proyecto usaremos un entorno virtual de desarrollo adecuado a python el cual será `virtualenv` para más información sobre este entorno de desarrollo [pinche aquí](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-entornovirtual.md).


- Hemos pensado en usar un determinado editor de texto, en este caso será Atom ([Más información](https://atom.io/)

- Será gestionado por una base de datos donde almacenemos todo tipo de noticias, podremos usar tanto [MySQL](https://www.mysql.com/), como [MariaDB](https://mariadb.org/), aun no lo tenemos completamente definido.

- Para realizar el testeo vamos a utilizar la librería `unittest` por su gran variedad de funcionalidades. [Más información](https://docs.python.org/3/library/unittest.html)

- El micro-framework que vamos a usar será `Flask` ya que me parece que será una buena herramienta para usar con Python, para desarrollar nuestro micro servicio.

- Ahora mismo utilizaremos `ficheros JSON` para el almacenamiento estatico, más tarde procederemos a implementar la BBDD.

- Para realizar los test usaremos [Travis-CI](https://travis-ci.org/)


## Integración Continua

Para hacer realizar los test vamos a usar la clase `funciones.py` donde podremos obtener todas las noticias de un determinado día, las noticias que un usuario público en un determinado momento, añadir una noticia a la lista de noticias.

El uso que esta clase tendría sería mostrar y añadir noticias, teniendo en cuenta que se añade una noticia en el día actual, y esto se añadiría a nuestra aplicación de noticias.

Para instalarla y probarla tendremos que instalar los `requirements.txt` y con los archivos de la carpeta `src`, ejecutamos la clase `test.py`, con esto bastaría para poder probarla.

Para más información ir a: [más info](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-integracionCont.md)


## Despliege y configuración de un PaaS - Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Para que nuestro micro servicio comience a funcionar se ha elegido como PaaS : Heroku

Para quien no sepa que es un Paas aquí dejo un pequeña explicación :

El concepto de Plataforma como Servicio (PaaS, Platform as a Service) es una categoría de servicios cloud que proporciona una plataforma y un entorno que permiten a los desarrolladores crear aplicaciones y servicios que funcionen a través de Internet. Los servicios PaaS se alojan en la nube, y los usuarios pueden acceder a ellos simplemente a través de su navegador web. [Más info](https://www.interoute.es/what-paas)


#### Motivos por los que se ha elegido Heroku

Las características principales de Heroku son:
1.  Es una plataforma totalmente gratuita
2. Podemos crear un dyno, que puede ejecutar un máximo de dos tipos de procesos
3. Nuestro dyno utiliza 512 Mb de RAM
4. Tras 30 minutos de inactividad el dyno se para (sleep), además debe estar parado 6 horas cada 24 horas.
5. Podemos utilizar una base de datos postgreSQL con no más de 10.000 registros

Una de las cosas que nos ha hecho elegirlo ha sido:

	- Sobre todo que es gratis
	- Permite la integración con Github
	- Permite también con Travis-CI
	- y es muy fácil de manejar.


**Despliegue** https://noticiero-app.herokuapp.com/


[Más información consultar Documentación](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-confPaaS.md)


## Configuración de entorno de pruebas usando contenedores : DOCKER

Contenedor: [https://contenedornoticias.herokuapp.com/](https://contenedornoticias.herokuapp.com/)

Hemos usado `Docker`, como contenedor. Así como el despliegue del contenedor lo hemos realizado en `Heroku`, la publicación de la imagen ha sido en `DockerHub`.

URL del despliege de la imagen: https://hub.docker.com/r/natalia2911/proyectoiv-bot/


Más información sobre lo que hemos usado:
	- [Nuestra Documentación](https://github.com/natalia2911/ProyectoIV-BOT/blob/master/doc/doc-docker.md)


Información adicional:
		- [Información Docker](https://www.docker.com/)
		- [Información Heroku](https://dashboard.heroku.com/)
		- [Información DockerHub](https://hub.docker.com/)
