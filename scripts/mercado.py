"""Datos de mercado para la vigía de tesis.

Uso:
  python scripts/mercado.py precios tesis/tokens-ia/watchlist.json
  python scripts/mercado.py polymarket "recession"
  python scripts/mercado.py comparar historial/tokens-ia

Requiere: pip install yfinance requests
"""
import json
import sys
from pathlib import Path


def precios(watchlist_path):
    import yfinance as yf

    wl = json.loads(Path(watchlist_path).read_text(encoding="utf-8"))
    tickers = [t for grupo in wl["grupos"].values() for t in grupo]
    datos = yf.download(tickers, period="1y", auto_adjust=True, progress=False)["Close"]
    salida = {}
    for t in tickers:
        serie = datos[t].dropna() if t in datos else None
        if serie is None or serie.empty:
            salida[t] = {"error": "sin datos"}
            continue
        ultimo = float(serie.iloc[-1])
        salida[t] = {
            "precio": round(ultimo, 2),
            "var_1m_pct": round((ultimo / float(serie.iloc[-21]) - 1) * 100, 2) if len(serie) > 21 else None,
            "desde_max_52s_pct": round((ultimo / float(serie.max()) - 1) * 100, 2),
        }
    print(json.dumps(salida, ensure_ascii=False, indent=2))


def polymarket(busqueda):
    import requests

    r = requests.get(
        "https://gamma-api.polymarket.com/public-search",
        params={"q": busqueda, "limit_per_type": 10},
        timeout=20,
    )
    r.raise_for_status()
    salida = []
    for ev in r.json().get("events", []):
        for m in ev.get("markets", []):
            if m.get("closed"):
                continue
            precios_txt = m.get("outcomePrices") or "[]"
            try:
                precios_lista = json.loads(precios_txt)
            except (TypeError, ValueError):
                precios_lista = []
            salida.append({
                "pregunta": m.get("question"),
                "prob_si_pct": round(float(precios_lista[0]) * 100, 1) if precios_lista else None,
                "cierra": m.get("endDate"),
                "volumen_usd": m.get("volume"),
            })
    print(json.dumps(salida, ensure_ascii=False, indent=2))


def comparar(carpeta):
    """Diferencias entre los dos últimos registros JSON de una tesis."""
    archivos = sorted(Path(carpeta).glob("*.json"))
    if len(archivos) < 2:
        print("Solo hay un registro: esta es la foto de partida.")
        return
    antes, ahora = (json.loads(p.read_text(encoding="utf-8")) for p in archivos[-2:])
    previo = {e["ticker"]: e for e in antes["empresas"]}
    cambios = []
    for e in ahora["empresas"]:
        p = previo.get(e["ticker"])
        if not p:
            cambios.append({"ticker": e["ticker"], "nota": "nuevo en la lista"})
            continue
        gi0, gi1 = p.get("crec_implicito_pct"), e.get("crec_implicito_pct")
        salto = gi0 is not None and gi1 is not None and abs(gi1 - gi0) > 3
        if p.get("veredicto") != e.get("veredicto") or salto:
            cambios.append({
                "ticker": e["ticker"],
                "precio": [p.get("precio"), e.get("precio")],
                "crec_implicito_pct": [gi0, gi1],
                "veredicto": [p.get("veredicto"), e.get("veredicto")],
            })
    print(json.dumps({"desde": antes["fecha"], "hasta": ahora["fecha"], "cambios": cambios},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    {"precios": precios, "polymarket": polymarket, "comparar": comparar}[sys.argv[1]](sys.argv[2])
