# Fast Calculation

- Fast Calculation, istediğiniz basamakta iki sayıyı toplama ve çıkarma işlemleriyle önünüze getirir.
- Amacınız işlemin sonucunu olabildiğince kısa sürede yazabilmektir.
- Her oyunun sonunda doğru cevapladığınız soru sayısına ve cevap sürenize göre puan kazanırsınız.

-  *Fast Calculation henüz erken geliştirme aşamasında, dolayısıyla geliştirilecek birçok özelliği bulunmakta. Yine de aklınızdaki fikirleri paylaşmaktan çekinmeyin.*


------------

### Değiştirebileceğiniz Özellikler
- fastCalculation.py içindeki SETTINGS kısmında repeatTime(Soru Sayısı) ve limit(Maksimum Basamak Sayısı) özelliklerini istediğiniz gibi değiştirebilirsiniz.
##### Default Settings
```
# SETTINGS
repeatTime = 5
limit = 2
```

------------
### Puan Hesaplanması
 Puanlarınız şu kurallara göre hesaplanır:
 - Her oyun +5 puan alırsınız.
 - 5 saniyenin altında cevapladığınız her soru için hızınız kadar puan alırsınız.
 - Doğru cevapladığınız her soru için basamak limiti ile orantılı olarak puan kazanırsınız.