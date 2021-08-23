"""
PROGRAM KONVERSI SISTEM BILANGAN 
Created by : Muhammad Rizki
"""
# Pengaturan Input diatur dalam program utama apakah string/int


class NumberSysConverter:
    def __init__(self):
        pass

    # Fungsi Desimal To Biner
    def destodes(self, val):
        return val

    def hextohex(self, val):
        return val

    def bintobin(self, val):
        return val

    def destobin(self, val):
        self.__hasil = "{0:b}".format(int(val))
        return self.__hasil

    # Fungsi Desimal To Octal
    def destookt(self, val):
        self.__hasil = 0
        self.__count = 1
        while (val != 0):
            self.__remainder = val % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            val //= 8
        return self.__hasil

    # Fungsi Desimal To Heksadesimal
    def destohex(self, val):
        self.__hasil = "{0:X}".format(int(val))
        return self.__hasil

    # Fungsi Biner To Desimal
    def bintodes(self, val):
        self.__hasil = int(str(val), 2)
        return self.__hasil

    # Fungsi Biner To Octal
    def bintooct(self, val):
        self.__sementara = int(str(val), 2)
        self.__hasil = 0
        self.__count = 1
        while (self.__sementara != 0):
            self.__remainder = self.__sementara % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__sementara //= 8
        return self.__hasil

    # Fungsi Biner To Hexadesimal
    def bintohex(self, val):
        self.__sementara = int(str(val), 2)
        self.__hasil = "{0:X}".format(int(self.__sementara))
        return self.__hasil

    # Fungsi Hexadesimal To Desimal
    def hextodes(self, val):
        self.__hasil = int(str(val), 16)
        return self.__hasil

    # Fungsi Hexadesimal To Biner
    def hextobin(self, val):
        self.__sementara = int(str(val), 16)
        self.__hasil = "{0:b}".format(int(self.__sementara))
        return self.__hasil

    # Fungsi Hexadesimal To Octal
    def hextooct(self, val):
        self.__sementara = int(str(val), 16)
        self.__hasil = 0
        self.__count = 1
        while (self.__sementara != 0):
            self.__remainder = self.__sementara % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__sementara //= 8
        return self.__hasil
