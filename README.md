GERİ DÖNÜŞÜM ASİSTANI

**Proje Hakkında**
Geri Dönüşüm Asistanı, yapay zeka destekli, kullanıcıların atık fotoğraflarını yükleyerek hangi geri dönüşüm kategorisine ait olduğunu belirlemelerine yardımcı olan bir web uygulamasıdır. Temel amacı, geri dönüşüm bilincini artırmak, atık ayrıştırma sürecini kolaylaştırmak ve çevresel sürdürülebilirliğe katkıda bulunmaktır.

Kullanıcı dostu arayüzü sayesinde, tek bir fotoğraf çekerek veya yükleyerek atığınızın kağıt, plastik, cam veya metal gibi hangi kutuya ait olduğunu hızla öğrenebilirsiniz.

Özellikler
**Yapay Zeka Destekli Atık Tanıma:** Yüklenen atık görsellerini sınıflandırmak için derin öğrenme modeli kullanır.
**Gerçek Zamanlı Geri Bildirim:** Atığın kategorisi ve hangi kutuya atılması gerektiği hakkında anında bilgi sağlar.
**Görsel Önizleme:** Kullanıcının yüklediği görseli analizden önce önizler.
**Basit ve Temiz Arayüz:** Kolay anlaşılır ve kullanımı pratik bir web arayüzü sunar.
**Hata Yönetimi:** Geçersiz dosya tipleri veya sunucu hataları gibi durumlarda kullanıcıyı bilgilendirir.
**Veritabanı Desteği (SQLite):**İleride analiz geçmişini veya kategori bilgilerini depolamak için altyapı sunar.

Kullanılan Teknolojiler
Proje, hem arka uç hem de ön uç geliştirmeyi kapsayan çeşitli modern teknolojileri bir araya getirmektedir:

Yapay Zeka (AI) & Makine Öğrenimi (ML)
**TensorFlow / Keras:** Derin öğrenme modeli eğitimi ve çıkarımı için ana kütüphane.
**PIL (Pillow):** Görüntü işleme görevleri (boyutlandırma, format dönüştürme).
**NumPy:** Sayısal veri manipülasyonu, özellikle görüntü verilerini tensörlere dönüştürme.
**Evrişimli Sinir Ağları (CNN):** Görsel tanıma için temel makine öğrenimi mimarisi.
**Transfer Öğrenimi:** Hızlı ve verimli model geliştirme için önceden eğitilmiş modellerden faydalanma (örneğin MobileNetV2).

Web Geliştirme
**Python:** Arka uç (backend) geliştirme için ana programlama dili.
**Flask:** Hafif ve esnek Python mikro web çerçevesi (routing, API endpoint'leri, statik dosya sunumu).
**HTML5:** Web sayfasının yapısal iskeleti.
**CSS3:** Web arayüzünün stil ve tasarımı.
**JavaScript (JS):** İstemci tarafı etkileşimler, AJAX (Fetch API) ile asenkron iletişim.
**JSON:** Sunucu ile istemci arasında veri alışverişi formatı.
**Werkzeug:** Flask'in güvenli dosya yükleme gibi yardımcı araçları.

Veritabanı
**SQLite3:** Dosya tabanlı, hafif bir ilişkisel veritabanı çözümü. Python'ın yerleşik `sqlite3` modülü ile kolayca entegre edilmiştir.


