import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filmler=pd.read_csv("data/tmdb_5000_movies.csv")
krediler=pd.read_csv("data/tmdb_5000_credits.csv")

krediler.rename(columns={"movie_id":"id"}, inplace=True)
birlesmis_df=pd.merge(filmler,krediler,on="id")#İki veri setinin ortak sütun olan "id" üzerinden
                                               #birleştirildiği kısım
print(birlesmis_df)

print("\nBirleşmiş Veri Setinin Boyutu (Satır, Sütun):")
print(birlesmis_df.shape)

print("\nVeri Setinin İlk 10 Satırı:")
print(birlesmis_df[["id","title_x","budget","revenue"]].head(10))

print("\nVeri Seti Bilgisi:")
birlesmis_df.info()

print("\nFilmlerin İstatiksel Özeti:")
print(birlesmis_df[["budget","revenue","vote_average"]].describe())

temiz_df=birlesmis_df[(birlesmis_df["budget"]>0) & (birlesmis_df["revenue"]>0)]#Birleştirilmiş veri setinden hatalı/eksik kısımların
                                                                               #çıkarıldığı kısım

print(f"\nTemizlik Öncesi Film Sayısı: {birlesmis_df.shape[0]}")#".shape[0]" veri setinin satır sayısını alır
print(f"Temizlik Sonrası Film Sayısı: {temiz_df.shape[0]}")
print(f"Veri Setinden Çıkarılan Hatalı/Eksik Satır Sayısı: {birlesmis_df.shape[0]-temiz_df.shape[0]}")

temiz_df["kâr"]=temiz_df["revenue"]-temiz_df["budget"]#Veri setine "kâr" sütununun eklediği kısım

temiz_df["YGO"]=temiz_df["kâr"]/temiz_df["budget"]#Veri setine Yatırım Getirisi Oranı (YGO) sütunun
                                                  #eklendiği kısım

temiz_df["release_date"]=pd.to_datetime(temiz_df["release_date"])#Veri setindeki "release_date" sütununun tarih tipine çevrildiği kısım

temiz_df["release_year"]=temiz_df["release_date"].dt.year#"release_date" sütununun yıl bilgisini alıp
                                                         #yeni bir sütun oluşturulduğu kısım

print("\nYeni Üretilen Sütunlar:")
print(temiz_df[["title_x","budget","revenue","kâr","YGO","release_year"]].head())

sns.set_theme(style="whitegrid")#Grafiklerin görsel stilini ayarlayan ana tema fonksiyonu
top_10_kar=temiz_df.nlargest(10,"kâr")
plt.figure(figsize=(12,6))
sns.barplot(data=top_10_kar,x="kâr",y="title_x",palette="magma")#En çok kâr eden ilk 10 film için sütun grafiği oluşturan kısım
plt.title("En Çok Kâr Eden İlk 10 Film", fontsize=14,fontweight="bold")
plt.xlabel("Kâr (Dolar)",fontsize=12)
plt.ylabel("Film Adı",fontsize=12)
plt.tight_layout()#Grafiğin görsel kalitesini ve okunabilirliğini artıran fonksiyon
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=temiz_df,x="budget",y="kâr",alpha=0.6,color="teal")#Bütçe ve kâr arasındaki ilişkiyi görmek için
                                                                        #nokta grafiği oluşturulan kısım
plt.title("Bütçe ve Kâr İlişkisi",fontsize=14,fontweight="bold")
plt.xlabel("Bütçe (Dolar)",fontsize=12)
plt.ylabel("Kâr (Dolar)",fontsize=12)
plt.tight_layout()
plt.show()

korelasyon=temiz_df[["budget","revenue","kâr","YGO","vote_average"]].corr()#".corr()" korelasyon matrisi oluşturan fonksiyon
print("\nKorelasyon Matrisi:")
print(korelasyon)

temiz_df.to_csv("data/temizlenmis_tmdb_movies.csv", index=False)#Sadeleştirmiş ve doğru verileri tutan yeni bir
                                                                #veri seti dosyasını oluşturan ve csv dosyasına fazladan
                                                                #bir sütun eklenmesini önlemek için "index=False" yapılan kısım
print("\nİşlenmiş veri 'data/temizlenmis_tmdb_movies.csv' olarak kaydedildi.")

plt.figure(figsize=(8,6))
sns.heatmap(korelasyon,annot=True,cmap="coolwarm",fmt=".3f",linewidths=0.5)#Korelasyon matrisini ısı haritasında görselleştiren kısım
                                                                           #"annot=True" hücrelerin içine gerçek korelasyon sayılarını yazar
plt.title("Korelasyon Matrisi Isı Haritası",fontsize=14,fontweight="bold")
plt.tight_layout()
plt.show()



