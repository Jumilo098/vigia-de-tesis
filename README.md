# Vigía de tesis

Plantilla del Instituto Quant para vigilar tesis de inversión con Claude, el MCP de
Profeta, Yahoo Finance y Polymarket, dejando un historial en GitHub.

Guía completa, paso a paso: [`Guia_Vigia_de_Tesis.pdf`](Guia_Vigia_de_Tesis.pdf).

## Crea tu copia (un solo comando)

Con [GitHub CLI](https://cli.github.com) instalado y `gh auth login` hecho:

```bash
gh repo create vigia-de-tesis --template Jumilo098/vigia-de-tesis --private --clone
cd vigia-de-tesis
pip install -r requirements.txt
```

Eso crea **tu** repositorio privado a partir de esta plantilla y lo descarga a tu
computador. Hazlo privado: ahí vas a guardar decisiones sobre tu dinero.

Sin terminal: pulsa **Use this template → Create a new repository** arriba en esta
página y marca **Private**.

Si solo quieres mirar el contenido: `git clone https://github.com/Jumilo098/vigia-de-tesis.git`.

## Después de crear tu copia

1. Conecta Profeta a Claude Code con la URL que te da Profeta
   (Configuración → Conecta Profeta a tu IA):

   ```bash
   claude mcp add --transport http profeta "URL-QUE-TE-DIO-PROFETA"
   ```

2. Copia `mi-cartera.plantilla.md` como `mi-cartera.md` y llénala con tus posiciones.
   Git ignora `mi-cartera.md`: no se sube.

3. Abre Claude Code en la carpeta y escribe:

   ```
   /vigia tokens-ia
   ```

## En claude.ai (sin terminal)

Descarga `vigia-de-tesis-skill.zip` desde
[Releases](https://github.com/Jumilo098/vigia-de-tesis/releases/latest), súbelo sin
descomprimir en Personalizar → Skills y escribe «vigía» en un chat nuevo. La misma skill
está en la carpeta `skill/vigia-de-tesis`.

## Qué hay aquí

| Ruta | Qué es |
|------|--------|
| `tesis/tokens-ia/` | La idea, los tres escenarios, las 12 señales y los 29 tickers |
| `historial/tokens-ia/2026-10-13.json` | Foto de partida (registro #0) |
| `scripts/mercado.py` | Precios, Polymarket y comparación de registros |
| `.claude/` | El comando `/vigia` y la skill para Claude Code |
| `skill/vigia-de-tesis/` | La misma skill, para subir a claude.ai |
| `mi-cartera.plantilla.md` | Plantilla de tu cartera (tu copia llena queda fuera de git) |

Material educativo. No es recomendación de inversión.
