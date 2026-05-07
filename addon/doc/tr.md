---
author:
- Çağrı Dogan &lt;cagrid@hotmail.com&gt;
- Umut Korkmaz &lt;umutkork@gmail.com&gt;
autonumber-headings: 1
css:
- style.css
date: 12 Kasım 2019 Salı
extratags: 1
extratags-back: 0
filename: doc_tr
include-after:
- '%addonDir%/doc/dependencies.md'
keywords: dokümantasyon, MarkdownForever, NVDA add-on, Turkish, Türkçe
lang: tr
langd: tr
subtitle: NVDA için tam özellikli Markdown ve HTML dönüştürücü
template: default
title: MarkdownForever %addonVersion% documentation
toc: 1
...

**İçindekiler**
%toc%

## Giriş

MarkdownForever, Markdown veya HTML içeriğini kolayca dönüştüren küçük bir NVDA eklentisidir. Herhangi bir metni Markdown veya HTML biçiminde yazın, görüntüleyin ve istediğiniz zaman sonucu anında dönüştürmek veya önizlemek için basit bir kısayola basın. Tam olarak son web sayfanızda veya HTML kaynak kodunda göründüğü gibi, HTML'yi destekleyen herhangi bir metin alanına yapıştırılmaya hazır.

MarkdownForever ile:

* Markdown'ı HTML'ye dönüştürebilir
* Markdown'ı HTML kaynak koduna dönüştürebilir
* HTML'yi Markdown'a dönüştürebilir
* Markdown'u biçimlendirilmiş HTML'ye dönüştürebilirsiniz

## Ama bu Markdown olayı Dünya'da ne?

Wikipedia'ya göre,
> Markdown, düz metin biçimlendirme sözdizimine sahip hafif bir biçimlendirme dilidir. Tasarımı birçok çıktı biçimine dönüştürülmesine izin verir, ancak aynı ada sahip orijinal araç yalnızca HTML'yi destekler. Markdown genellikle benioku dosyalarını biçimlendirmek, çevrimiçi tartışma forumlarına mesaj yazmak ve düz metin düzenleyicisi kullanarak zengin metin oluşturmak için kullanılır.

