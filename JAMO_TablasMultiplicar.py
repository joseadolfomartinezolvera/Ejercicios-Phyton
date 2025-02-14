from collections import OrderedDict
def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


def tablaDeMultiplicar():
  n = int(input('Ingrese la tabla:'))
  inicio = 1
  fin = 13
  multiplicando = write_roman(n)
  for i in range(inicio, fin):
    multiplicador = write_roman(i)
    total = n*i
    totalRomanos = write_roman(total)
    print(multiplicando, 'x', multiplicador,'=',totalRomanos)
tablaDeMultiplicar()
