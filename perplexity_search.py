"""
Perplexity AI Deep Search CLI
Context tasarrufu icin harici arama scripti.
"""
import os
import sys
import argparse
import requests
from datetime import datetime
from pathlib import Path

# .env destegi (opsiyonel)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Sabitler
API_URL = "https://api.perplexity.ai/chat/completions"
MODELS = {
    "sonar": "sonar",
    "sonar-pro": "sonar-pro",
    "reasoning": "sonar-reasoning-pro"
}
DEFAULT_MODEL = "sonar-pro"


def get_api_key():
    """API anahtarini ortam degiskeninden alir."""
    key = os.getenv("PERPLEXITY_API_KEY")
    if not key:
        print("HATA: PERPLEXITY_API_KEY ortam degiskeni bulunamadi.")
        print("Windows'ta: setx PERPLEXITY_API_KEY \"pplx-xxx\"")
        sys.exit(1)
    return key


def search(query: str, model: str = DEFAULT_MODEL) -> dict:
    """Perplexity API'ye sorgu gonderir."""
    headers = {
        "Authorization": f"Bearer {get_api_key()}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODELS.get(model, model),
        "messages": [
            {
                "role": "system",
                "content": "Arastirma asistanisin. Konuyu derinlemesine arastir, "
                          "kaynaklari tara. Markdown formatinda, basliklar ve "
                          "maddeler iceren kapsamli bir rapor hazirla."
            },
            {"role": "user", "content": query}
        ],
        "temperature": 0.1
    }

    print(f"Araniyor: {query}")
    print(f"Model: {model}")

    response = requests.post(API_URL, json=payload, headers=headers, timeout=120)
    response.raise_for_status()

    data = response.json()
    return {
        "content": data["choices"][0]["message"]["content"],
        "citations": data.get("citations", []),
        "model": model
    }


def save_markdown(query: str, result: dict, output_dir: Path) -> Path:
    """Sonucu Markdown dosyasina kaydeder."""
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() else "_" for c in query)[:30]
    filename = f"{timestamp}_{safe_name}.md"
    filepath = output_dir / filename

    lines = [
        f"# {query}",
        "",
        f"**Tarih:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Model:** {result['model']}",
        "",
        "---",
        "",
        result["content"]
    ]

    if result["citations"]:
        lines.extend(["", "## Kaynaklar", ""])
        for i, url in enumerate(result["citations"], 1):
            lines.append(f"{i}. {url}")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Perplexity AI ile arama yap, sonucu Markdown olarak kaydet."
    )
    parser.add_argument("query", help="Arama sorgusu")
    parser.add_argument(
        "-m", "--model",
        choices=list(MODELS.keys()),
        default=DEFAULT_MODEL,
        help=f"Model secimi (varsayilan: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path(__file__).parent / "output",
        help="Cikti klasoru (varsayilan: ./output)"
    )

    args = parser.parse_args()

    try:
        result = search(args.query, args.model)
        filepath = save_markdown(args.query, result, args.output)
        print(f"Kaydedildi: {filepath}")
        print(f"Icerik boyutu: {len(result['content'])} karakter")
    except requests.exceptions.RequestException as e:
        print(f"API Hatasi: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nIptal edildi.")
        sys.exit(0)


if __name__ == "__main__":
    main()
