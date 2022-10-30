
class calisan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyet = []
        self. personel_ekle()
    
    def personel_ekle(self):
        self.personel.append(self.isim)
        print('{} adli kisi personele eklendi'.format(self.isim))

    def personel_gor(self):
        print(' Personel Listesi:')
        for kisi in self.personel:
            print('kisi')
    
    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyet.append(kabiliyet)
    def kabiliyet_gor(self):
        print('{} adli kisinin kaibliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyet:
            print(kabiliyet)
    
def main():
    worker1 = calisan('selim')
    worker1.kabiliyet_ekle('xxx')
    worker1.personel_gor()
    worker1.kabiliyet_gor()

if __name__ == '__main__':
    main()
