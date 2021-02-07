class Birey:
    def __init__(self,isim:str,soyisim:str,tcno:int):
        self.isim = isim
        self.soyisim= soyisim
        self.tcno =tcno
        
class Calısmayan(Birey):
    pass


class Calısan(Birey):
    def __init__(self, isim:str, soyisim:str, tcno:int, idno:int, maas:int):
        Birey.__init__(self, isim, soyisim, tcno)
        self.idno = idno
        self.maas = maas
        
    def zam(self,deger):
        self.maas += deger
        
class Muhendis(Calısan):
    def __init__(self, isim:str, soyisim:str, tcno:int, idno:int, maas:int,yazılım_dilleri:tuple, yabancı_diller:tuple, bilinen_programlar:tuple):
        Calısan.__init__(self, isim, soyisim, tcno, idno, maas)
        self.yazılımDilleri =yazılım_dilleri
        self.yabancıDiller= yabancı_diller
        self.bilinenProgramlar= bilinen_programlar
        
    


class Muhasebeci(Calısan):
    def __init__(self, isim:str, soyisim:str, tcno:int, idno:int, maas:int, bilinen_programlar:tuple):
        Calısan.__init__(self, isim, soyisim, tcno, idno, maas) 
        self.bilinenProgramlar = bilinen_programlar
    
    
x = Muhendis("ilhan", "ödün", 123456, 65432, 7000, ("c","c++","python",), ("ingilizce",), ("MS OFFİCE",))


y = Muhasebeci("sevim", "gok", 123456, 87654, 4000, ("CNR",))

print(x.maas)
x.zam(500)
print(x.maas)
        
    