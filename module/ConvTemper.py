"""
PROGRAM KONVERSI SATUAN SUHU
Created By : Nurkholilah Harahap
"""


class TemperatureConverter:
    def __init__(self, val):
        self.__nilai = val

    def celtocel(self):
        return self.__nilai

    def reamtoream(self):
        return self.__nilai

    def fahtofah(self):
        return self.__nilai

    def keltokel(self):
        return self.__nilai

    # FUNGSI Celcius to Reamur
    def celtoream(self):
        return (4.0 / 5 * self.__nilai)

    # FUNGSI Celcius to Fahrenheit
    def celtofah(self):
        return ((9.0/5*self.__nilai)+32)

    # FUNGSI Celcius to Kelvin
    def celtokel(self):
        return (273 + self.__nilai)

    # FUNGSI Reamur to Celcius
    def reamtocel(self):
        return ((5/4)*self.__nilai)

    # FUNGSI Reamur to Fahrenheit
    def reamtofah(self):
        return ((9/4)*self.__nilai + 32)

    # FUNGSI Reamur to Kelvin
    def reamtokel(self):
        return ((5/4) * self.__nilai + 273)

    # FUNGSI Fahrenheit to Celcius
    def fahtocel(self):
        return (5/9*(self.__nilai - 32))

    # FUNGSI Fahrenheit to Reamur
    def fahtoream(self):
        return (4/9*(self.__nilai - 32))

    # FUNGSI Fahrenheit to Kelvin
    def fahtokel(self):
        return (5/9*(self.__nilai) + 273)

    # FUNGSI Kelvin to Celcius
    def keltocel(self):
        return (self.__nilai - 273)

    # FUNGSI Kelvin to Reamur
    def keltoream(self):
        return (4/5*(self.__nilai - 273))

    # FUNGSI Kelvin to Fahrenheit
    def keltofah(self):
        return (9/5*(self.__nilai - 273) + 32)
