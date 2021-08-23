#Program Konversi Satuan Bilangan
#Pengaturan Input diatur dalam program utama apakah string/int 
class konvbilangan:
    def __init__(self,val):
        self.__input = val
    
    def destodes(self):
        return self.__input
    
    def hextohex(self):
        return self.__input
    
    def octtooct(self):
        return self.__input
    
    def bintobin(self):
        return self.__input

    #Fungsi Desimal To Biner
    def destobin(self):
        self.__hasil = "{0:b}".format(int(self.__input))
        return self.__hasil

    #Fungsi Desimal To Octal
    def destookt(self):
        self.__hasil = 0
        self.__count = 1
        while (self.__input!=0):
            self.__remainder = self.__input % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__input //= 8
        return self.__hasil

    #Fungsi Desimal To Heksadesimal
    def destohex(self):
        self.__hasil = "{0:X}".format(int(self.__input))
        return self.__hasil

    #Fungsi Biner To Desimal
    def bintodes(self):
        self.__hasil = int(str(self.__input),2)
        return self.__hasil

    #Fungsi Biner To Octal
    def bintooct(self):
        self.__sementara = int(str(self.__input),2)
        self.__hasil = 0
        self.__count = 1
        while (self.__sementara!=0):
            self.__remainder = self.__sementara % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__sementara //= 8
        return self.__hasil
        
    #Fungsi Biner To Hexadesimal
    def bintohex(self):
        self.__sementara = int(str(self.__input),2)
        self.__hasil = "{0:X}".format(int(self.__sementara))
        return self.__hasil

    #Fungsi Hexadesimal To Desimal
    def hextodes(self):
        self.__hasil = int(str(self.__input),16)
        return self.__hasil

    #Fungsi Hexadesimal To Biner
    def hextobin(self):
        self.__sementara = int(str(self.__input),16)
        self.__hasil = "{0:b}".format(int(self.__sementara))
        return self.__hasil
        
    #Fungsi Hexadesimal To Octal
    def hextooct(self):
        self.__sementara = int(str(self.__input),16)
        self.__hasil = 0
        self.__count = 1
        while (self.__sementara!=0):
            self.__remainder = self.__sementara % 8
            self.__hasil += self.__remainder * self.__count
            self.__count *= 10
            self.__sementara //= 8
        return self.__hasil
    
    # Fungsi Octal To Decimal
    def octtodec(self):
        return int(self.__input,8)
    
    #Fungsi Octal To Biner
    def octtobin(self):
        self.__sementara = int(self.__input,8)
        self.__hasil = bin(self.__sementara)
        return self.__hasil[2:]
    
    #Fungsi Octal To Heksadesimal
    def octtohex(self):
        self.__sementara = int(self.__input,8)
        self.__hasil = "{0:X}".format(int(self.__sementara))
        return self.__hasil

# #Ini Program Uji Coba Bisa Diabaikan
# obj = konvbilangan('1010')
# obj_aa = obj.bintobin()
# print(obj_aa)

    

