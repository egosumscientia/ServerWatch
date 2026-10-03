# ServerWatch --- Planificación del proyecto

## Objetivo general

Desarrollar progresivamente un mini sistema de monitoreo de servidores
en Python.

El proyecto está orientado al aprendizaje práctico: la complejidad se
incorporará únicamente cuando exista una necesidad real. Inicialmente se
trabajará con datos simulados y, conforme avance el proyecto, podrán
incorporarse archivos, JSON, logging, interacción con Linux, procesos,
networking u otros conceptos si resultan naturales dentro del
desarrollo.

La planificación por fases funciona como una guía general y podrá
ajustarse si durante el desarrollo aparecen mejores decisiones de
diseño.

------------------------------------------------------------------------

## Fase 1 --- Modelo básico de servidor

**Objetivo:** crear la primera representación de un servidor.

El sistema comenzará manejando información básica como:

-   hostname;
-   dirección IP;
-   estado UP/DOWN.

Esta fase permitirá trabajar con clases, objetos, atributos y métodos
básicos sin introducir todavía métricas ni otras responsabilidades.

------------------------------------------------------------------------

## Fase 2 --- Métricas del servidor

**Objetivo:** representar información básica sobre el consumo de
recursos de un servidor.

Se incorporarán progresivamente métricas como:

-   uso de CPU;
-   uso de memoria;
-   uso de disco.

Se trabajará con la actualización y consulta de estas métricas
utilizando inicialmente datos simulados.

------------------------------------------------------------------------

## Fase 3 --- Validación de datos

**Objetivo:** impedir que los objetos del sistema puedan quedar en
estados inválidos.

Se introducirán validaciones sobre los datos que ya existan en el
proyecto, por ejemplo métricas fuera de rangos razonables o estados no
permitidos.

Las validaciones se incorporarán únicamente cuando exista una necesidad
concreta derivada de las fases anteriores.

------------------------------------------------------------------------

## Fase 4 --- Servicios

**Objetivo:** representar los servicios que se ejecutan en un servidor.

El sistema podrá asociar servicios a cada servidor y consultar
información relevante sobre ellos, incluyendo su estado.

Esta fase permitirá trabajar con colecciones y con relaciones entre
diferentes elementos del dominio.

------------------------------------------------------------------------

## Fase 5 --- Evaluación de salud

**Objetivo:** permitir que ServerWatch determine el estado general de
salud de un servidor.

La evaluación podrá considerar información como:

-   disponibilidad del servidor;
-   métricas;
-   estado de sus servicios.

Las reglas concretas se definirán cuando lleguemos a esta fase.

------------------------------------------------------------------------

## Fase 6 --- Alertas

**Objetivo:** detectar automáticamente condiciones anormales.

El sistema podrá identificar situaciones como:

-   uso elevado de CPU;
-   uso elevado de memoria;
-   poco espacio disponible en disco;
-   servicios detenidos;
-   servidor no disponible.

A partir de estas condiciones se introducirán alertas dentro del
sistema.

------------------------------------------------------------------------

## Fase 7 --- Monitoreo de múltiples servidores

**Objetivo:** evolucionar desde el monitoreo de un servidor individual
hacia la administración de varios servidores.

ServerWatch deberá poder mantener una colección de servidores y realizar
operaciones sobre ellos.

En esta fase podrá surgir naturalmente la necesidad de una entidad que
represente el propio sistema de monitoreo.

------------------------------------------------------------------------

## Fase 8 --- Historial de mediciones

**Objetivo:** conservar información de mediciones anteriores.

Hasta este punto las métricas podrán representar principalmente el
estado actual. En esta fase se estudiará cómo registrar mediciones a lo
largo del tiempo.

Esto permitirá comenzar a observar cambios y comportamiento histórico.

------------------------------------------------------------------------

## Fase 9 --- Persistencia

**Objetivo:** conservar información entre diferentes ejecuciones del
programa.

Se evaluará el uso de:

-   archivos;
-   JSON;
-   lectura y escritura de datos.

La estructura concreta se decidirá según el estado real del proyecto al
llegar a esta fase.

------------------------------------------------------------------------

## Fase 10 --- Interfaz de consola

**Objetivo:** permitir operar ServerWatch desde una terminal.

La interfaz podrá ofrecer operaciones como:

-   consultar servidores;
-   consultar métricas;
-   consultar servicios;
-   visualizar estados;
-   consultar alertas.

No se definirá anticipadamente una interfaz compleja; se construirá a
partir de las funcionalidades que ya existan.

------------------------------------------------------------------------

## Fase 11 --- Logging y manejo de errores

**Objetivo:** mejorar la observabilidad y robustez de la aplicación.

Se podrá incorporar:

-   logging;
-   manejo de excepciones;
-   tratamiento de errores de archivos;
-   tratamiento de datos inválidos;
-   registro de eventos relevantes.

Esta fase deberá aprovechar situaciones reales que hayan aparecido
durante el desarrollo anterior.

------------------------------------------------------------------------

## Fase 12 --- Monitoreo real

**Objetivo:** comenzar a reemplazar algunos datos simulados por
información obtenida del sistema real.

Dependiendo de cómo haya evolucionado ServerWatch, podrán explorarse
conceptos como:

-   información real de CPU;
-   memoria;
-   disco;
-   procesos;
-   servicios de Linux;
-   conectividad;
-   networking.

El alcance exacto se decidirá únicamente al llegar a esta fase.

------------------------------------------------------------------------

## Posibles extensiones

Las siguientes funcionalidades **no forman parte obligatoria del
proyecto**:

-   testing automatizado;
-   base de datos;
-   API;
-   interfaz gráfica;
-   monitoreo remoto;
-   concurrencia;
-   otras integraciones.

Solo se incorporarán si existe una razón concreta para hacerlo y aportan
valor al aprendizaje o al funcionamiento de ServerWatch.

------------------------------------------------------------------------

## Metodología de desarrollo

El proyecto se desarrollará bajo las siguientes reglas:

1.  Se trabajará una sola fase a la vez.
2.  Dentro de cada fase se trabajará un solo paso a la vez.
3.  El estudiante escribirá todo el código de implementación.
4.  No se proporcionará código de solución inicialmente.
5.  Cada paso indicará qué debe conseguirse, el comportamiento esperado,
    las restricciones y los casos importantes.
6.  Después de cada paso se revisará la implementación antes de
    continuar.
7.  No se avanzará mientras el paso actual tenga errores pendientes.
8.  Ante dificultades se proporcionarán pistas progresivas antes de
    mostrar una solución.
9.  Las decisiones importantes de diseño con varias alternativas
    razonables se discutirán antes de elegir una.
10. No se incorporarán funcionalidades correspondientes a fases futuras.
11. Se preservará el comportamiento correcto conseguido en las fases
    anteriores.
12. La estructura del proyecto se reorganizará únicamente cuando la
    complejidad real lo justifique.
13. La planificación podrá ajustarse durante el desarrollo si aparece
    una razón técnica o pedagógica clara.

------------------------------------------------------------------------

## Principio del proyecto

**La complejidad debe aparecer como consecuencia de una necesidad real,
no porque se haya diseñado anticipadamente.**
