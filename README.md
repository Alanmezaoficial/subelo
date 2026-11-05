# Súbelo · Manos a la Obra

Prepara y comprueba tu siguiente entrega. Dos ediciones con el mismo nombre comercial: Claude y Codex.

Adaptación y documentación de Alanmeza.ai sobre el proyecto original. Consulta [autoría](ATTRIBUTION.md), [licencia](LICENSE) y [aviso original](NOTICE).

## Elige tu edición

- [Guía Codex](docs/guia-codex.md): parte de la adaptación instalada y conserva Windows, AGENTS.md y las herramientas disponibles.
- [Guía Claude](docs/guia-claude.md): conserva el flujo del original con nombres propios y sus requisitos reales.
- [Diferencias](docs/diferencias.md), [actualización](docs/actualizar-desde-original.md) y [validación](docs/validacion.md).

Para probar el plugin Claude desde esta raíz: `claude --plugin-dir ./claude`.
Para Codex copia la carpeta completa `codex/skills/subelo` a un destino de skills nuevo. Las guías incluyen PowerShell con protección contra sobrescritura.

Repositorio público: [Alanmezaoficial/subelo](https://github.com/Alanmezaoficial/subelo). Incluye ambas ediciones, sus guías y avisos de procedencia.

## Obtener desde GitHub

```text
git clone https://github.com/Alanmezaoficial/subelo.git
cd subelo
```

Para instalar el plugin en Claude Code:

```text
/plugin marketplace add Alanmezaoficial/subelo
/plugin install subelo@alanmeza-subelo
```

Para Codex, sigue la [guía de instalación](docs/guia-codex.md) y copia la carpeta completa indicada arriba. Los comandos públicos apuntan a este repositorio; su existencia no demuestra activación conversacional en el host.

## Contenido

`claude/` es la raíz del plugin. `codex/skills/subelo/` es autocontenido y `codex/.codex-plugin/plugin.json` permite empaquetar esa edición como plugin. `docs/` contiene guías propias y el registro de evidencia. `tests/` queda fuera del runtime instalado. Los avisos históricos de la base Codex están en `licenses/`.

## Versiones

Versión derivada: **1.0.0**. La revisión original se identifica por commit en `upstream.lock.json`; ese número no pretende ser la versión del creador.

## Desarrollo y pruebas

Usa un entorno Python aislado e instala requirements-dev.txt; después ejecuta python -m pytest tests --import-mode=importlib. Estas dependencias son de validación, no del sitio ni del runtime de la skill. La ejecución del host conversacional se verifica aparte.


