# Fast Calculation

- Fast Calculation, istediğiniz basamakta iki sayıyı toplama ve çıkarma işlemleriyle önünüze getirir.
- Amacınız işlemin sonucunu olabildiğince kısa sürede yazabilmektir.
- Her oyunun sonunda doğru cevapladığınız soru sayısına ve cevap sürenize göre puan kazanırsınız.

------------

### Değiştirebileceğiniz Özellikler
- fastCalculation.py içindeki SETTINGS kısmında repeatTime(Soru Sayısı), limit(Maksimum Basamak Sayısı) ve difficulty(Zorluk) özelliklerini istediğiniz gibi değiştirebilirsiniz.
##### Default Settings
```
# SETTINGS
repeatTime = 5
limit = 2
difficulty = 1
```
-  *Tepki süresi bonusunu istemiyorsanız `reaction_time = 0.2` değişkeninin değerini 0.0 olarak ayarlayabilirsiniz.*

------------

### Puan Hesaplanması
 Puanlarınız şu kurallara göre hesaplanır:
 - Her oyun +5 puan alırsınız.
 - 5 saniyenin altında cevapladığınız her soru için hızınız kadar puan alırsınız.
 - Doğru cevapladığınız her soru için basamak limiti ile orantılı olarak puan kazanırsınız.

------------

### Zorluk Dereceleri
- **Kolay Mod [İLERİDE EKLENECEK]:** Doğru bildiğiniz sorulardan puan alabilmek için gereken maksimum cevaplama süresi ~~5 saniyeden~~ **7 saniyeye** çıkarılır. Ancak bildiğiniz sorulardan daha az puan alırsınız.
- **Normal Mod:** Oyunun sıradan ayarlarıyla oynayın.
- **Zor Mod:** Vereceğiniz tek yanlış cevap oyunun direkt bitmesine ve puanınızın hesaplanmamasına sebep olacak. Ayrıca yanlış yaptığınız soruların cevapları gösterilmez.

------------

### Alpha v1.2
#### fastCalculation
- İşlem sürelerinden daha fazla puan alabilmeniz için reaction_time(Tepki Süresi) bonusu eklendi.
- Artık oyun sonunda en uzun ve en kısa cevap sürelerinizi görebileceksiniz.
- Kodlarda birtakım iyileştirmeler yapıldı

#### fastReaction 
- Kritik sorunları henüz çözüme kavuşmadığı için tam olarak yayınlanmasa da fastReaction adlı yeni bir proje üzerinde çalışıyorum.
