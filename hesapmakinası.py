while True:
    sayi1 = int(input("1. Sayıyı giriniz = "))
    sayi2 = int(input("2. Sayıyı giriniz = "))
    islem = input("Yapmak istediğiniz işlemi seçin: toplama, çıkarma, çarpma, bölme veya çıkış: ")

    if islem == "toplama":
        print("Sonuç:", sayi1 + sayi2)
    elif islem == "çıkarma":
        print("Sonuç:", sayi1 - sayi2)
    elif islem == "çarpma":
        print("Sonuç:", sayi1 * sayi2)
    elif islem == "bölme":
        if sayi2 == 0:
            print("Hata: Sıfıra bölme yapılamaz!")
        else:
            print("Sonuç:", sayi1 / sayi2)
    elif islem == "çıkış":
        print("Çıkıyor...")
        break  
    else:
        print("Geçersiz işlem girdiniz!")
