# Fase 4 — Gestión de múltiples servidores

## Objetivo

Convertir ServerWatch de un modelo capaz de representar un servidor individual en un sistema capaz de administrar múltiples servidores.

La fase estará centrada principalmente en escribir lógica Python nueva.

Se introducirá una clase responsable de mantener y operar sobre una colección de objetos `Server`, reutilizando todo lo construido durante las Fases 1, 2 y 3.

---

## Estado inicial

Actualmente existe:

`src/server.py`

con la clase:

`Server`

Cada instancia mantiene:

- `hostname`
- `ip_address`
- `status`
- `cpu_usage`
- `memory_usage`
- `disk_usage`

También dispone de comportamiento para:

- cambiar el estado entre `UP` y `DOWN`;
- consultar si el servidor está `UP`;
- actualizar métricas;
- simular métricas;
- validar tipos y rangos de métricas;
- obtener información mediante `get_info()`;
- representar el servidor mediante `__str__()`.

Las métricas aceptan `int` y `float`, rechazan `bool` y deben permanecer entre `0` y `100`.

Una actualización inválida lanza `ValueError` y no modifica parcialmente las métricas.

Todo ese comportamiento debe preservarse.

---

## Nueva responsabilidad

Durante esta fase se creará:

`src/server_manager.py`

con una clase:

`ServerManager`

`ServerManager` será responsable de administrar un conjunto de objetos `Server`.

La clase `Server` seguirá representando un servidor individual.

La clase `ServerManager` representará la colección y las operaciones relacionadas con varios servidores.

Esta separación permitirá practicar composición entre objetos sin introducir herencia ni arquitecturas innecesarias.

---

## Alcance de la Fase 4

La fase se desarrollará progresivamente y cubrirá:

1. Crear `ServerManager`.
2. Mantener internamente una colección de servidores.
3. Agregar objetos `Server` a la colección.
4. Consultar los servidores administrados.
5. Buscar un servidor por `hostname`.
6. Definir y manejar el comportamiento frente a servidores duplicados.
7. Eliminar servidores.
8. Filtrar servidores según su estado operativo.
9. Obtener servidores `UP`.
10. Obtener servidores `DOWN`.
11. Realizar operaciones sencillas sobre la colección cuando sean necesarias para consolidar la lógica de gestión.
12. Preservar completamente el comportamiento existente de `Server`.

No se implementará todo al mismo tiempo.

Cada capacidad será introducida mediante pasos pequeños.

---

## Conceptos de Python que se practicarán

Esta fase debe servir para practicar principalmente:

- creación y uso de clases;
- composición entre objetos;
- colecciones;
- listas y/o diccionarios según las decisiones de diseño;
- almacenamiento de objetos dentro de colecciones;
- iteración;
- búsqueda;
- condiciones;
- retorno de objetos;
- filtrado;
- eliminación de elementos;
- métodos de instancia;
- responsabilidades entre clases;
- control de flujo;
- manejo de casos donde una búsqueda no produce resultados;
- prevención de estados inconsistentes.

El objetivo no es únicamente conseguir que ServerWatch funcione, sino escribir y razonar sobre esta lógica manualmente.

---

## Nombres iniciales

Archivo nuevo:

`src/server_manager.py`

Clase nueva:

`ServerManager`

Durante la fase se introducirán progresivamente métodos relacionados con operaciones como:

- agregar servidores;
- buscar servidores;
- eliminar servidores;
- obtener servidores;
- filtrar por estado.

Los nombres concretos de los métodos serán indicados al comenzar el paso correspondiente.

No deben crearse todos anticipadamente.

---

## Relación entre `ServerManager` y `Server`

`ServerManager` trabajará con instancias existentes de `Server`.

Conceptualmente:

`Server` representa un servidor.

`ServerManager` administra varios `Server`.

No se utilizará herencia entre estas clases.

`ServerManager` no debe duplicar la lógica interna que ya pertenece a `Server`.

Por ejemplo, la lógica para cambiar un servidor a `UP` seguirá perteneciendo a `Server`.

---

## Decisiones de diseño que deben discutirse antes de implementarse

Si durante la fase aparece una decisión con varias alternativas razonables, debe explicarse antes de escoger una.

En particular, no decidir automáticamente:

- si la colección interna debe comenzar como lista o diccionario cuando ambas alternativas sean razonables;
- qué debe ocurrir cuando se intenta agregar un servidor duplicado;
- qué criterio define exactamente un duplicado;
- qué debe ocurrir cuando se busca un servidor inexistente;
- qué debe ocurrir cuando se intenta eliminar un servidor inexistente;
- si determinados métodos deben retornar objetos, booleanos u otro resultado cuando existan varias opciones razonables.

