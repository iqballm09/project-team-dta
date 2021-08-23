# Program Konversi Satuan Bilangan
# Pengaturan Input diatur dalam program utama apakah string/int
class NumberSysConverter:
    def __init__(self):
        self.__input = 0

    def destodes(self, val):
        self.__input = val
        return self.__input

    def hextohex(self, val):
        self.__input = val
        return self.__input

    def octtooct(self, val):
        self.__input = val
        return self.__input

    def bintobin(self, val):
        self.__input = val
        return self.__input

    # Fungsi Desimal To Biner
    def destobin(self, val):
        self.__input = val
        self.__hasil = "{0:b}".format(int(self.__input))
        return self.__hasil

    # Fungsi Desimal To Octal
    def destookt(self, val):
        self.__input = val
        self.__hasil = 0
        self.__count = 1
        while (self.__input != 0):
            self.__remainder = self.__input % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__input //= 8
        return self.__hasil

    # Fungsi Desimal To Heksadesimal
    def destohex(self, val):
        self.__input = val
        self.__hasil = "{0:X}".format(int(self.__input))
        return self.__hasil

    # Fungsi Biner To Desimal
    def bintodes(self, val):
        self.__input = val
        self.__hasil = int(str(self.__input), 2)
        return self.__hasil

    # Fungsi Biner To Octal
    def bintooct(self, val):
        self.__input = val
        self.__sementara = int(str(self.__input), 2)
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
        self.__input = val
        self.__sementara = int(str(self.__input), 2)
        self.__hasil = "{0:X}".format(int(self.__sementara))
        return self.__hasil

    # Fungsi Hexadesimal To Desimal
    def hextodes(self, val):
        self.__input = val
        self.__hasil = int(str(self.__input), 16)
        return self.__hasil

    # Fungsi Hexadesimal To Biner
    def hextobin(self, val):
        self.__input = val
        self.__sementara = int(str(self.__input), 16)
        self.__hasil = "{0:b}".format(int(self.__sementara))
        return self.__hasil

    # Fungsi Hexadesimal To Octal
    def hextooct(self, val):
        self.__input = val
        self.__sementara = int(str(self.__input), 16)
        self.__hasil = 0
        self.__count = 1
        while (self.__sementara != 0):
            self.__remainder = self.__sementara % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__sementara //= 8
        return self.__hasil

    # Fungsi Octal To Decimal
    def octtodec(self, val):
        self.__input = val
        return int(self.__input, 8)

    # Fungsi Octal To Biner
    def octtobin(self, val):
        self.__input = val
        self.__sementara = int(self.__input, 8)
        self.__hasil = bin(self.__sementara)
        return self.__hasil[2:]

    # Fungsi Octal To Heksadesimal
    def octtohex(self, val):
        self.__input = val
        self.__sementara = int(self.__input, 8)
        self.__hasil = "{0:X}".format(int(self.__sementara))
        return self.__hasil

    def selectFunc(self, val, key):
        if key == "DecimalDecimal":
            result = self.destodes(val)
        elif key == "DecimalBinary":
            result = self.destobin(val)
        elif key == "DecimalOctal":
            result = self.destookt(val)
        elif key == "DecimalHexa":
            result = self.destohex(val)
        elif key == "BinaryDecimal":
            result = self.bintodes(val)
        elif key == "BinaryBinary":
            result = self.bintobin(val)
        elif key == "BinaryOctal":
            result = self.bintooct(val)
        elif key == "BinaryHexa":
            result = self.bintohex(val)
        elif key == "HexaDecimal":
            result = self.hextodes(val)
        elif key == "HexaBinary":
            result = self.hextobin(val)
        elif key == "HexaOctal":
            result = self.hextooct(val)
        elif key == "HexaHexa":
            result = self.hextohex(val)
        elif key == "OctalOctal":
            result = self.octtooct(val)
        elif key == "OctalBinary":
            result = self.octtobin(val)
        elif key == "OctalDecimal":
            result = self.octtodec(val)
        elif key == "OctalHexa":
            result = self.octtohex(val)
        return result
# #Ini Program Uji Coba Bisa Diabaikan
# obj = konvbilangan('1010')
# obj_aa = obj.bintobin()
# print(obj_aa)
