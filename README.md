
# Prueba técnica Fianly

_Este aplicativo permite la autenticación de un usuario mediante su identificador(email) y contraseña, este proceso de autenticación retorna un token con el cual podrá acceder a la información de los usuarios registrados en el sitio._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

## Estructura del proyecto

El proyecto consiste de 2 endpoints:

#### /auth/:

Este endpoint nos permite hacer autenticación, haciendo uso de un user_id, el cual vamos a asumir será un email, y de una contraseña. La estructura de la petición (POST) es la siguiente:

```
{ 

     "user":"example@gmail.com",
     "password":"example123"
     
}

```

Si las credenciales son correctas la respuesta esperada es:

```

{

    "token": "fas4df54ds5fsad5fs4d5f4a5f4ds5f45sa4f5sd",
    "user_name": "example"
    
}

```
#### /user/:

Este endpoint nos permite acceder a los nombres y apellidos de las personas registradas, para hacer uso de ella, realizamos una peticion(GET) y en los Headers vamos a agreagar la key "Authorization"  con el valor "Bearer exampletoken", para mayor comprension se recomienda ver la imagen de ejemplo de una peticion mediante postman un poco mas abajo.

Si el token es valido la respuesta esperada es:
```
[

    {
        "first_name": "Example",
        "last_name": "Example"
    }
    

]
```


Se recomienda ampliamente hacer las peticiones mediante Postman:

Asi luce una peticion a /auth/ desde postman:


![auth endpoint postman](https://i.ibb.co/gyWtBNT/image.png)

Asi luce una peticion a /user/ desde postman:

![user endpoint postman](https://i.ibb.co/h7HMgB0/image.png)


### Pre-requisitos 📋

NOTA: Si no deseamos realizar instalación local, revisar primero la sección Despliege

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
	* git clone https://github.com/JuanDavidArce/PruebaTecnicaFianly.git
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
_El proyecto cuenta con los siguientes datos para que hagamos pruebas mediante las peticiones explicadas en la estructura del proyecto, estas peticiones las hacemos a la direccion localhost:8000/endpoint/ :_

```

first_name		last_name	password	username	email
Juan David		Arce Martinez	prueba1		juandavid	juandavid@gmail.com
Laura Sofia		Perez Osorio	prueba2		laura		laura@gmail.com
Raul 			Alvares		prueba4		raul		raul@gmail.com
Carlos			Martinez	prueba5		carlos		carlos@gmail.com
Pedro Arturo		Reyes		prueba6		pedro		pedro@gmail.com
Santiago		Flores		prueba7		santiago	santiago@gmail.com
Camilo			Morales		prueba8		camilo		camilo@gmail.com

```

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

_Para hacer deploy es bastante fácil gracias a las facilidades de Docker, para ello solo necesitamos instalar Docker y Docker Compose en nuestro servidor, posterior a esto ejecutar los mismos comandos mencionados en instalación y ejecución, habilitar el puerto en el servidor para que sea accesible, y con esto ya tendríamos nuestra aplicación desplegada._
_para nuestro caso tenemos la aplicación desplegada en aws, y podemos hacerle peticiones a las siguientes direcciones:_

```
http://3.144.226.58:8000/auth/
http://3.144.226.58:8000/user/
```

## Construido con 🛠️



* Django/Django Rest Framework- El framework web usado
* Python - Lenguaje de programacion
* Docker - Entorno de trabajo aislado


## Autor✒️


* **Juan David Arce Martinez**



