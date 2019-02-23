class NumerosRomanos:
    valoresRomanoDecimal = { 
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    valoresDecimalRomano = { 
            1: 'I', 
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M' 
            }
    def __init__ (self):
        pass





    def decimal_romano(self, numero_decimal):
        resultado_romano = ''
        decimal_temporario = numero_decimal
        invertida = sorted(self.valoresDecimalRomano.keys(), reverse=True)

        def dr_letra_unica(decimal, resultado_romano, decimal_temporario):

            resultado_romano += self.valoresDecimalRomano[decimal]
            decimal_temporario -= decimal
            return resultado_romano, decimal_temporario

        def dr_letra_composta(decimal, resultado_romano, decimal_temporario):
            valor_decrementado = decrescimo(decimal_temporario)
            romano_decrementado = self.valoresDecimalRomano[valor_decrementado]
            resultado_romano += "{}{}".format(romano_decrementado, self.valoresDecimalRomano[decimal])
            decimal_temporario -= decimal - valor_decrementado
            return resultado_romano, decimal_temporario

        def decrescimo(decimal_temporario):
            if decimal_temporario >= 400:
                return 100
            elif decimal_temporario >= 40:
                return 10
            elif decimal_temporario >= 4:
                return 1
            else:
                return 0


        while decimal_temporario>0:
            for x in invertida:
                if (decimal_temporario <= 0):
                    break
                if (decimal_temporario >= x):
                    resultado_romano, decimal_temporario = dr_letra_unica(x, resultado_romano, decimal_temporario)

                elif (decimal_temporario >= (x-decrescimo(decimal_temporario))):
                    resultado_romano, decimal_temporario = dr_letra_composta(x, resultado_romano, decimal_temporario)




        return resultado_romano
