---
name: vigia-de-tesis
description: Revisa una tesis de inversión guardada (por defecto "tokens-ia") contra datos vivos de Profeta, precios de Yahoo Finance y apuestas de Polymarket; compara con el último registro, dice qué señales tempranas se movieron y deja un registro nuevo en el repositorio de GitHub. Úsala cuando el usuario diga "vigía", "revisa la tesis", "¿cómo va la tesis de tokens?" o /vigia.
---

# Vigía de tesis

Convierte una tesis (una idea sobre hacia dónde va el mundo) en una revisión periódica,
con datos, que no arranca de cero cada vez: siempre se compara con el registro anterior.

No es asesoría financiera. Describe lo que el precio descuenta y qué señales se mueven;
la decisión y la gestión del riesgo son del usuario.

## 0. Qué tesis

- Si el usuario no nombra otra, la tesis es `tokens-ia`.
- Cada tesis vive en `tesis/<nombre>/` con tres archivos: `tesis.md` (la idea y los
  escenarios), `senales.md` (qué vigilar y con qué umbral) y `watchlist.json` (tickers por grupo).
- Si el usuario trae una tesis nueva, primero ayúdale a escribir esos tres archivos
  (mira `references/tesis-tokens-ia.md` como modelo) y trata la primera revisión como
  "foto de partida".

## 1. Leer el último registro

Busca el archivo más reciente en `historial/<tesis>/` (nombres `AAAA-MM-DD.json`).
- En Claude Code: léelo del repositorio local (haz `git pull` antes).
- En claude.ai: pídele al usuario que adjunte el último `.json` de su repositorio, o que
  conecte el repositorio de GitHub al proyecto. Si no hay ninguno, es una foto de partida.
- Lee también `mi-cartera.md` si existe. Si no, pregunta en una sola línea qué posiciones
  tiene relacionadas con la tesis (puede responder "ninguna").

## 2. Datos fundamentales (MCP de Profeta)

Para cada ticker de `watchlist.json`:
- `expectativas` (uno por ticker): crecimiento que descuenta el precio, consenso,
  histórico, tasa base y veredicto.
- `ficha` (hasta 5 tickers por llamada): ROIC, WACC, margen operativo, PER,
  rentabilidad por flujo de caja (FCF yield), deuda/patrimonio.
- `insiders` solo para el grupo de "SaaS castigado" y "Servicios": compras en
  mercado abierto de los últimos 90 días.

Reglas: copia las cifras tal cual; si Profeta dice "base no usable" o "sin referencia",
dilo y no fuerces conclusión. Separa siempre "Profeta dice" de "lectura de Claude".

## 3. Datos de mercado

- Precios y variación desde el último registro: Yahoo Finance.
  En Claude Code ejecuta `python scripts/mercado.py precios tesis/<tesis>/watchlist.json`.
  En claude.ai usa búsqueda web ("<ticker> stock price") solo para los que cambien la lectura.
- Probabilidades de Polymarket para los mercados listados en `senales.md`
  (recesión en EE. UU., recortes de tasas, mercados sobre IA).
  En Claude Code: `python scripts/mercado.py polymarket "<búsqueda>"`.
  En claude.ai: búsqueda web en polymarket.com.
- Si una fuente no responde, dilo en el informe y sigue con el resto.

## 4. Evaluar señales

Recorre `senales.md` una por una y marca cada señal como:
`sin cambio` · `hacia A` · `hacia B` · `hacia C` · `sin dato`.
Compara contra el registro anterior: lo que importa es el movimiento, no el nivel.
Un cambio de veredicto en Profeta (p. ej. de "posible_valor" a "en_linea") o un
movimiento de más de 3 puntos en el crecimiento implícito cuenta como cambio.

## 5. Informe (en la respuesta)

En este orden, corto:
1. Una frase: ¿se movió algo desde el último registro? (fecha del anterior).
2. Tabla "Qué cambió": ticker, precio antes → ahora, crecimiento implícito antes → ahora,
   veredicto antes → ahora. Solo filas con cambios; si no hay, dilo.
3. Tabla de señales con su estado.
4. Marcador de escenarios: cuántas señales apuntan a A, B y C.
5. Cartera: qué posiciones del usuario quedan expuestas si gana cada escenario, y si
   tienen stop o regla de salida escrita. No recomiendes comprar ni vender.
6. Qué vigilar hasta la próxima revisión.
Cierra con: "Cifras de Profeta, Yahoo Finance y Polymarket a la fecha; no es recomendación de inversión."

## 6. Guardar el registro

Escribe `historial/<tesis>/<AAAA-MM-DD>.json` con la misma estructura que el registro
anterior (ver `references/formato-registro.md`) y un `<AAAA-MM-DD>.md` con el informe.
Incluye siempre: fecha y hora, cifras por ticker, estado de cada señal, marcador,
decisión del usuario (aunque sea "no hacer nada") y su razón.

- En Claude Code: `git add historial && git commit -m "vigia: <tesis> <fecha>" && git push`.
- En claude.ai: entrega los dos archivos para descargar y recuérdale subirlos a la
  carpeta `historial/<tesis>/` del repositorio (GitHub → Add file → Upload files).

Si el mismo día ya existe un registro, añade sufijo `-2`, `-3`.
