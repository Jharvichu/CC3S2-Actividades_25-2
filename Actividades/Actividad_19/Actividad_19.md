# Actividad19_CC3S2

## Bloque 1

**1.** Ejecutando: `docker build --no-cache -t ejemplo-microservice:0.1.0 .`

Construimos la imagen desde un inicio (sin el caché) y se le añade una etiqueta.

![b1_1](img/b1_1.png)

![b1_2](img/b1_2.png)

**2.** Ejecutando: `docker run --rm -d --name ejemplo-ms -p 80:80 ejemplo-microservice:0.1.0`

Iniciamos el contenedos en segundo plano, lo nombramos y abrimos en el puerto 80 para acceder a su servicio desde un navegador.

![b1_3](img/b1_3.png)

**3.** Ejecutando: `curl -i http://localhost/api/items/`

Enviamos una petición al servicio (GET) y nos muestra las cabeceras y la respuesta que devuelve.

![b1_4](img/b1_4.png)

**4.** Ejecutando: `docker logs -n 200 ejemplo-ms`

Para mostrar los últimos 200 logs del contenedor.

![b1_5](img/b1_5.png)

**5.** Ejecutando: `docker rm -f ejemplo-ms && docker image prune -f`

Borramos el contenedor y limpiamos las imágenes que ya no son necesarias.

![b1_6](img/b1_6.png)

## Bloque 2

**Ejercicios de Redacción**

**1.** Tres escenarios donde Docker Compose mejora el flujo diario

Docker compose nos ayuda bastante cuando trabajamos con diferentes servicios a la vez. Por ejemplo, si queremos simular una situación parecido a la de producción, entonces podemos levantar una API, una base de datos y un caché, todo esto con un solo comando, sin tener la necesidad de configurar cada cosa de manera separada.

También esto nos facilita las pruebas de integración porque ya no necesario instalar o correr servicio de manera manual, solo tendriamos que definirlos en el archivo y el `compose` los arma.

Ahora, para situaciones diarias es muy comodo porque podemos vincular nuestro código al contenedor, aplcando cualquier cambio al instante gracias a la opción `--reload`.

**2.** Por qué usar perfiles

Los perfiles nos ayudan a organizar mejor nuestros entornos y evita que todo se ejecute siempre. Por ejemplo, podemos tener nu perfil de desarrollo para desarrollo/codificación con recarga automática y otro perfil completamente diferente que usa imágenes "limpias" sin montajes.

Entonces, gracias a los perfiles, podemos correr solamente que lo necesitemos para cada caso.

**3.** Fragmento conceptual de `docker-compose.yml`

La idea de este archivo es definir, dentro de esta, los servicios que nuestro proyecto necesita. Por ejemplo podriamos tener un servicio principal que use una imagen personalizada, exponiendo puertos y montando carpetas de trabajo para que los cambios se muestren de forma inmediata.

En este archivo también podriamos incluir servicios de caché y, por último, podriamos configurarlo para que el servicio general dependa del servicio de caché.