# YouTube Playlist'ten Makale Oluşturma ve WordPress'e Yayınlama Projesi

Bu proje, belirli bir YouTube playlist'indeki videoların transkriptlerini indirerek, bu transkriptlerden otomatik olarak makaleler oluşturur ve bu makaleleri bir WordPress sitesine yayınlar. Proje, OpenAI'nin GPT-4 ve DALL·E 3 modellerini kullanarak içerik ve görsel oluşturma işlemlerini otomatikleştirir.

## Özellikler

- YouTube API kullanarak belirli bir playlist'teki videoların bilgilerini çeker.
- Videoların transkriptlerini indirir ve metin dosyaları olarak kaydeder.
- OpenAI GPT-4 modelini kullanarak transkriptlerden makaleler oluşturur.
- OpenAI DALL·E 3 modelini kullanarak makaleler için öne çıkan görseller oluşturur.
- Oluşturulan makaleleri ve görselleri bir WordPress sitesine otomatik olarak yayınlar.

## Kurulum

1. **Gereksinimler**: Projeyi çalıştırmak için Python 3.8 veya üzeri bir sürüm gereklidir.

2. **Bağımlılıkların Yüklenmesi**:
   - Proje bağımlılıklarını yüklemek için aşağıdaki komutu çalıştırın:
     ```bash
     pip install -r requirements.txt
     ```

3. **API Anahtarlarının Ayarlanması**:
   - `.env` dosyası oluşturun ve aşağıdaki ortam değişkenlerini ekleyin:
     ```plaintext
     YOUTUBE_API_KEY=your_youtube_api_key
     OPENAI_API_KEY=your_openai_api_key
     WORDPRESS_BASE_URL=your_wordpress_site_url
     WORDPRESS_USERNAME=your_wordpress_username
     WORDPRESS_PASSWORD=your_wordpress_password
     ```
   - `YOUTUBE_API_KEY`, `OPENAI_API_KEY`, `WORDPRESS_BASE_URL`, `WORDPRESS_USERNAME`, ve `WORDPRESS_PASSWORD` değerlerini kendi API anahtarlarınız ve WordPress bilgilerinizle değiştirin.

4. **Playlist Dosyasının Hazırlanması**:
   - `youtube_list.txt` dosyasına, transkriptlerini indirmek istediğiniz YouTube playlist'lerinin URL'lerini ekleyin. Her URL bir satırda olmalıdır.

## Kullanım

1. **Projeyi Çalıştırma**:
   - Projeyi çalıştırmak için aşağıdaki komutu kullanın:
     ```bash
     python main.py
     ```

2. **Adımlar**:
   - Proje, `youtube_list.txt` dosyasındaki playlist'lerden video bilgilerini çekecek ve transkriptleri indirecektir.
   - Transkriptlerden makaleler oluşturulacak ve bu makaleler için öne çıkan görseller oluşturulacaktır.
   - Oluşturulan makaleler ve görseller, belirtilen WordPress sitesine otomatik olarak yayınlanacaktır.

## Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkılarınızı bekliyoruz. Katkıda bulunmak için:

1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`).
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`).
4. Branch'inizi pushlayın (`git push origin feature/AmazingFeature`).
5. Bir Pull Request açın.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## İletişim

Proje ile ilgili herhangi bir sorunuz veya öneriniz varsa, lütfen bir issue açın veya fakucuker@gmail.com üzerinden bana ulaşın.

## Önemli Uyarı

Bu proje, YouTube'daki videoların transkriptlerini kullanarak otomatik olarak içerik oluşturur. Ancak, YouTube'daki videoların fikir hakları ve telif hakkı korumalarına tabi olabileceğini unutmayın. Bu projeyi kullanarak oluşturduğunuz içeriklerin ticari amaçlarla kullanılması veya dağıtılması, telif hakkı ihlallerine neden olabilir.

**Kullanıcı Sorumluluğu:**
- Bu projeyi kullanarak oluşturduğunuz içeriklerin telif hakkı ihlali oluşturup oluşturmadığını kontrol etmek sizin sorumluluğunuzdadır.
- YouTube'daki videoların transkriptlerini kullanmadan önce, ilgili içerik sahiplerinden gerekli izinleri almanız önemle tavsiye edilir.
- Bu proje, yalnızca eğitim ve kişisel kullanım amaçlıdır. Ticari kullanım için gerekli yasal izinlerin alınması kullanıcının sorumluluğundadır.

Bu projeyi kullanarak, yukarıdaki uyarıları kabul etmiş ve oluşabilecek herhangi bir yasal sorumluluğu üstlenmiş sayılırsınız.