Estas decisiones se tomarán durante el desarrollo, no anticipadamente.

---

## Compatibilidad con las fases anteriores

La Fase 4 no debe romper ni reemplazar el comportamiento conseguido anteriormente.

Debe continuar funcionando:

- creación independiente de objetos `Server`;
- estado inicial `DOWN`;
- `mark_up()`;
- `mark_down()`;
- `toggle_status()`;
- `is_up()`;
- métricas independientes por servidor;
- `update_metrics()`;
- validación de métricas;
- `simulate_metrics()`;
- `get_info()`;
- `__str__()`.

No modificar retroactivamente `Server` salvo que aparezca una razón concreta y justificada.

---

## Fuera del alcance

Durante esta fase NO implementar:

- estados de salud como `HEALTHY`, `WARNING` o `CRITICAL`;
- thresholds;
- alertas;
- historial de métricas;
- timestamps;
- persistencia;
- archivos;
- JSON;
- base de datos;
- archivos de configuración;
- logging;
- interfaz CLI;
- interfaz gráfica;
- API;
- métricas reales del sistema operativo;
- conexiones de red;
- monitoreo remoto;
- concurrencia;
- threads;
- multiprocessing;
- `asyncio`;
- nuevas clases adicionales sin necesidad clara;
- librerías externas.

La Fase 4 debe permanecer enfocada en administrar objetos `Server` en memoria.

---

## Pruebas durante esta fase

Las pruebas no serán el objetivo principal de la Fase 4.

El asistente diseñará comprobaciones pequeñas cuando sean necesarias para verificar que la lógica escrita funciona antes de avanzar.

El usuario no tendrá que desarrollar una suite de testing ni archivos de pruebas.

Cuando sea necesario utilizar temporalmente `main.py`, el asistente proporcionará el contenido completo del archivo.

Después de verificar un comportamiento, se continuará con nueva lógica.

---

## Criterios de finalización

La Fase 4 estará completa cuando ServerWatch pueda administrar correctamente múltiples objetos `Server` y realizar las operaciones de gestión definidas durante el desarrollo.

Como mínimo, al finalizar deberá ser posible:

- crear un `ServerManager`;
- agregar servidores;
- mantener varios servidores independientes;
- consultar la colección;
- buscar servidores;
- impedir o manejar correctamente duplicados según la política elegida;
- eliminar servidores;
- obtener servidores `UP`;
- obtener servidores `DOWN`;
- preservar completamente las métricas y estados individuales de cada objeto;
- mantener intacto el comportamiento conseguido en las Fases 1, 2 y 3.

---

## Metodología obligatoria

La fase se desarrollará con la misma metodología utilizada anteriormente:

1. Trabajar una sola fase a la vez.
2. Dentro de la fase, trabajar un solo paso a la vez.
3. El usuario escribe todo el código de implementación.
4. No proporcionar código de solución inicialmente.
5. Explicar en palabras qué debe implementarse, su comportamiento, restricciones y casos importantes.
6. El usuario pega su implementación después de cada paso.
7. Revisar la implementación antes de avanzar.
8. Si está correcta, proporcionar únicamente el siguiente paso.
9. Si contiene errores, explicar el problema y permitir que el usuario lo corrija.
10. No avanzar mientras el paso actual no esté correcto.
11. Si el usuario se atasca, proporcionar pistas progresivas antes de mostrar una solución.
12. No implementar anticipadamente funcionalidades de pasos posteriores.
13. No sobrearquitectar.
14. Consultar al usuario antes de resolver decisiones importantes de diseño con varias alternativas razonables.
15. Preservar siempre el comportamiento correcto conseguido anteriormente.
16. Las preguntas conceptuales se responden sin perder el punto exacto del desarrollo.
17. El asistente diseña las pruebas; el usuario se concentra en la lógica.
18. Si se necesita código temporal en `main.py`, el asistente proporciona el archivo completo.
19. Cuando se introduzca algo nuevo, indicar explícitamente el nombre del archivo, clase, método, atributo o función correspondiente, salvo que elegir el nombre sea parte del ejercicio.

---

## Resultado esperado

Al terminar esta fase, ServerWatch habrá pasado de representar servidores aislados a disponer de una primera capa real de administración de múltiples servidores.

La lógica seguirá siendo sencilla y completamente en memoria, pero proporcionará la base para fases posteriores donde el sistema podrá interpretar métricas, monitorear conjuntos de servidores y añadir funcionalidades más avanzadas de forma progresiva.
