# Actividad 1: Introduccion DevOps, DevSecOps

## DevOps vs Cascada tradicional

### 1. Diagrama comparativa

<p align="center">
  <img src="Imagenes/devops-vs-cascada.png" alt="Descripción" width="600"/>
</p>

#### **Cascada tradicional**

El modelo tradicional de cascada tiene un enfoque lineal y secuencial para el desarrollo de software, donde cada fase debe completarse antes de comenzar la otra fase. Las caracteristicas principales de este modelo es:

- Es rigido a los cambios una vez una fase se haya completado.
- Los usuarios finales no ven el software hasta las ultimas etapas.
- Los errores o malentendidos en fases iniciales pueden ser muy costosos.
- Cada fase ponen una gran enfasis en la documentacion.

#### **DevOps**

DevOps es una cultura, un conjunto de practicas y herramientas que integra a los equipos de desarrollo, equipos de calidad y equipos de operaciones para automatizar y agilizar procesos en todas las areas. Su objetivo principal es acortar el ciclo de vida del desarrollo y proporcionar software de alta calidad. Sus caracteristicas principales:

- Colaboracion continua y la eliminacion de silos organizacionales entre equipos.
- Automatizacion de pruebas, despliegues y monitoreo.
- Feedback continuo de forma rapida
- Monitoreo del rendimiento y salud de las aplicaciones en produccion.

### 2. Por qué DevOps acelera y reduce el riesgo en software para la nube frente a la cascada

Muchas caracteristicas de DevOps hacen que sea mas seguro y ventajoso para el desarrollo de software, como:

- Es facil desplegar rapidamente nuevas funcionalidades a un conjuntos de usuarios o a entornos de prueba, lo que nos permite obtener feedback de inmediato, evitandonos errores o problemas de diseño en la funcionalidad que implementamos, asi dandonos tiempo de corregir cuando el coste de cambio es aun menor.
- Se promueve la entrega continua de nuevas funcionalidades en pequeños lotes, estos cambios generalmente son pequeños y aislados, asi reduciendo  complejidad y riesgos en los despliegues ademas de ofrecer al usuario nuevas caracteristicas o correcciones en tiempo record.
- La automatizacion de la integracion continua (CI) y despliegue continuo (CD) aseguran los pasos de pruebas y despliegue se realicen sin errores, asi evitando cuellos de botella manuales, errores humanos y reduciendo el tiempo.

### 3. Contexto real donde un enfoque cercano a cascada sigue siendo razonable

Si bien DevOps es ampliamente adoptado, existen contextos donde un enfoque más cercano al modelo de cascada puede ser razonable o incluso preferible, especialmente cuando la razón principal es la seguridad y la fiabilidad por encima de la velocidad de desarrollo. Un ejemplo podria ser un software para plantas nucleares.

1. **Requisito de Seguridad y Certificacion Extrema**
   1. **Criterio Verificable** El software diseñado debe cumplir con regulaciones internacionales extramadamente estrictas y pasar un proceso de certificacion riguroso, cada linea de codigo debe ser revisada, probada y documentada formalmente.
   2. **Trade-off**: El proceso es muy blento y burocratico, asi que la velocidad de DevOps, con sus iteraciones y despligues frecuentes, seria riesgoso mas que todo por el tiempo y que un error podria provocar consecuencias graves. El modelo de cascada, con sus fases estrictas nos permite que cada fase sea validado, priorizando la seguridad por encima de otro factor.
2. **Acoplamiento inmutable con Hardware Critico**
   1. **Criterio Verificable** El software diseñado debe trabajar con un hardware de alto costo, que no se puede actualizar o reemplazar facilmente
   2. **Trade-off**:  La fiabilidad y la estabilidad a lo largo de la vida útil del sistema son el objetivo principal. El modelo de cascada invierte un tiempo significativo en la fase de diseño inicial para garantizar que el software sea compatible y robusto con este hardware desde el principio. Un enfoque de DevOps podría introducir incompatibilidades impredecibles o bugs en el sistema que serían casi imposibles.
   


