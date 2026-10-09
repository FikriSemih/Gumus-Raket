# 🎾 Gümüş Raket Tenis Kulübü & Deuce Cafe

## %100 Çevrimdışı (İnternetsiz) Yerel Bilgisayar Kurulum & Kullanım Kılavuzu

**Tesis:** Bademli / Bursa

**Hedef Cihaz:** Windows 10 (DESKTOP-1DQRR97 • Intel Core i3-6006U • 12,0 GB RAM • 238 GB SSD)

**Çalışma Modu:** **%100 Çevrimdışı (Offline) • Sıfır İnternet Bağımlılığı**

## 🔒 %100 ÇEVRİMDIŞI ÇALIŞMA PRENSİBİ

Bu sistem hiçbir şekilde internete, buluta veya dış sunuculara bağlanmaz:

* Bilgisayarın internet bağlantısı olmasa bile sistem eksiksiz çalışır.

* Tüm üye kayıtları, kasa defteri, aidatlar ve kordaj iş emirleri sadece bu bilgisayarın **238 GB SSD diskinde** saklanır.

* Dışarıya hiçbir veri çıkmaz, kulübün tüm ticari sırları ve üye bilgileri tamamen sizin bilgisayarınızda kalır.

## 🛠️ KUTUDAN ÇIKAN 3 TEMEL PARÇA

1. **`gumus_raket_v3.html`** *(Ana Ekran)*: İnternetsiz çalışan tek parça kulüp yönetim arayüzü.

2. **`server.py`** *(Yerel Motor)*: Bilgisayarın kendi içinde verileri SSD'ye kaydeden yerel motor.

3. **`baslat.bat`** *(Açma Düğmesi)*: Çift tıklayıp sistemi başlatan Windows dosyası.

## 📋 4 BASİT ADIMDA KULLANIMA BAŞLAMA

### \[ADIM 1\] — Masaüstüne Klasör Açın

1. Bilgisayarınızın Masaüstünde boş bir yere sağ tıklayın ➔ **Yeni** ➔ **Klasör** deyin.

2. Klasörün adını **`Gumus_Raket`** yapın.

3. Size verilen dosyaları bu klasörün içine koyun.

```
📁 Masaüstü / Gumus_Raket
  ├── 📄 gumus_raket_v3.html
  ├── ⚙️ server.py
  └── 🚀 baslat.bat

```

### \[ADIM 2\] — `baslat.bat` Dosyasına Çift Tıklayın

1. **`baslat.bat`** dosyasına çift tıklayın.

2. Siyah bir pencere açılır ve tarayıcınızda sistem `http://localhost:3000` adresinden anında açılır.

3. *Siyah pencereyi kapatmayın, simge durumuna küçültebilirsiniz.*

### \[ADIM 3\] — Veri Güvenliği & Kapanış

* Kasiyer gün sonunda `[✓ Vardiyayı Kapat & Devret]` dediğinde arka planda gizli **Z Raporu** oluşur.

* Yapılan her işlem anında diske yazıldığı için elektrik kesilse veya bilgisayar kapansa bile hiçbir veri kaybolmaz.

### \[ADIM 4\] — İleride Güncelleme Yapma (İnternetsiz & Verileri Bozmadan)

Sistemde **Kod Dosyası** ile **Veritabanı Dosyası** birbirinden tamamen bağımsızdır:

* **Kod:** `gumus_raket_v3.html` (Ekranlar, butonlar, özellikler)

* **Veri:** `gumus_raket_veritabani.json` (124 öğrenci, kasa paraları, kordaj fişleri)

İleride yeni bir özellik eklediğimizde eski kayıtları kaybetmeden güncelleme yapmak için:

1. Size yeni sürümü (örneğin `gumus_raket_v4.html`) bir **Flash Bellek (USB)** ile veririz.

2. Bu yeni dosyayı masaüstündeki `Gumus_Raket` klasörünün içine yapıştırırsınız.

3. `server.py` klasördeki yeni `v4` dosyasını otomatik algılar ve yayına alır.

4. **Veritabanı dosyanıza dokunmadığınız için**, 124 öğrencinin aidatları ve kasa bakiyesi milim oynamadan yeni ekranda aynen açılır!