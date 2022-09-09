class Zvire():


    def __init__(self, nazev, jmeno, vek, zuby):
        self.__nazev = nazev
        self.__jmeno = jmeno
        self.vek = vek
        self.zuby = zuby

    def get_jmeno(self):
        return self.__jmeno

    def get_nazev(self):
        return self.__nazev

    def printni(self):
        print ("Zvire: {self.__nazev} jmenem {self.__jmeno} je:{self.vek} roku stare a ma akrualne {self.zuby} zubu.")




if __name__ == '__main__':
    zvire1 = Zvire("opice" , "pavel", 8, 20)
    zvire2 = Zvire("medved", "Ota", 16, 28)
    zvire1.printni()
    zvire2.printni()



