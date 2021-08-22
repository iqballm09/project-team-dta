# Program Konversi Massa
"""
PROGRAM KONVERSI SATUAN MASSA
Created By : Nurul Azizah
"""


class MassConverter:
    def __init__(self, val):
        self.__nilai = val

    def tontoton(self):
        return self.__nilai

    def tontokwintal(self):
        return self.__nilai * 10

    def tontokg(self):
        return self.__nilai * 1000

    def tontoons(self):
        return self.__nilai * 35274

    def tontog(self):
        return self.__nilai * 1E+6

    def kwintaltoton(self):
        return self.__nilai / 10

    def kwintaltokwintal(self):
        return self.__nilai

    def kwintaltokg(self):
        return self.__nilai * 100

    def kwintaltoons(self):
        return self.__nilai * 3527

    def kwintaltog(self):
        return self.__nilai * 100000

    def kgtoton(self):
        return self.__nilai / 1000

    def kgtokwintal(self):
        return self.__nilai / 100

    def kgtokg(self):
        return self.__nilai

    def kgtoons(self):
        return self.__nilai * 35.274

    def kgtog(self):
        return self.__nilai * 1000

    def onstoton(self):
        return self.__nilai / 35274

    def onskwintal(self):
        return self.__nilai / 3527

    def onstokg(self):
        return self.__nilai / 35, 274

    def onstoons(self):
        return self.__nilai

    def onstog(self):
        return self.__nilai * 28.35

    def gtoton(self):
        return self.__nilai / 1E+6

    def gtokwintal(self):
        return self.__nilai / 1E+5

    def gtokg(self):
        return self.__nilai / 1000

    def gtoons(self):
        return self.__nilai / 28.35

    def gtog(self):
        return self.__nilai


# method_list = [func for func in dir(MassConverter)
#                if callable(getattr(MassConverter, func)) and
#                not func.startswith("__")]
# print(method_list)
