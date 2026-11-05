---
title: 'Súbelo · Edición Claude'
---

# Súbelo

Prepara y comprueba tu siguiente entrega. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Empieza por aquí: tres formas de instalar

Elige solo una opción. La instalación conserva la herramienta completa con sus referencias y scripts. Esta edición principal es para Claude Code; la variante Cowork de Súbelo se explica más abajo.

### 1. Copia un prompt con los enlaces · recomendado

Copia el bloque completo, pégalo en un chat nuevo de Claude Code y deja que prepare la instalación. La guía enlazada es pública en GitHub: no necesita iniciar sesión en el Bunker.

```text
Instala para mi usuario la edición Claude Code de Súbelo como plugin completo.

Guía pública: https://github.com/Alanmezaoficial/subelo/blob/main/docs/guia-claude.md
Repositorio: https://github.com/Alanmezaoficial/subelo

Lee la guía. Si estás en Claude Code con acceso a mi equipo, registra el catálogo Alanmezaoficial/subelo e instala subelo@alanmeza-subelo con los comandos admitidos por mi versión. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva también los comandos, agentes y el manifiesto del plugin. Verifica la instalación con la lista de plugins e indica cómo comprobar su activación en una sesión nueva. No ejecutes la skill todavía. Si estás en una conversación sin acceso al equipo o el host no admite este plugin, explica qué necesito sin simular una instalación.
```

### 2. Descarga el ZIP y acompáñalo con este prompt

En la ficha de esta edición, pulsa Descargar ZIP. Adjunta el archivo a un chat de Claude Code o indica su ruta local si el host no admite ese adjunto; después pega el bloque. Descargar o adjuntar el archivo sin pedir la instalación no lo instala. Cada ZIP incluye INSTALAR.md con estas instrucciones.

```text
Instala para mi usuario la edición Claude Code de Súbelo del ZIP adjunto subelo-claude-1.0.1.zip, como plugin completo.

Guía pública de apoyo: https://github.com/Alanmezaoficial/subelo/blob/main/docs/guia-claude.md

Localiza el ZIP o pide su ruta local si no puedes acceder al adjunto. Extrae de forma segura la carpeta subelo en una ubicación persistente y lee INSTALAR.md. Esta carpeta incluye .claude-plugin/plugin.json y su catálogo local .claude-plugin/marketplace.json, cuyo source es ./; registra ese catálogo local e instala subelo@alanmeza-subelo. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva comandos, agentes y recursos del plugin. Valida y consulta la lista de plugins, informa de la ruta y de la comprobación pendiente en una sesión nueva. No ejecutes la skill todavía. Si el host no es compatible o no tiene acceso al equipo, indícalo sin afirmar que quedó instalada.
```

<details>
<summary>3. Prefiero instalar manualmente · Terminal · Claude Code</summary>

Con Claude Code instalado y autenticado, abre una terminal y pega estas tres líneas. El catálogo obtiene el plugin completo desde GitHub. No necesita pedirle trabajo a una IA.

```text
claude plugin marketplace add Alanmezaoficial/subelo
claude plugin install subelo@alanmeza-subelo
claude plugin list
```

</details>

### Confirma que quedó disponible

Consulta claude plugin list y abre una sesión nueva de Claude Code para comprobar los comandos del plugin. Si la carpeta existe pero no aparece en el selector, informa de ambas cosas; no son la misma prueba.

Las secciones siguientes explican requisitos y alternativas con más detalle.

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

Los comandos de catálogo cambian la configuración local de Claude; ejecútalos cuando quieras instalar. No utilizan un repositorio público. Si descargaste solo el ZIP Claude, descomprímelo y usa `claude --plugin-dir` con su carpeta superior: el ZIP ahora incluye también su propio catálogo local. Después de guardarlo en una ubicación persistente, puedes registrar esa carpeta con `claude plugin marketplace add RUTA_A_LA_CARPETA` e instalar el plugin por su nombre.

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
