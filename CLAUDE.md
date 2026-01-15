# YAZILIM GELİŞTİRME TEMEL PRENSİPLERİ

Bu belge, projelerde uyulması gereken asgari standartları ve geliştirme felsefesini tanımlar. Amaç; güvenli, modüler ve yüksek performanslı yazılımları en yalın haliyle üretmektir.

## 1. Yalınlık ve Etkinlik İlkesi (Zen Felsefesi)
- **Minimum Kod, Maksimum İşlev:** Hedeflenen kalite ve performansa, mümkün olan en az satır kod ve en basit yapı ile ulaşılmalıdır.
- **Karmaşıklıktan Kaçınma:** Çözümler, problemin kendisinden daha karmaşık olmamalıdır. Anlaşılırlık, zekice yazılmış karmaşık koddan üstündür.
- **Odaklanma:** Yalnızca mevcut gereksinimleri karşılayan kod yazılmalı, gelecekteki varsayımlar üzerine geliştirme yapılmamalıdır.
- **Kaynak Verimliliği:** Kod, gereksiz döngülerden ve bellek yükünden arındırılmış olmalıdır. Donanımı yormayan yalın çözümler esastır.

## 2. Modüler Mimari
- **Parçalı Yapı:** Yazılım, birbirinden bağımsız çalışabilen, yönetilebilir küçük modüllere bölünmelidir.
- **Sorumlulukların Ayrılığı:** Her fonksiyon, sınıf veya modül yalnızca tek bir işi yapmalı ve o işi eksiksiz yerine getirmelidir.
- **Gevşek Bağlılık:** Bir modülde yapılan değişiklik, sistemin genelini veya diğer modüllerin işleyişini bozmamalıdır.
- **Ölçeklenebilirlik Prensibi:** Modüller, gelecek genişlemelere açık tasarlanır, ama overengineering yapılmaz.

## 3. Mühendislik Aşırılığından Kaçınma (Anti-Overengineering)
- **Amaca Uygunluk:** Projenin ölçeğine uygun araç ve yöntemler seçilmelidir. Basit bir script için karmaşık mimariler kurulmamalıdır.
- **Standart Çözümler:** Kanıtlanmış, standart kütüphaneler ve yöntemler tercih edilmeli; gereksiz yere özel (custom) yapılar icat edilmemelidir.

## 4. Veri Güvenliği ve Mahremiyet
- **Sır Yönetimi:** API anahtarları, şifreler ve özel bağlantı bilgileri kesinlikle kod içerisine (hard-coded) yazılmamalıdır.
- **Çevre Değişkenleri:** Tüm hassas bilgiler `.env` dosyaları veya güvenli çevre değişkenleri üzerinden yönetilmelidir.
- **İzolasyon:** `.env` dosyaları versiyon kontrol sistemlerine (Git vb.) dahil edilmemelidir.
- **Kişisel Veri Yasağı:** Geliştiricinin gerçek e-posta adresi, telefon numarası, adı veya kişisel bilgileri **ASLA** kod içine, test verisine veya herkese açık dosyalara (public repo) yazılmaz.
- **Yer Tutucu (Placeholder) Kullanımı:** E-posta gerekliyse `admin@example.com`, telefon gerekliyse `555-0000` gibi hayali veriler kullanılır.

## 5. Kod Kalitesi ve Okunabilirlik
- **Anlamlı İsimlendirme:** Değişken ve fonksiyon isimleri, yaptıkları işi açıkça ifade etmelidir.
- **Sürdürülebilirlik:** Kod, dokümantasyona ihtiyaç duymayacak kadar açık yazılmalı; gerektiği durumlarda kısa ve açıklayıcı yorum satırları eklenmelidir.

## 6. Ürün Yaşam Döngüsü ve MVP Yaklaşımı
- **Odaklı Geliştirme:** İlk sürümde sadece "olmazsa olmaz" özellikler geliştirilir. "Olsa güzel olur" özellikleri, ürün çalışıp değer ürettikten sonraya bırakılır. Bu sayede pazara çıkış hızı artırılır.

