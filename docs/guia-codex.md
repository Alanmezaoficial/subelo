---
title: 'Súbelo · Edición Codex'
---

# Súbelo

Prepara y comprueba tu siguiente entrega. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Antes de instalar

Necesitas Codex con acceso al sistema de archivos del equipo y una carpeta de trabajo. La biblioteca está en el apartado ChatGPT, pero este paquete está preparado para Codex: descargarlo desde un teléfono no lo instala en tu computadora ni lo habilita en todas las modalidades de ChatGPT.

La skill utiliza las herramientas que estén disponibles en esa sesión. Python es necesario para los helpers incluidos; las tareas del proyecto pueden necesitar Node, Git u otro runtime. No se necesita una clave de API para leer estas instrucciones ni se incluye ninguna.

## Obtener desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/subelo) incluye ambas ediciones. Si tienes Git, puedes obtenerlo en una carpeta nueva:

```text
git clone https://github.com/Alanmezaoficial/subelo.git
cd subelo
```

También puedes descargar el ZIP desde **Code → Download ZIP** en GitHub. Antes de copiar, abre la raíz que contiene `claude/` y `codex/`.

## Instala una copia con nombre propio

Descomprime el repositorio preparado. Abre PowerShell en su raíz, donde están `claude/` y `codex/`. Este comando copia únicamente la skill nueva y se detiene si ya existe ese destino:

```powershell
$source = (Resolve-Path '.\codex\skills\subelo').Path
$destination = Join-Path $env:USERPROFILE '.agents\skills\subelo'
if (Test-Path -LiteralPath $destination) { throw 'El destino ya existe; revisa su versión antes de actualizar.' }
New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

Si descargaste el ZIP de la edición Codex en lugar del repositorio completo, su carpeta superior ya se llama `subelo`: copia esa carpeta completa a `.agents/skills` de tu usuario. Deben quedar `SKILL.md`, sus recursos y `agents/openai.yaml` dentro de ella. Conserva `LICENSE` y `NOTICE`. Las instalaciones anteriores con otros nombres pueden seguir presentes.

## Verifica antes de encargar trabajo

Comprueba que existe `$env:USERPROFILE\.agents\skills\subelo\SKILL.md`. Inicia una sesión nueva de Codex y selecciona la skill; en CLI/extensión puedes escribir `$subelo` o abrir `/skills`. Si no aparece, reinicia el host y revisa la carpeta: no debe haber un nivel adicional `subelo/subelo`.

La presencia del archivo comprueba la copia; verla en el selector comprueba descubrimiento; completar un encargo comprueba ese recorrido. Son verificaciones distintas. Nuestro registro separa extracción/copia verificadas de la activación en una sesión nueva, que queda pendiente si el host no se probó.

## Empieza por el destino más cercano

Antes de publicar, comprueba que la entrega funciona en el entorno que sí tienes. Puedes encargar solo el inicio local:

```text
$subelo Inicia y comprueba este proyecto solo en localhost. Revisa la ruta principal y sus recursos y entrega la URL local.
```

Para un preview externo, indica el proveedor o deja que recomiende uno compatible con tu proyecto y sus requisitos. Tener una cuenta conectada no prueba que exista acceso al proyecto correcto.

## Los recorridos reales

El original distingue inicio local y despliegue en nube. Dentro del segundo detecta una aplicación con runtime o un sitio estático. Preview y producción son etapas del despliegue, no skills nuevas.

Súbelo detecta el stack, realiza comprobaciones previas, elige una ruta compatible y verifica la salida. Tiene referencias para Vercel, Railway, Docker/VPS, túneles y cuatro destinos de sitios estáticos. Codex conserva además el enrutamiento a Sites si está disponible y el proyecto ya lo utiliza. La lista no promete planes gratuitos ni prueba acceso a esos servicios.

```text
$subelo Revisa esta entrega y prepara un preview en el proyecto de alojamiento que ya tengo configurado. Detente antes de producción y muestra las comprobaciones realizadas.
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
