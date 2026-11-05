---
title: 'Súbelo · Edición Claude'
---

# Súbelo

Prepara y comprueba tu siguiente entrega. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Antes de instalar

La edición principal necesita **Claude Code**, no solo una conversación en claude.ai. Debes tenerlo instalado, autenticado y con acceso a la carpeta del proyecto. Las herramientas del proyecto y las CLIs de alojamiento se obtienen aparte cuando hagan falta. No hay credenciales ni cuentas incluidas.

Se conserva el flujo original de Claude y su resolución de recursos. En Súbelo, el original principal declara macOS/Linux y WSL2 para Windows. Un paquete que se puede descomprimir en Windows no demuestra que todos sus comandos POSIX funcionen en PowerShell.

## Instalar desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/subelo) contiene el catálogo y las dos ediciones. Dentro de una sesión de Claude Code:

```text
/plugin marketplace add Alanmezaoficial/subelo
/plugin install subelo@alanmeza-subelo
/plugin list
```

El nombre después de `@` corresponde al catálogo de este repositorio, distinto en cada skill. Instalarlo registra el plugin en tu entorno; comprueba después el comando indicado abajo y ejecuta un encargo pequeño. La publicación del repositorio no sustituye esa prueba del host.

## Prueba el plugin local

Descomprime el repositorio preparado y abre una terminal en su raíz. Para cargar el plugin solo durante esa sesión:

```text
claude --plugin-dir ./claude
```

Para registrarlo mediante su catálogo local:

```text
claude plugin validate .
claude plugin validate ./claude
claude plugin marketplace add .
claude plugin install subelo@alanmeza-subelo
claude plugin list
```

Los comandos de catálogo cambian la configuración local de Claude; ejecútalos cuando quieras instalar. No utilizan un repositorio público. Si descargaste solo el ZIP Claude, descomprímelo y usa `claude --plugin-dir` con su carpeta superior: el catálogo está en el repositorio completo.

## Comprueba qué se cargó

Abre el menú de skills/comandos y busca `/subelo:subelo`. El prefijo es el nombre del plugin. Si copias solo el `SKILL.md`, faltarán sus referencias; conserva la carpeta completa. No mezcles la instalación como plugin con una copia parcial en `~/.claude/skills`.

Validar el manifiesto, instalarlo y ejecutar un encargo son tres pasos diferentes. Los JSON/YAML y recursos de esta edición se revisan localmente; la instalación y el flujo conversacional en Claude Code o Cowork no se presentan como probados si no se abrió ese host.

## Empieza por el destino más cercano

Antes de publicar, comprueba que la entrega funciona en el entorno que sí tienes. Puedes encargar solo el inicio local:

```text
/subelo:subelo Inicia y comprueba este proyecto solo en localhost. Revisa la ruta principal y sus recursos y entrega la URL local.
```

Para un preview externo, indica el proveedor o deja que recomiende uno compatible con tu proyecto y sus requisitos. Tener una cuenta conectada no prueba que exista acceso al proyecto correcto.

## Los recorridos reales

El original distingue inicio local y despliegue en nube. Dentro del segundo detecta una aplicación con runtime o un sitio estático. Preview y producción son etapas del despliegue, no skills nuevas.

Súbelo detecta el stack, realiza comprobaciones previas, elige una ruta compatible y verifica la salida. Tiene referencias para Vercel, Railway, Docker/VPS, túneles y cuatro destinos de sitios estáticos. Codex conserva además el enrutamiento a Sites si está disponible y el proyecto ya lo utiliza. La lista no promete planes gratuitos ni prueba acceso a esos servicios.

```text
/subelo:subelo Revisa esta entrega y prepara un preview en el proyecto de alojamiento que ya tengo configurado. Detente antes de producción y muestra las comprobaciones realizadas.
```

## Página estática o aplicación

Una carpeta de HTML/CSS/JS sin manifiesto puede usar el perfil estático. Un proyecto Astro con `package.json` conserva el pipeline de aplicación durante preparación; cuando construyas `dist/`, puedes revisar esa salida como sitio estático explícitamente.

Los helpers incluidos permiten comprobar los argumentos antes de usarlos:

```text
python scripts/audit.py --help
python scripts/static_check.py --help
python scripts/env_extract.py --help
```

