bakiye = 1000
while True:
  istek = int(input("Para yatırmak 1 para çekmek için 2 yazın"))
  
  if istek == 1:
    yatirma = int(input("Tutar girin"))
    bakiye = bakiye + yatirma
    print bakiye
    continue
  
  while bakiye>0 :
  
    if istek == 2:
      cekme = int(input("Tutar girin"))
      bakiye = bakiye - cekme
      
      if bakiye<0:
        print("Yetersiz bakiye")
        break
      elif bakiye>0:
        print(bakiye)
     
    
    
  


  


