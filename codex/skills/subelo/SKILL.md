---
name: subelo
description: Prepara, publica y verifica una web, API, agente o servicio usando un flujo local o auditado de preview a producción. Detecta el stack, ejecuta preflight, elige entre Sites, Vercel, Railway, Docker/SSH, hosts estáticos o túnel temporal, entrega variables sin exponer secretos y valida HTTP/rutas. Úsala cuando el usuario pida ejecutar localmente, crear una URL de preview, desplegar, publicar o promover a producción. No la uses para publicar paquetes npm/PyPI ni para tocar producción sin autorización explícita posterior al preview.
---

# Súbelo para Codex

Detecta, audita, enruta y despliega con evidencia separada para cada etapa. Esta adaptación conserva el proyecto MIT de Hainrixz; consulta [LICENSE](LICENSE).

## Regla principal

Producción nunca es implícita. Las frases `auto`, `full auto` o similares pueden automatizar preflight y preview, pero no autorizan producción. Después de validar el preview, muestra URL, comando/acción exacta, destino, DNS, variables y posibles costos; solicita una autorización explícita para promover esa versión concreta.

## Modos

- **Local:** inicia el proyecto y verifica el endpoint local. No abre túnel salvo petición expresa.
- **Preview:** despliega una versión temporal o staging y la verifica. Es el modo por defecto de cualquier petición de deploy ambigua.
- **Producción:** solo después de un preview verde de la misma fuente y autorización explícita.

## Contrato de seguridad

1. No suavices checks fallidos ni presentes una comprobación omitida como aprobada.
2. No publiques producción sin preview 2xx/3xx y revisión explícita del usuario.
3. No imprimas, registres ni subas secretos. Informa nombres de variables, nunca valores.
4. No instales ni autentiques CLIs de terceros automáticamente. Explica el requisito y espera si necesita intervención del usuario.
5. No modifiques código para superar el preflight sin mostrar el diff y obtener autorización.
6. No reescribas historial Git, fuerces pushes ni elimines despliegues.
7. Respeta configuración existente: `.openai/hosting.json`, `.vercel/project.json`, `railway.toml`, `Dockerfile`, DNS y pipelines.
8. Separa claramente estas pruebas: build/lint, typecheck, HTTP local, navegador, Git push, preview, producción y rutas/DNS.
9. Un rollback solo se ejecuta contra una versión anterior identificada y con autorización, salvo que el proveedor ofrezca una transacción automática ya configurada por el usuario.

## Fase 0: alcance y estado

Resuelve la raíz del proyecto, revisa instrucciones `AGENTS.md`, estado Git y cambios del usuario. No exijas un árbol limpio para preview local; para producción, identifica exactamente la fuente que se publicará y evita mezclar cambios ajenos.

Si existe un reporte reciente de `$checalo`, léelo. Para producción de una app nueva o de un cambio sustancial, bloquea hasta que no queden hallazgos Critical/High sin una aceptación de riesgo explícita.

## Fase 1: detección

Lee [references/project-types.md](references/project-types.md) y detecta manifiestos, framework, package manager, runtime, comando de build/start, puerto, variables, bases de datos, monorepo y configuración de despliegue existente.

- Si es monorepo, pregunta qué paquete publicar.
- Si es una librería/CLI sin servicio web, detente: esta skill no publica npm/PyPI.
- En Windows usa los ejecutables disponibles (`.cmd`, PowerShell o runtime empaquetado); no obligues a usar WSL si el flujo nativo funciona.

## Fase 2: preflight

Ejecuta [scripts/audit.py](scripts/audit.py) con el intérprete Python disponible y consulta [references/audit-checklist.md](references/audit-checklist.md). Valida, según el modo:

- secretos rastreados y cobertura de `.gitignore`;
- lockfile coherente;
- variables requeridas frente a `.env.example`;
- build/start y binding de puerto;
- dependencias graves cuando la herramienta esté disponible;
- estado y origen Git que corresponden a la fuente a desplegar.

Si el script no soporta una plataforma o check, reproduce esa comprobación con herramientas nativas y registra la sustitución. Un fallo bloquea; propone el arreglo, pero no lo aplica sin permiso.

## Fase 3: destino

Recomienda un destino y da una razón. Carga solo su referencia:

