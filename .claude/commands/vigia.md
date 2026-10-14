---
description: Revisa una tesis de inversión con Profeta, Yahoo Finance y Polymarket y guarda el registro en GitHub
argument-hint: [nombre-de-tesis]
---
Usa la skill vigia-de-tesis sobre la tesis "$ARGUMENTS" (si está vacío, "tokens-ia").

Antes de empezar: `git pull`.
Pasos: lee el último registro de historial/, consulta Profeta por MCP, ejecuta
`python scripts/mercado.py precios tesis/<tesis>/watchlist.json` y
`python scripts/mercado.py polymarket "recession"`, evalúa senales.md, escribe el
informe, guarda historial/<tesis>/<fecha>.json y .md, ejecuta
`python scripts/mercado.py comparar historial/<tesis>` para verificar el diff,
y haz commit + push con el mensaje "vigia: <tesis> <fecha>".
Antes del commit, pregúntame qué decisión tomo (puede ser "no hacer nada") y por qué.