Markdown hakkında daha fazla bilgi için [Wikipedia'daki makalenin tamamı.](https://en.wikipedia.org/wiki/Markdown) okunabilir.

Dolayısıyla, web belgelerinizi hata yapma riski olan HTML kullanarak yazmak yerine, kolay ezberlenen etiketleri kullanacaksınız ve işiniz kısa zamanda bitecek. Markdown ile HTML'nin yapabileceği şeyleri az ya da çok yapabilirsiniz: başlıklar, sıralı (numaralı) veya sırasız (madde işaretli) listeler, bağlantılar ve hatta tablolar.

Örneğin, birinci düzey bir başlık yapmak istiyorsanız, bir karma işareti (#) ve ardından başlığınızın adını aralarında boşluk olacak veya olmayacak biçimde yazacaksınız:

> `#Bu, birinci düzey bir başlık örneğidir`

son HTML belgenizde aşağıdaki gibi gösterilir:

> <h1>\!Bu, birinci düzey bir başlık örneğidir</h1>

İkinci düzey bir başlık için İki diyez  işareti kullanacaksınız, üçüncü seviye için üç, Vb.
 
Şimdi sıralanmamış bir öğe listesi oluşturalım. Bunu yapmak için, listenizdeki tüm öğelere yıldız işareti (*) ekleyebilirsiniz. İşte bir örnek:

<blockquote>
```
* Portakal
* Şeker
* Süt
```
</blockquote>

Bu şu şekilde gösterilecektir:

> * Portakal
> * Şeker
> * Süt

Ayrıca bağlantının başlığını köşeli parantez ([]) içine yazıp, ardından boşluk bırakmadan parantez içine URL'yi ekleyerek de bağlantı oluşturabilirsiniz. Örneğin:

    [NVAccess'in web sitesini ziyaret etmek için buraya tıklayın](https://www.nvaccess.org)

Bu şu şekilde gösterilir:

[NVAccess'in web sitesini ziyaret etmek için buraya tıklayın](https://www.nvaccess.org)
 
Hatta şunları da koyabilirsiniz: *italik yazı* yıldız işaretleri içine alarak veya **kalın yazı** iki yıldızla çevreleyerek... Olasılıklar çok. Şuna bir bakın [Markdown ipuçları Sayfası](https://www.markdownguide.org/cheat-sheet/) for more tags and details.

## Markdown'ı HTML'ye dönüştürme

Bu özellik, ekranda görüntülenen herhangi bir Markdown metnini HTML'ye dönüştürmenize olanak tanır ve Markdown'unuzun son HTML belgesinde nasıl görüneceğini gösterir. Bu, Markdown biçiminde yazdığınız bir belge, sabit diskinizde zaten bulunan bir .md dosyası veya bir web sayfasında bulunan Markdown metni olabilir. Varsayılan olarak, MarkdownForever o anda görüntülenen tüm metni dönüştürür, ancak dönüştürülecek yalnızca belirli bir parçayı da seçebilirsiniz.

Aşağıdaki komutları kullanabilirsiniz:

- *NVDA+ALT+b*: Sonucu varsayılan web tarayıcınızda web sayfası olarak görüntüler.
- *NVDA+ALT+n*: Sonucu NVDA'nın sanal arabelleğinde bir web sayfası olarak görüntüler.

NVDA'nın kendi kullandığı tarama kipindense, sonucu tarayıcıda göstermeniz önerilir Bazı etiketler, özellikle HTML5 etiketleri örneğin `<details>,` NVDA sanal arabelleğince desteklenmez.

## Markdown'u HTML kaynak koduna dönüştürme

Bu, Markdown metnini saf HTML diline dönüştürür. İşiniz bittiğinde dosyayı bir HTML dosyasına, bir forum yayınına veya HTML kodunun desteklendiği web üzerindeki herhangi bir metin alanına kopyalayıp yapıştırabilirsiniz.

Aşağıdaki komutlar kullanılabilir:

- *NVDA+ALT+l*: Sonuç, NVDA'nın sanal arabelleğinde görüntülenir.
- *NVDA+Ctrl+h*: HTML kaynak kodunu panoya kopyalar.

## HTML'yi Markdown'a dönüştürme

Bu özellik, bir HTML kaynak içeriğinden bir Markdown metni üretmeye çalışır. Her zamanki gibi bu, ekranda görüntülenen metnin tamamı veya belirli bir bölüm üzerinde çalışır. Aşağıdaki komutlar kullanılabilir:

- *NVDA+Alt+k*: Sonucu  NVDA sanal arabelleğinde gösterir.
- *NVDA+Shift+g*: Sonucu panoya kopyalar.

Bir HTML web sayfasını URL'sini seçerek Markdown'a da dönüştürebilirsiniz. Tabii, önce varsayılan HTML2Text dönüşüm motorunun doğru ayarlandığından emin olmalısınız, bunu NVDA'nın ana menüsünde bulunan [MarkdownForever ayarları,](#markdownforevers-default-settings) altından yapabilirsiniz.
 
## Markdown'u Biçimlendirilmiş HTML'ye Dönüştürme

Bu işlev, Markdown içeriğinizi biçimlendirilmiş HTML'ye dönüştürür ve panoya kopyalar. Biçimlendirilmiş HTML, tıklanabilir bağlantılar, başlıklar vb. İle tarayıcınız tarafından görüntülenen herhangi bir web sayfasına benzeyecektir. Bu yalnızca bir Markdown içeriğinden oluşturulabilir. HTML kaynak koduyla çalışmaz. Bu eylemi gerçekleştirmek için NVDA + shift + h tuşlarına basın.

Lütfen dikkat! biçimlendirilmiş HTMLMicrosoft Word, Wordpad, Thunderbird gibi uygulamalara, web sayfasındaki bazı zengin metin alanları vb yapıştırılabilir. Ancak, Notepad, Notepad++, gibi metin düzenleyicilerine yapıştırılamaz.

## Etkileşimli Mod

Etkileşimli mod, tüm MarkdownForever özelliklerini daha kullanışlı ekstralar barındıran uygun bir iletişim kutusunda sunan bir işlevdir, Etkileşimli Modu açmak için NVDA + CTRL + i tuşlarına basın.
İşte Sekme sırasıyla ekranların açıklamaları:

* "Dönüştür": Bu ilk birleşik giriş kutusu dönüşüm yönünü seçmenizi sağlar: HTML, HTML kaynağı veya Markdown. Seçmek için yukarı ve aşağı ok tuşlarını kullanın.
* "İçindekiler tablosu oluştur": Bu onay kutusu, her bir bölüme yönlendiren tıklanabilir bağlantılar içeren son HTML belgenizin bölümlerinin bir dizinini oluşturmanıza veya oluşturmamanıza olanak tanır. Bu seçeneğin durumu, [Markdown forever ayarları](#markdownforevers-default-settings) altından da belirlenebilir.
* "Başlıkları otomatik olarak numaralandırmayı deneyin": İşaretliyse, Markdown Forever başlıklarınıza (veya bölümlerinize) her başlığın seviyesine göre numaralı ön ekler koymaya çalışır ÖRN başlık seviyesi 1 için "1.", Seviye 2 için "1.1." vb. 
* "Özel etiketleri Etkinleştir": İşaretlenirse, Markdown içeriğinizde gerçek tarih veya saat gibi şeyleri otomatik olarak eklemek için özel etiketler kullanma olanağı sunar. Bu seçeneğin durumu, [MarkdownForever ayarları](#markdownforevers-default-settings) altından da varsayılan olarak ayarlanabilir.
* "Özel etiketlerin tersine çevirisine izin ver": Bu [Özel-etiketler](#extra-tags)in Markdown Forever tarafından oluşturulan bir HTML içeriğini Markdown'a geri dönüştürürken orijinal formlarına geri döndürülüp döndürülmeyeceğini belirler. (örneğin %date%). 
* "Başlık": HTML belgenizin, internet tarayıcısında gösterilecek olan başlığını buraya girebilirsiniz.
* "Bağlantılı meta veri bloğu": Bu salt okunur alan şunları görüntüler: 
* "HTML kaynağından bağlantılı meta veriler oluşturun ": Bir HTML kaynak dosyasını Markdown'a dönüştürürken, kaynak koddaki meta verileri tahmin etmeye çalışır (başlık, dil, dosya adı vb.) ve sizin için [meta veri bloğu](#optional-metadata-block) oluşturur. Bu seçenek yalnızca HTML'den Markdown'a dönüşüm için kullanılabilir.
* "Sanal Tamponda Göster": Dönüştürülen içeriğinizi sanal bir NVDA arabelleğinde açar.
* "Tarayıcıda Göster": Dönüştürülmüş içeriğinizi varsayılan internet tarayıcınızda görüntüler.
* "Panoya kopyala": Dönüştürülen içeriğinizi yapıştırılmaya hazır olarak Windows panonuza yerleştirir.
* "Farklı kaydet": Dönüştürülmüş belgenizi standart Farklı Kaydet pencereleri iletişim kutusu aracılığıyla sabit diskinize kaydetmenizi ister. Varsayılan Kaydetme konumu [MarkdownForever varsayılan ayarlarında](#markdownforevers-default-settings) da ayarlanabilir.

## İsteğe bağlı Meta veri bloğu

Meta veri bloğu, [Varsayılan ayarlardan](#markdownforevers-default-settings) bağımsız olarak belirli bir belge için belirli parametreler ayarlamanıza olanak tanır. Belgenin en başına yerleştirilmeli ve üç tire ("---") ile başlamalı ve üç nokta ("...") veya üç tire ("---") ile bitmelidir. Her giriş şu biçimde girilmelidir: anahtar: "değer" (değer tırnak işaretleri içine alınmalıdır). Meta veri bloğundan sonra boş bir satır bulunmalıdır.

### Desteklenen meta verilerin listesi

* author (veya authors): Belge için bir veya daha fazla yazar adı belirtmenizi sağlar. (aşağıdaki örneğe bakın) HTML dosyasının üstbilgi bölümüne eklenecektir. Bu anahtar büyük / küçük harfe duyarlı değildir.
* autonumber-headings: Başlıkların otomatik olarak numaralandırılıp numaralandırılmayacağını belirtmenizi sağlar. Olası değerler: true (1) veya false (0).
* css (veya CSS): Belgenizin sunumu için bir veya daha fazla CSS dosyası belirtmenizi sağlar. (aşağıdaki örneğe bakın) Bu anahtar büyük / küçük harfe duyarlı değildir.
* date: Belgeniz için bir tarih belirtmenizi sağlar. HTML dosyasının üstbilgi bölümüne eklenecektir.
* extratags: [Özel etiketlerin](#extra-tags) yorumlanıp yorumlanmayacağını belirtmenizi sağlar. Olası değerler: true (1) veya false (0).
* extratags-back: Markdown Forever tarafından oluşturulan bir HTML içeriğini Markdown'a dönüştürürken [Özel etiketlerin ]((#extra-tags) orijinal biçimlerine (örneğin %date%) geri döndürülüp döndürülmeyeceğini belirtmenizi sağlar. Olası değerler: true (1) veya false (0).
* filename: kaydederken çıktı dosyasının adını belirtmenizi sağlar.
* keywords: Belgenizin kapsadığı konu (lar) ile ilgili anahtar kelimeler belirlemeye yarar.
* lang: belgenin ana dilini belirtmenizi sağlar. Eğer gerekliyse, belgenin içindeki dil değişikliklerini belirtmek için span / div etiketlerini lang parametresiyle kullanın.
* mathjax: [LaTeX ](https://en.wikipedia.org/wiki/LaTeX) 'da yazılmış matematiksel formüllerin dönüştürülüp dönüştürülmeyeceğini belirtmenizi sağlar. Olası değerler: doğru (1) veya yanlış (0). İnternet bağlantısı gereklidir ve dönüştürülmüş sonucu düzgün görüntülemek için tarayıcınızda açmanız gerekir, çünkü yorumlanmış LaTeX, NVDA'nın sanal tamponu tarafından oluşturulamaz.
[MathJax hakkında daha fazla bilgi almak için buraya tıklayın.](http://docs.mathjax.org/en/latest/)
* path: belgenin oluşturulması gereken dizini belirtmenizi sağlar. % Userprofile%,% appdata% ve% tmp% ortam değişkenleri desteklenir.
* subtitle: HTML belgeniz için bir alt başlık belirtmenizi sağlar. HTML dosyasının üstbilgi bölümüne eklenecektir.
* title: HTML belgesinin başlığını belirtmenizi sağlar. Etkileşimli Modda, başlık alanı bu anahtarın değeri kullanılarak otomatik olarak doldurulur.
* toc: içindekiler tablosunun oluşturulup oluşturulmayacağını belirtmek için kullanılır. Olası değerler: true (1) veya false (0).

### Meta veri kullanım örneği
<blockquote>
```
---
title: "basit bir başlık"
date: 2019-11-08
subtitle: "bu belgenizin alt başlığı"
lang: tr
author:
- Çağrı Doğan
- Engin Albayrak
CSS:
%userprofile%/document/main.css
%userprofile%/document/custom.css
keywords: NVDA, Markdown, HTML
filename: deneme
path: "%userprofile%/desktop"
toc: 0
autonumber-headings: 1
mathjax: 0
---

Merhaba Dünya! <span lang="fr">Bonjour le monde !</span> <span lang="es">¡Hola mundo!</span>
```
</blockquote>

Yukarıdaki örnekte, kullandığınız ses sentezleyicinin otomatik dil değiştirmeyi desteklediği ve ilgili onay kutusunun NVDA konuşma ayarlarında işaretlendiği varsayılarak metin üç dilde seslendirilecektir. Ses şu şekilde duyulur:

> Selam Dünya! <span lang="fr">Bonjour tout le monde!</span> <span lang="es">buenos días!</span>

## Özel etiketler

Özel etiketler, geçerli tarih veya saat gibi sistem bilgilerini otomatik olarak eklemek için Markdown içeriğinize koyabileceğiniz, HTML belgenizde net metin olarak görüntülenecek özel yer tutuculardır.

### Desteklenen Özel etiketler

| **Markdown içeriği** | **açıklama** | **Tarayıcıdaki sonuç** |
| :----------: | :----------: | :----------: |
| `%date%` | Geçerli tarih | %date% |
| `%time%` | Geçerli zaman | %time% |
| `%now%` | Geçerli tarih / saat | %now% |
| `%day%` | bulunulan  gün (uzun format) | %day% |
| `%dday%` | bulunulan gün (ondalık biçim) | %dday% |
| `%month%` | Ay (uzun format) | %month% |
| `%dmonth%` | Bulunulan ay (ondalık biçim) | %dmonth% |
| `%year%` | Bulunulan yıl (2 hane) | %year% |
| `%Year%` | bulunulan yıl (4 hane) | %Year% |
| `%toc%` | İmlecin konumundaki içerik tablosu (meta veri veya varsayılan ayarlarla etkinleştirildiyse) | N/A |

## MarkdownForever'ın varsayılan ayarları

Bunlara NVDA menüsü / MarkdownForever Ayarları / Ayarlar yolundan erişilebilir ve yukarıda belirtilen dönüştürme işlemiyle ilgili çeşitli ayarları varsayılan olarak yapılandırmanıza ve ayarlamanıza izin verir:

* "İçindekiler tablosu oluştur": Bu onay kutusu, her bir bölüme yönlendiren tıklanabilir bağlantılar içeren son HTML belgenizin bölümlerinin bir dizinini oluşturmanıza veya oluşturmamanıza olanak tanır. Bu davranış, [isteğe bağlı meta veri bloğu](#optional-metadata-block) içindeki "toc" anahtarı kullanılarak her belge için ayrı ayrı da ayarlanabilir ve ilgili [Özel etiket](#extra-tags) kullanılarak belgenin herhangi bir yerine yerleştirilebilir.
* "Özel etiketleri Etkinleştir": Bu işaretlenirse, gerçek tarih veya saat gibi şeyleri otomatik olarak eklemek için Markdown içeriğinizde [özel etiketler](#extra-tags) kullanma olanağı sağlar. Bu davranış, [isteğe bağlı meta veri bloğundaki](#optional-metadata-block) "extratags" anahtarı kullanılarak belge başına da ayarlanabilir.
* "HTML kaynağı için karşılık gelen meta veriler oluştur": Bir HTML kaynak dosyasını Markdown'a dönüştürürken, meta verileri kaynak koddan (başlık, dil, dosya adı vb.) tahmin etmeye çalışır ve [meta veri bloğu](#optionnal-metadata-block)unu sizin oluşturur.
* "Etkileşimli modda varsayılan eylem": Bu, [Etkileşimli mod](#interactive-mode)da enter tuşuna basıldığında gerçekleştirilecek varsayılan eylemi seçmenize olanak tanır: (Oluşturulan içeriği tarayıcınızda, NVDA  geçici arabelleğindde gösterebilir veya panoya kopyalayabilirsiniz.
* "Markdown motoru": MarkdownForever iki dönüşüm motoru arasında seçim yapmanızı sağlar, [HTML2Text](https://pypi.org/project/html2text/) ve [HTML2Markdown.](https://pypi.org/project/html2markdown/) İhtiyacınıza veya üretilen sonuca göre tercih ettiğiniz ürünü deneyin ve seçin.
* "Markdown uzantıları": `markdown-it-py` tarafından desteklenen özellikleri yapılandırır (tablolar, görev listeleri, dipnotlar, başlık kimlikleri vb.).
* "yol": Burada, dönüştürülen belgeleriniz için sabit diskinizde varsayılan bir kaydetme konumu belirleyebilirsiniz. tüm çalışmalarınızı saklamak için her zaman aynı klasörü kullanmanız yararlı olur.
* "HTML şablonlarını yönet": Bu, HTML şablonları eklemeye, düzenlemeye ve silmeye izin veren bir iletişim kutusu açar. Şablonlarla, sayfa stilinden sorumlu olan CSS (basamaklı stil sayfaları) kullanarak oluşturulan HTML belgelerinizin görsel yönlerini özelleştirebilirsiniz. Bu, renkleri değiştirmenize, yapımlarınıza görüntü  veya resimler eklemenize ve her özel ihtiyaç için bir şablon oluşturmanıza olanak tanır. Tabii ki web üzerinde CSS öğrenmek için birçok öğretici var,  mesela [bu](https://www.htmldog.com/guides/css/beginner/) iyi bir başlangıç noktası olabilir.

## Komut özeti

- *NVDA+CTRL+i*: Etkileşimli mod
- *NVDA+ALT+b*: Markdown'dan HTML'e dönüştürür. Sonuç varsayılan tarayıcınızda görüntülenir.
- *NVDA+ALT+n*: Markdown'dan HTML'e dönüştürür. Sonuç, NVDA'nın geçici arabelleğinde gösterilir.
- *NVDA+ALT+k*: HTML'den Markdown'a dönüştürür. Sonuç NVDA'nın geçici arabelleğinde gösterilir.
- *NVDA+ALT+l*: Markdown'dan kaynak HTML'e dönüştürür. Sonuç NVDA'nın geçici arabelleğinde gösterilir.
- *NVDA+SHIFT+g*: HTML'den Markdown'a dönüştürür. Sonuç panoya kopyalanır.
- *NVDA+SHIFT+h*: Markdown'dan biçimlendirilmiş HTML'e dönüştürür: Sonuç panoya kopyalanır.
- *NVDA+CTRL+h*: Markdown'dan kaynak HTML'e dönüştürür. Sonuç panoya kopyalanır.

## Eklenti Bilgileri

* Authors:
	- André &lt;<dev@andreabc.net>&gt;: eklentinin yaratıcısı ve ana sürdürücüsü.
	- Sof &lt;<hellosof@gmail.com>&gt;: İngilizce ve Fransızca dokümantasyon, çeşitli öneriler.
	- Victor Cai: Çince yerelleştirmesi.
	- Çağrı Dogan, Umut Korkmaz: Türkçe lokalizasyon.
	- Rémy Ruiz &lt;<remyruiz@gmail.com>&gt;: İspanyolca yerelleştirm.
	- Ve daha fazlası!
* License: GNU General Public License, version 2
* [kararlı sürüm](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon)
* [geliştirme sürümü](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon?channel=dev)
* GitHub repository: [aaclause/NVDA-markdownForever](https://github.com/aaclause/nvda-markdownForever)
* **Dahil edilen bileşenler**: