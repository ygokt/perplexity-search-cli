# Perplexity Deep Search CLI

Context/token tasarrufu icin harici Perplexity arama araci.

## Kullanim

```bash
python perplexity_search.py "sorgu"
python perplexity_search.py "sorgu" --model reasoning
```

## Modeller
- `sonar` - Hizli
- `sonar-pro` - Kapsamli (varsayilan)
- `reasoning` - Derin analiz

## Cikti
Raporlar `output/` klasorune MD formatinda kaydedilir.

## API Key
Windows ortam degiskeni: `PERPLEXITY_API_KEY`
