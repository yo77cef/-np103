yas = int(input("Yaşınızı girin"))
note = float(input("Bitirme notunuzu girin"))

if yas>20 or yas<50 or note<80:
  print("Aday uygun değil")
else:
  print("Aday uygun")