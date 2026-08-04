# 🎬 Film Veri Analizi

Bu proje, [TMDB 5000 Film Veri Seti](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) kullanılarak sinema sektöründeki bütçe, gişe hasılatı ve popülerlik gibi dinamiklerin incelendiği bir veri analizi çalışmasıdır.

## Araçlar ve Kütüphaneler

* **Dil:** Python
* **Veri İşleme:** Pandas
* **Görselleştirme:** Seaborn & Matplotlib

## 📊 Proje Kapsamında Neler Yapıldı?

* **Veri Ön İşleme:** Ham veri seti incelendi, gereksiz indeksler (`to_csv(index=False)`) temizlenerek tablo analize hazır hale getirildi.
* **En'ler (Top 10) Analizi:** En yüksek bütçeli, gişede en çok hasılat yapan ve izleyiciler tarafından en popüler bulunan filmler veri seti üzerinden listelenerek sütun grafiği üzerinden görselleştirildi.
* **Bütçe ve Gişe:** Film bütçeleri ile gelirleri arasındaki dağılım eğilimleri incelendi.
* **Korelasyon Analizi:** Değişkenler arasındaki istatistiksel bağlar `corr()` fonksiyonu ile hesaplanıp, sonuçlar `heatmap` (ısı haritası) üzerinden görselleştirildi.

> **Not:** GitHub dosya boyutu kısıtlamaları nedeniyle orijinal veri setleri repoya yüklenmemiştir (bu büyük dosyalar, repoda bulunan `.gitignore` aracılığıyla dışarıda bırakılmıştır). Projeyi incelemek isterseniz veri setini yukarıdaki bağlantıdan indirebilirsiniz.