Desde la carpeta instalada de la skill, un ejemplo sobre una salida ya construida es:

```text
python scripts/audit.py "ruta al proyecto" --profile static --publish-dir dist --json
```

El checker busca entrada, rutas, diferencias de mayúsculas, archivos faltantes, secretos en el contenido publicable y otros problemas de la carpeta. El host puede resolver URLs de forma distinta: abre también la página servida. Una comprobación de archivos no reemplaza HTTP y navegador.

## Qué información necesita

La ruta del proyecto, comando de build/inicio, destino existente, carpeta publicable y variables requeridas por **nombre**. Si falta autenticación o una herramienta externa, debe explicarlo. Nunca pegues valores secretos en el chat, logs, capturas ni comandos de ejemplo.

Una variable que el build incrusta en el JavaScript del navegador es pública. Un repositorio privado no convierte ese bundle en un almacén secreto. Si la función necesita una credencial privada, requiere una parte de servidor adecuada; no basta cambiar el nombre de la variable.

## Confirmación: diferencia importante entre ediciones

**Codex:** conserva el contrato de la adaptación instalada. Puede automatizar preparación y preview; producción requiere revisión del preview concreto y autorización posterior sobre la misma fuente y destino. «Auto» no elimina esa puerta.

**Claude:** conserva `ask_at_start`, `full_auto` y `always_ask` del original. `full_auto` puede promover a producción después de su ventana ESC de cinco segundos; úsalo solo si has elegido y autorizado ese comportamiento. Para revisar con calma, pide «paso a paso». `VISUAL_VERIFY` activa la comprobación visual cuando su herramienta está disponible; `ALLOW_DIRTY_TREE` afecta el bloqueo por cambios sin commit, no sustituye la identificación de la fuente que vas a publicar.

Si el proveedor publica directamente, por ejemplo una subida estática sin entorno de preview separado, primero debe revisarse localmente el mismo directorio que se subirá. El resultado debe explicar esa diferencia antes de la acción pública.

## Súbelo para páginas web: variante Cowork

El paquete adicional `subelo-web.plugin` está dirigido a Cowork y páginas estáticas. Conserva su checker y dos referencias. Si el host no tiene terminal, el flujo puede guiar una revisión por archivos y la publicación por navegador; no debe presentar esa revisión manual como ejecución del script.

Importa el archivo en la sección de plugins del host compatible. Esta importación no se ha probado aquí en Cowork. Para desarrollo en Claude Code puedes cargar `claude/cowork-plugin` con `--plugin-dir` y usar `/subelo-web:subelo-web`. No copies el plugin Cowork en Codex: su recorrido estático está integrado en `$subelo`.

## Qué entrega y cómo recuperarte

Una entrega útil identifica la fuente, los checks realmente realizados, URL del entorno correspondiente, recursos/rutas comprobados y recuperación disponible. Si se inició solo localmente, la URL no funciona en el iPhone por internet ni persiste como publicación en nube.

Si hay un error de build, conserva el fallo y corrige su causa. Si hay HTTP 200 pero faltan estilos, revisa rutas, mayúsculas y carpeta publicable. Si falla la promoción, no repitas despliegues ni ejecutes un rollback destructivo sin identificar una versión anterior y la autorización aplicable. Tener instrucciones de recuperación no significa que exista rollback automático en todos los proveedores.

## Mantener esta edición

Antes de actualizar guarda una copia de tu carpeta instalada y de cualquier cambio propio. Revisa `upstream.lock.json`, `CHANGELOG.md` y `docs/actualizar-desde-original.md` en el repositorio preparado. Compara la siguiente revisión en otra carpeta; no uses un reemplazo completo para integrar cambios pequeños.

Actualiza solo la edición que utilizas. Comprueba referencias y extracción, vuelve a instalar en un destino aislado y después ejecuta un encargo representativo. Las actualizaciones de estas skills y las versiones del proyecto que estás construyendo son trabajos distintos.

## Autoría y comprobaciones

Adaptación y documentación de **Alanmeza.ai**, sobre los proyectos originales de **Enrique Rocha / Hainrixz** y, en Chécalo, **Cyber Neo Contributors**. Se conservan MIT, `LICENSE`, `NOTICE` y los avisos de procedencia. Consulta el registro de validación de esta edición para distinguir scripts probados, copia instalada y host conversacional pendiente.
