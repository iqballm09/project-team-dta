"""
PRORAM KONVERSI SATUAN DATA
Created By : Muhammad Rizki
"""


class ByteConverter:
    def __init__(self, val):
        self.__input = val

    # Fungsi GB to GB
    def gigatogiga(self):
        return self.__input

    # Fungsi GB TO MB
    def gigatomega(self):
        return self.__input*1024

    # Fungsi GB TO KB
    def gigatokilo(self):
        return self.__input*1024*10**3

    # Fungsi GB TO BYTE
    def gigatobyte(self):
        return self.__input*1024*10**6

    # Fungsi MB TO GB
    def megatogiga(self):
        return self.__input/1024

    # Fungsi MB TO MB
    def megatomega(self):
        return self.__input

    # Fungsi MB TO KB
    def megatokilo(self):
        return self.__input*1024

    # Fungsi MB TO BYTE
    def megatobyte(self):
        return self.__input*1024*10**3

    # Fungsi KB TO GB
    def kilotogiga(self):
        return self.__input/(1024*10**3)

    # Fungsi KB TO MB
    def kilotomega(self):
        return self.__input/1024

    # Fungsi KB TO KB
    def kilotokilo(self):
        return self.__input

    # Fungsi KB TO BYTE
    def kilotobyte(self):
        return self.__input*1024

    # Fungsi BYTE TO GB
    def bytetogiga(self):
        return self.__input/(1024*10**6)

    # Fungsi BYTE TO MB
    def bytetomega(self):
        return self.__input/(1024*10**3)

    # Fungsi BYTE TO KB
    def bytetokilo(self):
        return self.__input/1024

    def bytetobyte(self):
        return self.__input

# PROGRAM COBA UJI DATA INIMAH BISA DIABAIKAN
#print("Konversi Megabyte ke KiloByte")
#obj = konversi(32.5)
#obj_aa = obj.megatokilo()
#print("32.5 MB = ",obj_aa," KB")
