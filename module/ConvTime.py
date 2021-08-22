"""
PROGRAM KONVERSI SATUAN WAKTU
Created By : Nurul Azizah
"""


class TimeConverter:
    def __init__(self, val):
        self.__nilai = val

    def menittodetik(self):
        return self.__nilai * 60

    def detiktomenit(self):
        return self.__nilai / 60

    def jamtomenit(self):
        return self.__nilai * 60

    def menittojam(self):
        return self.__nilai / 60

    def jamtodetik(self):
        return self.__nilai * 3600

    def detiktojam(self):
        return self.__nilai / 3600

    def haritojam(self):
        return self.__nilai * 24

    def jamtohari(self):
        return self.__nilai / 24

    def haritomenit(self):
        return self.__nilai * 1440

    def menittohari(self):
        return self.__nilai / 1440

    def haritodetik(self):
        return self.__nilai * 86400

    def detiktohari(self):
        return self.__nilai / 86400