- Si existe `.openai/hosting.json` o el proyecto usa Sites: usa la skill de Sites y su conector disponibles en la sesión; reutiliza el `project_id`, nunca crees otro para el mismo sitio.
- Next/Vite/Astro/SPA: [Vercel](references/targets/vercel.md) si no hay configuración de Sites.
- FastAPI/Flask/Express/worker HTTP: [Railway](references/targets/railway.md).
- Docker, estado persistente o VPS propio: [Docker + SSH](references/targets/docker-vps.md).
- Demo temporal desde local: [cloudflared](references/targets/cloudflared-tunnel.md).
- HTML o salida estática: consulta [sitios estáticos](references/static-sites.md) y las referencias de [Cloudflare Pages](references/targets/cloudflare-pages.md), [Netlify](references/targets/netlify.md), [GitHub Pages](references/targets/github-pages.md) o [Render](references/targets/render.md) según el destino elegido. Verifica sus condiciones actuales, no asumas gratuidad ni capacidades por esta lista.
- Para agentes, lee además [references/agents.md](references/agents.md).

No cambies de proveedor si ya existe una vinculación funcional, salvo petición explícita.

## Fase 4: preview

Verifica que el conector o CLI esté disponible y autenticado. Si no, detente con instrucciones exactas; inicio de sesión, CAPTCHA y aprobación de costos pertenecen al usuario.

Entrega variables requeridas según [references/env-mapping.md](references/env-mapping.md) sin mostrar valores. Despliega la misma fuente identificada en Fase 0, captura la URL y verifica:

1. HTTP con redirecciones; 2xx/3xx es requisito mínimo.
2. Endpoint de salud o ruta principal.
3. Para frontend, visibilidad real en navegador cuando esté disponible: sin pantalla en blanco ni error de runtime.
4. Rutas y assets críticos, no solo `/`.

Mantén el preview disponible para revisión cuando el entorno lo permita. Si falla, entrega logs y conserva producción intacta.

## Fase 5: puerta de producción

Presenta un resumen compacto:

- URL de preview y verificaciones realizadas;
- commit/fuente exacta;
- proveedor/proyecto y URL o dominio de producción;
- acción exacta de promoción;
- variables que se configurarán por nombre;
- impacto DNS y costos conocidos, verificados actualmente.

Pregunta si autoriza promover ese preview a ese destino. Una respuesta anterior a la creación del preview no cuenta. Cualquier `espera`, `alto`, `todavía no` o equivalente cancela la promoción.

## Fase 6: producción y verificación

Tras la autorización:

1. Promueve o despliega la fuente aprobada.
2. Verifica URL canónica, HTTP, redirección `www` si existe, endpoint de salud, rutas y assets clave.
3. Confirma por nombre que las variables remotas requeridas existen.
4. Entrega logs y rollback documentado, sin ejecutarlo.
5. Si la verificación falla, detente y solicita autorización antes de un rollback o una nueva promoción.

La entrega final debe distinguir qué quedó comprobado y qué quedó pendiente; un estado `READY` del proveedor no sustituye la verificación de la URL pública.

## Perfil estático

El helper admite --profile auto/app/static, --publish-dir y --target además de sus opciones previas. Un proyecto Astro/Next con manifiesto sigue el pipeline app; para auditar su salida construida usa explícitamente --profile static --publish-dir dist. En un directorio HTML sin manifiesto detecta static. Usa --scoped para revisión local limitada y declara lo omitido. El checker lee archivos, no certifica publicación. Comprueba también la URL y los recursos servidos. En local utiliza 127.0.0.1 salvo petición de exposición; no trates ese binding como fallo de producción.

Los ejemplos heredados de las referencias no cambian este contrato: utiliza PowerShell/herramientas de sesión de Codex en Windows. No ejecutes Bash/Monitor ni interpretes un prefijo ! como sintaxis disponible aquí. Descubre Python; no impongas python3 ni WSL. La política automática del original Claude no se aplica a esta edición: producción siempre requiere autorización sobre el preview concreto.

## Compatibilidad del ejecutor

Esta edición dirige a Codex con las herramientas expuestas en la sesión. Los nombres de capacidades heredados en ejemplos no registran APIs ni permisos de Claude. Para datos de OpenAI consulta OpenAI Docs; para Anthropic u otro proveedor consulta sus fuentes oficiales, sin cambiar el proveedor elegido por el proyecto. La documentación técnica con fecha es una caché histórica: verifica los datos cambiantes antes de usarlos.
