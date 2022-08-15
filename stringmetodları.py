# String (Karakter Dizileri) Metodları
# Veri yapılarının üzerinde çalışan veri yapılarına özel metodlar(fonksiyonlar) bulunur.
# Bu yapılara dir(str) diyerek metodlara ulaşabiliriz.

print(dir(str))
# len fonksiyonu (Boyut Bilgisine Ulaşmak)

name = "VanGogh"
# Bu string değerin sorgulamasını yaparsak eğer str olarak karşımıza çıkar.
print(type(name))
print(len(name))
print(len("sohbet"))
# Kullanmış olduğumuz yapının metod mu fonksiyon mu olduğunu nasıl ayırt ederiz?
# Eğer bir fonksiyon class yapısı içerisinde tanımlandıysa buna metod denir. Eğer bir class yapısı içinde değilse metod değildir.

# Upper() & Lower(): Küçük- Büyük dönüşümleri
print("fatih".upper())
print("FATİH".lower())

# Replace: Karakter değiştirir
hi = "Hello AI Era"
print(hi.replace("l", "p"))

# Split: böler
print("Hello AI Era".split())

# Strip: kırpar
print("ofofo".strip("o"))

# Capitalize: İlk harfleri büyütür
print("foo".capitalize())

# Farklı metod modelleri bulunmaktadır. Şu an için mantığı anlamak adına bu kadar metod örneği bırakıyorum.

