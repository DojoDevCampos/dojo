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
    def decimal_romano(self,numero_decimal):      
        resultado_romano = ''
        decimal_temporario = numero_decimal
        while decimal_temporario>0:
            for x in sorted(self.valoresDecimalRomano.keys(),reverse=True): 
                if (decimal_temporario >= x):
                      resultado_romano += self.valoresDecimalRomano[x]
                      decimal_temporario -= x
        return resultado_romano
        return self.valoresDecimalRomano[numero_decimal]
