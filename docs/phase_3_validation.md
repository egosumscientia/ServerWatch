# Fase 3 — Validación de métricas

## Objetivo

Incorporar validación básica a las métricas de `Server` para impedir que el objeto acepte valores inválidos de CPU, memoria y disco.

Esta fase parte del sistema de métricas construido en la Fase 2 y debe preservar todo el comportamiento conseguido anteriormente.

---

## Estado inicial

Cada instancia de `Server` dispone actualmente de las métricas:

- `cpu_usage`
- `memory_usage`
- `disk_usage`

Las tres comienzan en `0`.

El método:

`update_metrics(cpu_usage, memory_usage, disk_usage)`

actualiza las tres métricas.

El método:

`simulate_metrics()`

genera valores enteros aleatorios entre `0` y `100` y utiliza `update_metrics()` para almacenarlos.

Las métricas representan porcentajes.

---

## Objetivo funcional

Las métricas deben mantenerse dentro del rango válido:

`0 <= valor <= 100`

Esto aplica a:

- CPU
- memoria
- disco

Durante esta fase se incorporarán progresivamente las reglas necesarias para evitar que `Server` quede con métricas inválidas.

---

## Alcance

La fase debe cubrir progresivamente:

1. Validación del rango permitido para las métricas.
2. Definición del comportamiento cuando una métrica está fuera del rango.
3. Validación del tipo de dato cuando corresponda.
4. Protección frente a actualizaciones parciales: si una actualización conjunta contiene algún valor inválido, el objeto no debe quedar parcialmente actualizado.
5. Comprobación de valores límite.
6. Comprobación de entradas inválidas.
7. Verificación de que `simulate_metrics()` continúa funcionando con las nuevas reglas.
8. Preservación del comportamiento conseguido en las Fases 1 y 2.

---

## Valores límite

Los valores:

- `0`
- `100`

deben considerarse válidos.

Los valores inferiores a `0` o superiores a `100` deben considerarse inválidos.

La política exacta para reaccionar ante valores inválidos se decidirá durante el desarrollo antes de implementarla.

---

## Restricciones de diseño

La validación introducida en esta fase estará limitada a las métricas.

No implementar todavía:

- validación de `hostname`;
- validación de `ip_address`;
- validación real de direcciones IP;
- estados de salud del servidor;
- `HEALTHY`;
- `WARNING`;
- `CRITICAL`;
- thresholds configurables;
- alertas;
- historial de métricas;
- timestamps;
- persistencia;
- JSON;
- archivos de configuración;
- logging;
- métricas reales de Linux;
- nuevas clases sin una necesidad clara.

No utilizar librerías externas para resolver la validación.

La implementación debe mantenerse sencilla y acorde con el alcance actual de ServerWatch.

---

## Compatibilidad con fases anteriores

La Fase 3 no debe romper el comportamiento existente.

Debe continuar funcionando:

- creación independiente de servidores;
- estado inicial `DOWN`;
- `mark_up()`;
- `mark_down()`;
- `toggle_status()`;
- `is_up()`;
- `get_info()`;
- `__str__()`;
- `update_metrics()`;
- `simulate_metrics()`.

Cada instancia debe continuar manteniendo independientemente su estado y sus métricas.

---

## Simulación

`simulate_metrics()` debe continuar generando métricas válidas.

La simulación debe respetar las mismas reglas de validación utilizadas por las actualizaciones normales y debe continuar reutilizando `update_metrics()`.

---

## Integridad de una actualización

Una llamada a `update_metrics()` representa una actualización conjunta de CPU, memoria y disco.

Al finalizar esta fase, una actualización inválida no debe dejar al objeto en un estado parcialmente actualizado.

Si alguno de los valores proporcionados invalida la actualización completa, las métricas anteriores deben conservarse.

La estrategia concreta para conseguir este comportamiento se decidirá durante la implementación.

---

## Fuera del alcance

Esta fase NO determina todavía si un servidor está funcionando bien o mal según sus métricas.

Por ejemplo, un uso de CPU de `95%` puede ser una métrica válida aunque posteriormente otra fase pueda considerarlo un estado problemático.

La Fase 3 responde únicamente a la pregunta:

**¿El dato recibido es válido como métrica?**

No responde todavía:

**¿La métrica indica que el servidor está saludable?**

---

## Criterios de finalización

La Fase 3 estará completa cuando:

- CPU, memoria y disco acepten únicamente los valores definidos como válidos;
- los límites `0` y `100` funcionen correctamente;
- los valores fuera del rango sean rechazados según la política elegida;
- los tipos de datos aceptados estén claramente definidos y comprobados;
- una actualización inválida no modifique parcialmente las métricas;
- `simulate_metrics()` siga funcionando;
- `get_info()` y `__str__()` continúen funcionando;
- el estado `UP`/`DOWN` siga siendo independiente de las métricas;
- las funcionalidades de las Fases 1 y 2 permanezcan intactas.

---

## Metodología de implementación

La fase se desarrollará incrementalmente.

Se implementará un solo paso a la vez.

Cada paso será revisado antes de continuar con el siguiente.

No se introducirán anticipadamente funcionalidades correspondientes a fases posteriores.