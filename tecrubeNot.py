note = int(input("Mezuniyet notunuz nedir"))
tecrube = int(input("1 ve 5 arasında tecrübeniz nedir"))

if note>90 or tecrube==5 and note>70:
  print("İşe al")

elif note>70 or tecrube == 4:
  print("Mülakata çağır")

else:
  print("İşe alma")

