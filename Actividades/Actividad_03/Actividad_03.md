# **Actividad 3: Integración de DevOps y DevSecOps con HTTP, DNS, TLS y 12-Factor App**

## **Parte Teórica**

### **1. Introduccion a DevOps**

DevOps es un cambio cultural organizacional que busca integrar los procesos entre los equipos de desarrolladores, control de calidad y operaciones, asi evitando silos organizacionales y acortando el ciclo de vida del desarrollo de software.

#### **Del código a la producción:**

DevOps influye en el ciclo de vida de las aplicaciones a lo largo de su desarrollo. Es cierto que cada fase depende de otras, pero el cambio organizacional que es DevOps realiza, es que todos los equipos esten implicados de algun modo en todas las fases.

- Planificación y Código: Los equipos definen las caracteristicas del sistema, y comienzan a escribir código
- Pruebas: El código avanzado se ejecuta automaticamente y se ejecutan pruebas unitarias y de integración. Si las pruebas fallan, el equipo puede darnos feedback.
- Pipeline CI-CD: Cada cambio en el código activa un pipeline de CI que integra el nuevo código con el repositorio principal. Una vez que pase el pipeline (pruebas, validaciones, etc) se empaqueta y se despliega automáticamente en entornos de staging y producción.
- Operación y Monitoreo: Después del despliegue, el equipo de operaciones supervisa la aplicación, recopilando métricas y logs para identificar y resolver problemas de manera proactiva.

#### **DevOps vs Waterfall**

A diferencia de **DevOps**, el modelo **Waterfall** es un enfoque secuencial y lineal para el desarrollo de software. Cada fase (análisis de requisitos, diseño, implementación, pruebas y despliegue) debe completarse antes de que comience la siguiente.

#### **You Build It, You Run It**

Esta idea central de DevOps significa que el equipo que crea el código también es responsable de su funcionamiento en producción. Esto genera mayor responsabilidad y colaboración, eliminando las barreras tradicionales entre equipos.

#### **Mitos y Realidades**

1. **Mitos**
   1. "DevOps son solo herramientas": Falso. Las herramientas (como Jenkins o Docker) son importantes, pero la base es la cultura de colaboración entre equipos.
   2. "DevOps es un equipo": Falso. DevOps no es un rol o un equipo separado, sino una forma de trabajar que toda la organización debe adoptar.
2. **Realidades**
   1. Principios CALMS: El éxito de DevOps depende de su filosofía, basada en cinco pilares: Cultura, Automatización, Lean, Medición y Sharing.
   2. Feedback y métricas: Se utilizan datos y métricas para mejorar procesos y tomar decisiones informadas, no para culpar a alguien.
   3. Gates (Puertas de Calidad): Puntos de control automatizados en el proceso de despliegue que garantizan que el código cumpla con los estándares de calidad antes de llegar a producción.

### **2. Marco CALMS en accion**

El marco CALMS es un modelo para entender y aplicar los principios de DevOps. No es un conjunto de herramientas, sino una guía cultural y técnica para mejorar el flujo de trabajo de desarrollo de software

1. **C de Cultura**: La cultura se enfoca en la colaboración, confianza y transparencia entre los equipos de desarrollo y operaciones. Se trata de romper los silos y crear un entorno donde la responsabilidad es compartida. En el laboratorio al utilizar un control de versiones como **git**, fomenta la colabopracion para solucionar errores o mejorar codigo.

2. **A de Automatizacion**: La automatización busca eliminar tareas manuales y repetitivas para reducir errores y acelerar el ciclo de entrega. Es la clave para implementar la integración y despliegue continuo (CI/CD). Se aplica este pilar al tener un **makefile** en el laboratorio, ya que tiene targets que automatizan entornos virtuales, isntalaciones, etc.

3. **L de Lean**: El enfoque Lean busca optimizar el flujo de trabajo para entregar valor al cliente lo más rápido posible. Esto implica identificar y eliminar "desperdicios" como esperas, procesos burocráticos y defectos. En este laboratorio al tener variables de entorno como `APP_NAME`, `DOMAIN` y `PORT` hace que la configuracion se reproducible y estandarizada, eliminando el desperdicio de tiempo y errores de configuracion.

4. **M de Medicion**: La medición implica recopilar datos para obtener insights sobre el rendimiento del sistema y el proceso. Las métricas permiten a los equipos tomar decisiones basadas en evidencia y no en suposiciones. En el **Makefile** al tener como target el `make check-http` aplica este pilar ya que verifica el estado de la aplicacion, puertos, conexiones, etc.

5. **S de Sharing**: El pilar de Sharing se centra en compartir conocimientos y aprender de los éxitos y fracasos. Esto incluye compartir herramientas, procesos y, lo que es más importante, las lecciones aprendidas.

### **3. Visión cultural de DevOps y paso a DevSecOps**

DevOps propone que los equipos trabajen juntos desde el inicio del ciclo de vida del software hasta el final. Esta colaboración continua es la base para integrar la seguridad, transformando DevOps en DevSecOps. En lugar de una revisión de seguridad al final del proceso, la seguridad se *desplaza a la izquierda* (**shift-left**), lo que significa que se incorpora desde la fase de planificación, codificación y pruebas, garantizando que el software sea seguro desde el principio.

#### **Escenario de fallo y controles de seguridad**

Imagina que un certificado TLS de tu aplicación caduca. En un entorno DevSecOps, la mitigación cultural implica que los equipos de desarrollo y operaciones trabajen juntos para resolver el problema y, lo que es más importante, para implementar un control automatizado que evite que vuelva a suceder.

#### **Controlles clave de seguridad**

1. Analisis estatico de codigo (SAST):
   
   Se escanea el código fuente de la aplicación en busca de vulnerabilidades comunes como inyecciones SQL, cross-site scripting (XSS) o credenciales codificadas, mayormente esta en el pipepine CI.

2. Configuracion de cabeseras TLS:

    Se revisa la configuración del servidor web para asegurar que solo se utilicen protocolos y cifrados seguros. El archivo de Nginx ya muestra esto con `ssl_protocols TLSv1.2 TLSv1.3`. Este control se integra en el despliegue continuo.
   
3. Analisis de vulnerabilidades de dependencias:

    Se inspecciona las dependencias del proyecto (por ejemplo, la lista de librerías de Python) en busca de vulnerabilidades conocidas. Este control se ejecuta en el pipeline CI de igual manera que el SAST.

### **4. Metodología 12-Factor App**

- **Config en el entorno**: parámetros como `PORT`, `MESSAGE` y `RELEASE` se leen como variables de entorno.  
- **Port binding**: la aplicación expone un puerto (8080) sin depender de servidores externos.  
- **Logs como flujo de eventos**: lo que ocurre en la app aparece en `stdout`.  
- **Procesos sin estado**: la aplicación no guarda datos en disco, lo que facilita escalarla o reiniciarla.  