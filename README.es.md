# Artificer

**v0.4 (alpha)** · [Read in English](README.md)

Un framework para programar con IA sin perder el control del código. Nunca vibecoding.

En los mundos de fantasía, el artífice construye sus propias criaturas mecánicas y conoce cada pieza, así que nunca se vuelven contra él. Aquí la criatura es la IA: escribe rápido, y tú sigues siendo el arquitecto.

## Qué es, en corto
- **Para qué**: la IA escribe el código, pero tú decides qué se construye y cómo, entiendes cada cambio antes de aprobarlo y te mantienes afilado (o mejoras) mientras trabajas.
- **Cómo**: un ciclo por tarea, decisiones de diseño que siempre son tuyas, cuatro niveles de quién escribe el código y una capa de aprendizaje que mide lo que sabes de verdad.
- **Dónde**: dentro de tu agente de código preferido: Claude Code, Codex, GitHub Copilot (VS Code) u OpenCode.

## Cómo funciona
**1. Un ciclo por tarea**

| Paso | Comando | Tú |
|---|---|---|
| Intención y ejemplos (Dado/Cuando/Entonces = la spec) | `/artificer-spec` | los defines |
| Explorar, decisiones, mapa de cambios (tramos de 200 líneas como máximo) | `/artificer-map` | tomas cada decisión de diseño y apruebas el mapa |
| Construir, un tramo a la vez, tests primero | `/artificer-build` | escribes lo que diga tu nivel |
| Verificar y cerrar | `/artificer-verify` | revisas con un mapa de riesgo y apruebas el diff |

Cambios pequeños: `/artificer-quick`. Los documentos del proyecto (producto, principios, diseño, arquitectura) tienen sus propios comandos.

**2. Tus decisiones.** La IA plantea las decisiones de diseño (stack, estructura, patrones, datos, contratos) y nunca las responde. Opciones solo si las pides, con pros y contras y sin recomendación. Nada sin decidir se construye.

**3. Cuatro niveles: quién escribe el código**

| | off | assist | core | full |
|---|---|---|---|---|
| Quién escribe | la IA | la IA | tú escribes la lógica y las aserciones de los tests | tú escribes todo |
| Qué haces además de decidir y aprobar | revisar | predecir, explicar, responder preguntas sobre el código | | |

**4. Aprender mientras trabajas.** Explicaciones cortas dentro de las preguntas cuando un concepto parece nuevo para ti, lecturas guiadas del código que no conoces, repaso espaciado de tus errores, un codemap del código que conoces y una ficha de personaje honesta (`/artificer-stats`) donde los niveles solo suben superando pruebas.

**5. Git, siempre tuyo.** La IA solo propone rama, mensaje de commit y PR. Los ejecuta solo con tu orden expresa y nunca añade atribución a la IA.

## Instalación
Requiere Git y Python 3.

```bash
git clone https://github.com/MatOtS/artificer-ai.git
cd artificer-ai
python install.py
```

El instalador pregunta qué agentes de código usas e instala Artificer en cada uno. Para actualizar: `git pull` y otra vez `python install.py`. Para quitarlo: `python uninstall.py` (tus datos se conservan).

Después, en tu agente: `/artificer-onboard` (guía corta y tu perfil), y en un proyecto `/artificer-setup`.

## Tus datos y tus cambios
- **Datos** (perfil, ficha, progreso, codemaps): viven en `data/`, que git ignora. Para sincronizarlos entre PCs, ten tu propia copia privada de este repositorio y quita `data/` del `.gitignore`.
- **Personalizar** el tono, las reglas, los comandos o cualquier archivo: en `custom/` (ver [custom/README.md](custom/README.md)). Las actualizaciones nunca lo tocan. Editar `core/` también funciona, bajo tu responsabilidad al actualizar.

## Feedback
Abre un [issue](../../issues/new/choose): feedback de uso (qué funcionó, qué fue lento, dónde sentiste que perdías el control) o un bug.

## Hecho con IA
Artificer se construyó con un uso altísimo de IA: la mayor parte de su texto lo escribió un agente de código, en conversaciones largas donde el autor decidía qué construir y cómo. La misma idea que defiende el framework.

## Basado en
Desarrollo guiado por especificaciones y por comportamiento, desarrollo guiado por tests, revisiones pequeñas y enfocadas, e investigación sobre aprendizaje: Lead-and-Reveal (Kazemitabaar et al., IUI 2025), la ilusión de progreso en juniors que usan IA (Prather et al., ICER 2024), uso comprometido frente a uso ciego de la IA (Shen & Tamkin, 2026), recuperación espaciada y guía que se retira.

Más: el método en [core/skills/artificer/SKILL.md](core/skills/artificer/SKILL.md), los niveles en [core/skills/learn/learning-levels.md](core/skills/learn/learning-levels.md), ideas en [docs/BACKLOG.md](docs/BACKLOG.md) y el plan en [docs/ROADMAP.md](docs/ROADMAP.md) (en inglés).

## Licencia
[MIT](LICENSE) © Matias Otero Sarra
