class Ovqat:
    def __init__(self, nomi):
        self.nomi = nomi

    def tayyorlash(self):
        print("Ovqat tayyorlandi", end="")

class Palov(Ovqat):
    def tayyorlash(self):
        super().tayyorlash()
        print(", Palov tayyorlandi")


o1 = Ovqat("Ovqat")
p1 = Palov("Palov")

o1.tayyorlash()
p1.tayyorlash()


class Haydovchi:
    def __init__(self, ism):
        self.ism = ism

    def haydash(self):
        print("Haydayapti", end="")

class TaksiHaydovchi(Haydovchi):
    def haydash(self):
        super().haydash()
        print(", Yo‘lovchi tashimoqda")


h1 = Haydovchi("Ali")
t1 = TaksiHaydovchi("Vali")

h1.haydash()
t1.haydash()
