class long: 
  def longitud(self):
    letra=input("Ingrese palabra: ")
    num=letra.lower()
    num=num[0].upper()+num[1:]
    numletra=0
    for i in letra:
      numletra+=1
    print('La palabra ' , num , 'tiene',numletra,'letras')

  

cadena=long()
cadena.longitud()
