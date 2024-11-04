''' Bazen web sayfası geliştirirken geniş liste veya seçenekleri kullanıcıya göstermek gerekebilir. 
    Kullanıcı bu listeyi vey seçenekleri görmek için sayfayı kaydırdığında asıl sayfanın sabit kalmasını isteriz. 
    İşte bu tür durumlarda yazılımcılar iframe ile bir sayfayı başka bir sayfanın içine yerleştirirler.

    Başka bir sayfa ile etkileşime geçeceğimiz için Webdriver nesnemizi o sayfaya yönlendirmeliyiz.  
    Bunun için selenium ile driver.switch_to.frame(tanımlayıcı) frame e geçiş yapıp oradaki işlemlerimizi tanımlayabiliriz. 

    Burada bir frame i tanımlamak için üç yolumuz var. 
    1. Id: şayet geçiş yapacağımız iframe in id si var ise onu verebiliriz. 
    2. Name: iframe in name attribute varsa onu kullanabiliriz
    3. Index: sayfada kaçıncı iframe e geçiş yapmak istiyorsak onun indeksini verebiliriz. 
    Burada webelement listesinden bahsettiğimiz için indeks 0-tabanlı. Yani switch_to.frame(0) Webdriver nesnemizi sayfadaki ilk iframe e götürecektir. 

    Iframe ile işimiz bittikten sonra Webdriver nesnemizi tekrar oradan çıkarmamız gerekir. Selenium bize bunun için iki seçenek sunuyor

    1. switch_to.parent_frame : bir üst iframe e geçmek. Şayet iframe içinde iframe varsa en içtekinden bir üst iframe e geçmek için bunu kullanmamız gerekecek
    2. switch_to.default_content(): bu ise bizi sayfanın kendisine götürecektir, yani bütün iframe lerin dışına. 

    NOT: şayet sayfada bir tane iframe var ise onun içinden sayfanın kendisine dönmek için de parent_frame kullanabiliriz. 
    Ama kullanmamalıyız. Sayfanın kendisine geçişler için default_content i tercih etmeliyiz. 
'''