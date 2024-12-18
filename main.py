preis=24.95 #Kitap fiyatı
rabatt=0.4  #indirim oranı
kargo_1=3   #1. kitabın kargo ücreti
kargo=0.75  #2 ve daha fazla kitap kargo ücreti
zahl=60
#60 kitabın fatura bedelini hesaplayın

print(((preis-preis*rabatt)*zahl)+(kargo_1+kargo*(zahl-1)))