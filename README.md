
# Prueba técnica Fianly

_Este aplicativo permite la autenticación de un usuario mediante su identificador(email) y contraseña, este proceso de autenticación retorna un token con el cual podrá acceder a la información de los usuarios registrados en el sitio._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Para ejecutar el proyecto debemos tener instalado en nuestro equipo el siguiente software:_

```
Docker:

	-Windows y Mac (https://www.docker.com/products/docker-desktop/)
	
	-Ubuntu: Para instalar docker en este sistema operativo debemos de abrir nuestra termial
	 y escibir los siguientes comandos:
	 
		 * sudo apt update
		 * sudo apt upgrade
		 * sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common
		 * curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		 * sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
		 * sudo apt update
		 * sudo apt install docker-ce
	
		 Si tienes problemas durante la instalacion puedes visitar:
		 https://www.hostinger.co/tutoriales/como-instalar-y-usar-docker-en-ubuntu 
		 
Docker Compose:

	-Windows y Mac: Este software viene incluido con la instalación de Docker
	
	-Ubuntu: Para realizar la instalación debemos de escribir los siguientes comandos en nuestra terminal:
	
		* sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
		* sudo chmod +x /usr/local/bin/docker-compose
		
		Si tienes problemas con la instalación puedes visitar la siguiente página:
		https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es 
```

### Instalación y ejecución del proyecto🔧
IMPORTANTE: Debemos abrir la aplicacion de docker en Windows y Mac, una vez hecho esto podemos proseguir con el proceso.
al abrir la aplicacion en windows se podria presentar el error "Hardware assisted virtualization and data execution protection must be enabled in the BIOS", para solucionarlo, basta con abrir una terminal como administrador y correr el comando "bcdedit /set hypervisorlaunchtype auto", reiniciar el pc abrir la aplicacion y continuar con el proceso.

_A continuación se describen los pasos necesarios para tener el proyecto corriendo en nuestro equipo:_

_Para iniciar debemos de descargar el proyecto. Si tenemos git podemos descargar el proyecto fácilmente, entrando a la terminal de nuestro equipo y escribiendo:_

```
-Ubuntu,Windows y Mac:
	* git clone git@github.com:JuanDavidArce/PruebaTecnicaFianly.git
```

_Si no tenemos git instalado, podemos descargar el archivo comprimido desde la siguiente página:
https://github.com/JuanDavidArce/PruebaTecnicaFianly y una vez descargado descomprimimos el archivo._

_Ya descomprimido el archivo o descargada la carpeta, procedemos a entrar a ella (PruebaTecnicaFianly), estando dentro, ingresamos a la carpeta TechnicalTest, una vez allí abrimos una terminal y seguimos con el proceso._

_Tambien podemos movernos hasta dicha carpeta desde una terminal_

_Una vez hecho esto lo primero que vamos a hacer es construir las imágenes y el entorno de Docker necesario para que nuestro proyecto se pueda ejecutar satisfactoriamente, esto lo hacemos con el siguiente comando:_

```
-Windows y Mac:
	* docker-compose build

-Ubuntu:
	* sudo docker-compose build
```

_Una vez construido nuestro entorno vamos a proceder a ejecutarlo con el siguiente comando:_

```
-Windows y Mac:
	* docker-compose up

-Ubuntu:
	* sudo docker-compose up
```

_Con el paso anterior ya deberíamos tener nuestro entorno listo para hacer pruebas y verificar el funcionamiento del proyecto_

## Ejecutando tests ⚙️

_Se tienen 5 tests en el proyecto, para ejecutarlos, debemos ubicarnos en la carpeta mencionada en instalación y ejecución del proyecto y abrir una terminal o también podemos movernos desde una terminal hasta allí._
_Cuando estemos en la terminal escribimos lo siguiente:_
```
-Windows y Mac:
	* docker-compose run --rm django python3 manage.py test

-Ubuntu:
	* sudo docker-compose run --rm django python3 manage.py test
```

### Análisis de los test🔩

_Aquí tenemos 2 diferentes conjuntos de test, uno para el endpoint auth y otro para el endpoint user:_

```
Auth:

- Test Response Success: Enviando una serie de datos correctos al endpoint, verifica que la respuesta sea un status code 200 OK  

- Test Response Bad Request: Verifica que la estructura del JSON enviado al endpoint es la esperada, de no ser así este test válida que la respuesta sea un status code 400 Bad Request

- Test Response Invalid Credentials: Válida que la respuesta del endpoint cuando se le envian unas credenciales inválidas sea un status code 401 unauthotized
```
```
User:

- Test Response Succes: Cuando se envía un token válido, verifica si la respuesta es un status code 200 ok  

- Test Response Invalid Token: Si el usuario envía un token inválido, verifica que la respuesta sea un status code 401 unauthorized
```



## Despliegue 📦

_Agregar notas adicionales sobre como hacer deploy_

## Construido con 🛠️



* Django/Django Rest Framework- El framework web usado
* Python - Lenguaje de programacion
* Docker - Entorno de trabajo aislado


## Autor✒️


* **Juan David Arce Martinez**



