# Formato del registro (historial/<tesis>/AAAA-MM-DD.json)

```json
{
  "tesis": "tokens-ia",
  "fecha": "2026-10-13",
  "hora_local": "21:25 America/Bogota",
  "fuente": "MCP de Profeta (expectativas, ficha, insiders); Yahoo Finance; Polymarket",
  "tipo": "foto_de_partida | revision",
  "estado_tesis": "Observando / Se inclina a A / B / C",
  "empresas": [
    {"ticker": "ADBE", "grupo": "SaaS castigado", "precio": 236.28,
     "crec_implicito_pct": 1.92, "crec_consenso_pct": 7.3, "crec_historico_fcf_pct": 19.27,
     "tasa_base_pct": 77.08, "veredicto": "posible_valor",
     "roic_pct": 36.79, "wacc_pct": 10.75, "roic_menos_wacc_pp": 26.04,
     "margen_operativo_pct": 35.7, "per": 10.35, "fcf_yield_pct": 11.65, "deuda_patrimonio": 0.57}
  ],
  "insiders": {"CRM": {"compras_90d_usd": 999451, "nota": "..."}},
  "senales": [{"n": 1, "nombre": "Planes de suscripción", "estado": "hacia B", "evidencia": "..."}],
  "marcador": {"A": 0, "B": 1, "C": 0},
  "mi_cartera": [{"ticker": "...", "peso_pct": 0, "stop": "...", "escenario_que_la_daña": "..."}],
  "decision": "No hacer nada",
  "razon": "...",
  "proxima_revision": "semanal"
}
```

El campo `decision` es obligatorio aunque sea "no hacer nada": es lo que permite,
meses después, auditar si las decisiones fueron buenas (accountability).
