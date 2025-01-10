while True:
  yatay = int(input("Yatay kordinatı girin"))
  dikey = int(input("Dikeyb kordinatı girin"))
  
  if yatay>8 or dikey>8 or yatay<1 or dikey<1:
    print("GEÇERSİZ GİRİŞ")
    continue
  renk = yatay + dikey
  
  if renk%2 ==0:
    print("siyah")
  else:
    print("beyaz")