## 7. Basitleştirilmiş Dağıtım (Deployment)
- **İkili Ortam Kuralı:** Sistem sadece iki aşamadan oluşur: Lokal (Geliştirme) ve Canlı (Production).
- **Canlıda Kodlama Yasağı:** Canlı sistem üzerinde asla doğrudan kod değişikliği yapılmaz. Geliştirmeler lokalde tamamlanıp test edildikten sonra canlıya gönderilir.

## 8. Otomatik Hata Yönetimi
- **Kendi Kendini Açıklayan Hatalar:** Kod, bir hata oluştuğunda sistemin neden durduğunu basit bir metin dosyasına (log) yazacak şekilde kurgulanmalıdır. Bu, hata ayıklama süresini dakikalara indirir.

## 9. Oturum Devir Teslimi (Context Preservation)
- **Başlangıç Kuralı:** Her yeni oturumun başında, önce varsa `SESSION_LOG.md` dosyasını okuyarak projenin son durumunu ve hedefleri hafızana yüklemek **zorundasın**.
- **Bitiş Kuralı:** Oturum sonlandırılmadan önce, yoksa `SESSION_LOG.md` dosyasını oluşturmalı, varsa şu üç başlık altında güncellemek **zorundasın**:
  1. ** Tamamlananlar:** Bu oturumda teknik olarak bitirdiğin işler.
  2. ** Mevcut Durum:** Kod şu an çalışıyor mu? Bilinen hatalar neler?
  3. ** Sonraki Adımlar:** Bir sonraki oturumda yapılması gereken öncelikli görevler.
  
 ## 10. Etkileşimli Planlama ve Netleştirme (Plan Mode)
- **Önce Sor:** Karmaşık görevlerde varsayım yapma. Kodlamaya başlamadan önce `AskUserQuestionTool` kullanarak detayları sor ve netleştir.
- **Plan Dosyası:** Netleştirmeden sonra, kod yazmadan önce bir `PROJECT_PLAN.md` dosyası oluştur. İzleyeceğin adımları buraya yaz ve kullanıcı onaylamadan kodlamaya başlama.

## 11. Versiyon Kontrol Otomasyonu (GitHub)
- **Tam Yetki:** Kullanıcı talimat verdiğinde; repo oluşturma, commit atma ve push işlemlerini otomatik olarak gerçekleştir.
- **Akıllı Kayıt:** Büyük değişiklikleri bekleme. Çalışan her anlamlı parçadan sonra (atomic commits) otomatik commit ve push yap.

## 12. Kriz Yönetimi ve Hata Döngüsü (Anti-Loop) 🛑

- **3 Vuruş Kuralı (Three-Strike Rule):** Bir hatayı düzeltmek için 3 kez deneme yaptıysan ve hala çözülmediyse, **DURMAK ZORUNDASIN**.
- **Körü Körüne Düzeltme Yasak:** 4. denemeyi yapmadan önce, sorunu analiz et, kök nedeni (root cause) kullanıcıya açıkla ve strateji değiştir. Rastgele kod deneyerek token ve zaman harcama.
- **Geri Alma (Rollback):** Eğer bir düzeltme girişimi daha fazla hata doğuruyorsa, hemen değişiklikleri geri al ve temiz duruma dön.

## 13. Test ve Doğrulama (Kalite Güvencesi)
- **Kritik Test Kuralı:** Sistemin para, veri kaydı veya hukuksal işlem yapan kritik fonksiyonları için mutlaka basit birim testleri (unit test) yazılmalıdır.
- **Otomatik Üretim:** Test kodlarını yazmakla zaman kaybedilmemeli; test senaryoları yapay zeka tarafından üretilmeli ve doğrulanmalıdır.