''' Python ve selenium kullanarak pencere/sekme değiştirirken window_handles ile aldığımız listenin indeksini kullanmak doğru ve 
    kullanışlı bir yöntem değil. Onun yerine bu videoda daha kullanışlı bir fonksiyon ile sekmeler arası aşağıdaki fonksiyonu kullanarak nasıl geçiş 
    yacağımızı anlatıyorum. 

    def sekme_degistir(baslik):
        for sayfa in driver.window_handles:
            driver.switch_to.window(sayfa)
            if baslik.lower() in driver.title.lower():
                break

    Kısaca bu fonksiyona geçiş yapmak istediğimiz sayfanın başlığını veya başlığın içinde yer alan o sayfa has bir kelimeyi verebiliriz. 
    Fonksiyon, Webdriver nesnesinin açtığı pencereler/sekmeler arasında tek tek geçiş yaparak her bir sayfanın başlığını alacak. 
    Şayet verdiğimiz parametre kelimesi alınan başlık içindeyse, demekki driver o anda istediğimiz sayfada ve döngüden çıkabilir.
'''