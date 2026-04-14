Ölü Piksel Test Uygulaması Yeni bir monitör veya laptop aldığımda ölü pikselleri hızlıca kontrol edebilmek için bu basit ama etkili aracı geliştirdim. Sadece renkleri göstermekle kalmıyor, hatalı noktayı bulduğunda koordinatlarını da sisteme kaydediyor.

Ne Yapıyor Bu Proje?

Renk Kontrolü: Klavyeden 1, 2, 3, 4, 5 tuşlarını kullanarak ekranı farklı renklere boyayabiliyorsun.

Tıklayıp Kaydet: Eğer bir ölü piksel görürsen üzerine tıkla; JavaScript o anki X ve Y koordinatlarını alıp arka plandaki Flask sunucusuna gönderiyor.

Backend Kaydı: Sunucu (Python), gelen bu hataları terminale veya bir dosyaya rapor olarak basabiliyor.

Çalıştırmadan önce bilgisayarda olması gerekn bir yazılım var.
Bu yazılım(flask) bunu kurmak için aşağıda belirtiğim kodu terminalde çalıştırınız.
"pip install flask"
"pip3 install flask" bu mac için bir komut.

Nasıl Çalıştırılır?

Bilgisayarına Python yüklü olduğundan emin ol.

Terminalden python3 app.py komutunu çalıştır.

Tarayıcıdan 127.0.0.1:5000 adresine gir.

Tam ekran yap ve kontrol etmeye başla.

Kullandığım Teknolojiler

Frontend: HTML, CSS, JavaScript (Koordinat yakalama için).

Backend: Python & Flask (Veri iletişimi için).
