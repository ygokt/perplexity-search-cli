# Perplexity Deep Search CLI - Proje Planı

## Amaç
Claude Code'un context/token tasarrufu yapması için harici bir Perplexity arama scripti.

## Kapsam
- **CLI tabanlı** Python scripti
- **Markdown çıktı** (dosyaya kayıt)
- **Windows ortam değişkeni** ile API key yönetimi

## Dosya Yapısı
```
C:\Projeler\perplexity\
├── perplexity_search.py    # Ana script
├── .env.example            # Örnek env dosyası (opsiyonel referans)
├── output/                 # Raporların kaydedileceği klasör
└── requirements.txt        # Bağımlılıklar
```

## Özellikler

### 1. Model Seçimi
- `sonar` - Hızlı arama
- `sonar-pro` - Daha kapsamlı arama
- `sonar-reasoning-pro` - Derin mantık yürütme (deep research muadili)

### 2. Kullanım Şekilleri
```bash
# Basit arama
python perplexity_search.py "2024 yapay zeka trendleri"

# Model seçerek
python perplexity_search.py "konu" --model sonar-reasoning-pro

# Çıktı klasörü belirterek
python perplexity_search.py "konu" --output ./raporlar
```

### 3. Çıktı Formatı
- Tarih ve model bilgisi
- Ana içerik (Markdown)
- Kaynakça (citations)
- Dosya adı: `YYYYMMDD_HHMMSS_konu.md`

## Uygulama Adımları

1. [ ] `perplexity_search.py` oluştur
2. [ ] `requirements.txt` oluştur
3. [ ] `output/` klasörü için .gitkeep
4. [ ] `.env.example` oluştur (referans için)
5. [ ] Test et

## Bağımlılıklar
- `requests` - HTTP istekleri
- `python-dotenv` (opsiyonel) - .env desteği

## Notlar
- Gemini'nin önerisi temel alındı, sadeleştirildi
- Emojiler kaldırıldı (Claude Code ile uyum)
- Hata mesajları açık ve anlaşılır
