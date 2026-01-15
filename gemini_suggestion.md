import requests
import json
import os
import sys
import argparse
from datetime import datetime

# Opsiyonel: .env dosyası desteği (pip install python-dotenv)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# -------------------------------------------------------------------------
# AYARLAR
# -------------------------------------------------------------------------

# API Anahtarını ortam değişkenlerinden (Environment Variables) alır.
API_KEY = os.getenv("PERPLEXITY_API_KEY")

if not API_KEY:
    print("❌ HATA: API Key bulunamadı!")
    print("Lütfen 'PERPLEXITY_API_KEY' adında bir Windows ortam değişkeni tanımlayın")
    print("veya projenizde .env dosyası varsa 'python-dotenv' kütüphanesini yükleyin.")
    sys.exit(1)

# Kullanılacak Model
# 'sonar-reasoning': Derinlemesine arama ve mantık (Deep Research muadili)
# 'sonar': Daha hızlı, daha kısa cevaplar.
MODEL_NAME = "sonar-reasoning" 

# -------------------------------------------------------------------------
# FONKSİYONLAR
# -------------------------------------------------------------------------

def search_perplexity(query):
    """
    Perplexity API'sine istek atar ve sonucu döndürür.
    """
    url = "https://api.perplexity.ai/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Sistem mesajı: Ekonomik/Sektörel analiz formatı
    system_prompt = (
        "Sen uzman bir araştırma asistanısın. "
        "Verilen konuyu derinlemesine araştır, akademik ve güncel sektörel kaynakları tara. "
        "Çıktıyı Markdown formatında; net başlıklar, madde işaretleri ve analizler içeren "
        "kapsamlı bir rapor olarak hazırla."
    )

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "temperature": 0.1, 
    }

    print(f"\n🔍 Perplexity'de aranıyor: '{query}'")
    print(f"🤖 Model: {MODEL_NAME} (Bu işlem konunun derinliğine göre 10-30sn sürebilir...)\n")
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        content = data['choices'][0]['message']['content']
        citations = data.get('citations', [])
        
        return content, citations
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API Hatası: {e}")
        return None, None

def save_to_markdown(query, content, citations):
    """
    Sonucu Markdown dosyasına kaydeder.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Dosya ismini temizle ve kısalt
    safe_query = "".join([c if c.isalnum() else "_" for c in query]).strip("_")[:40]
    filename = f"Rapor_{safe_query}_{timestamp}.md"
    
    full_text = f"# Araştırma Raporu: {query}\n\n"
    full_text += f"**Tarih:** {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
    full_text += f"**Model:** {MODEL_NAME}\n\n"
    full_text += "---\n\n"
    full_text += content
    
    if citations:
        full_text += "\n\n## 🔗 Kaynakça\n"
        for i, link in enumerate(citations, 1):
            full_text += f"{i}. <{link}>\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    return filename

# -------------------------------------------------------------------------
# ANA AKIŞ
# -------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perplexity AI Derinlemesine Araştırma")
    # nargs='?' argümanı opsiyonel yapar
    parser.add_argument("query", type=str, nargs='?', help="Araştırılacak konu")
    
    args = parser.parse_args()
    query = args.query

    # Argüman yoksa interaktif olarak sor
    if not query:
        print("💡 Perplexity Derinlemesine Araştırma Aracı")
        print("------------------------------------------------")
        try:
            query = input("❓ Araştırma konusunu girin: ")
            if not query.strip():
                print("❌ Boş giriş yapıldı, çıkılıyor.")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n❌ İptal edildi.")
            sys.exit(0)
    
    content, citations = search_perplexity(query)
    
    if content:
        saved_file = save_to_markdown(query, content, citations)
        print(f"✅ Rapor başarıyla kaydedildi: {saved_file}")
        # Claude Code için ipucu
        print(f"👉 Claude'a okutmak için: 'cat {saved_file}'")
    else:
        print("❌ Arama başarısız oldu.")