# ServerWatch --- Fase 2: Métricas del servidor

## Estado previo

La **Fase 1 --- Modelo básico de servidor** está completada.

Actualmente existe la clase `Server`, definida en `server.py`, con:

-   `hostname`
-   `ip_address`
-   `status`, inicializado en `"DOWN"`
-   `mark_up()`
-   `mark_down()`
-   `toggle_status()`
-   `is_up()`
-   `get_info()`
-   `__str__()`

La Fase 1 estableció la representación básica y el manejo del estado de
un servidor.

------------------------------------------------------------------------

## Objetivo de la Fase 2

Incorporar métricas básicas de utilización de recursos a cada servidor.

Las métricas iniciales serán:

-   `cpu_usage`
-   `memory_usage`
-   `disk_usage`

Estas métricas representarán porcentajes de utilización.

Durante esta fase los datos seguirán siendo **simulados**. Todavía no se
obtendrá información real del sistema operativo.

------------------------------------------------------------------------

## Alcance

La fase deberá permitir progresivamente:

-   representar las métricas de cada servidor;
-   mantener sus valores como parte del estado de cada instancia;
-   actualizar las métricas;
-   consultar las métricas;
-   integrar las métricas de manera coherente con el modelo `Server`
    existente.

La implementación concreta se decidirá paso a paso durante el
desarrollo.

------------------------------------------------------------------------

## Fuera de alcance

En esta fase no se introducirán anticipadamente:

-   validaciones de rangos o tipos, salvo que se decida explícitamente
    cambiar el plan;
-   servicios;
-   evaluación automática de salud;
-   alertas;
-   historial de mediciones;
-   archivos o JSON;
-   persistencia;
-   logging;
-   obtención real de métricas desde Linux;
-   networking;
-   base de datos;
-   interfaz gráfica.

La **validación de datos corresponde inicialmente a la Fase 3**.

------------------------------------------------------------------------

## Reglas de desarrollo

1.  Trabajar un solo paso a la vez.
2.  El usuario escribe todo el código de implementación.
3.  No proporcionar código de solución inicialmente.
4.  Cada paso debe indicar qué conseguir, el comportamiento esperado,
    las restricciones y los casos importantes.
5.  Revisar la implementación del usuario antes de avanzar.
6.  No avanzar mientras el paso actual tenga errores pendientes.
7.  Si el usuario se atasca, proporcionar pistas progresivas antes de
    mostrar una solución.
8.  No introducir funcionalidades de fases posteriores.
9.  Preservar todo el comportamiento correcto conseguido en la Fase 1.
10. Evitar sobrearquitectura.
11. Cuando exista una decisión de diseño importante con varias
    alternativas razonables, explicar brevemente las opciones y
    preguntar antes de decidir.
12. El asistente diseña y realiza las pruebas; el usuario se concentra
    en implementar la lógica.
13. Al introducir nuevos elementos, indicar explícitamente cómo nombrar
    archivos, clases, métodos, atributos, funciones u otros componentes,
    salvo que decidir el nombre sea parte deliberada del ejercicio.

------------------------------------------------------------------------

## Punto de inicio

El primer trabajo de la Fase 2 será incorporar a cada instancia de
`Server` los atributos:

-   `cpu_usage`
-   `memory_usage`
-   `disk_usage`

Inicialmente las tres métricas comenzarán en `0`.

En ese primer paso no se agregarán todavía validaciones, métodos de
actualización ni cambios en `get_info()`.

------------------------------------------------------------------------

## Principio de la fase

Las métricas se incorporarán de la forma más simple posible y la
complejidad adicional aparecerá únicamente cuando una necesidad concreta
del proyecto la justifique.
