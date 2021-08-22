# Program Konversi Massa
"""
PROGRAM KONVERSI SATUAN PANJANG
Created By : M. Iqbal
"""


class LengthConverter:
    def __init__(self, val):
        self.__nilai = val

    def miltomil(self):
        return self.__nilai

    def miltokm(self):
        return self.__nilai * 1.60934

    def miltom(self):
        return self.__nilai * 1609.33999997549

    def miltoyard(self):
        return self.__nilai * 1759.9956255200022497

    def yardtoyard(self):
        return self.__nilai

    def yardtomil(self):
        return self.__nilai * 0.00056818040596590970413

    def yardtokm(self):
        return self.__nilai * 0.00091439772725880098542

    def yardtom(self):
        return self.__nilai * 0.91439772725880097415

    def kmtokm(self):
        return self.__nilai

    def kmtomil(self):
        return self.__nilai * 0.62136964781923631485

    def kmtom(self):
        return self.__nilai * 999.99751450000110253

    def kmtoyard(self):
        return self.__nilai * 1093.6105801618559781

    def mtom(self):
        return self.__nilai

    def mtomil(self):
        return self.__nilai * 0.00062136964781923627668

    def mtokm(self):
        return self.__nilai * 0.00099999751450000106193

    def mtoyard(self):
        return self.__nilai * 1.0936105801618558608
