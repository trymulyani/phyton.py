def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class Baru():
    minimum = 10000000
    maximum = 15000000

    def Turun(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def naik(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)

class Sedang():
    minimum = 20000000
    maximum = 30000000

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x<= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x >= self.maximum:
            return 1
        elif x<= self.minimum:
            return 0
        else:
            return up(x, self.minimum, self.maximum)


class Lama():
    minimum = 40000000
    maximum = 60000000

    def _berkurang(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _bertambah(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(self, pmt=lama(), psd=Baru()):
        result = []
        # [R1] JIKA Lama TURUN, dan baru  BANYAK, MAKA
        # Penghasilan BERKURANG.
        a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        z1 = self._berkurang(a1)
        result.append((a1, z1))
        # [R2] JIKA Lama TURUN, dan Sedang SEDIKIT, MAKA
        # Penghasilan BERKURANG.
        a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        z2 = self._berkurang(a2)
        result.append((a2, z2))
        # [R3] JIKA sedang NAIK, dan Lama BANYAK, MAKA
        # Penghasilan BERTAMBAH.
        a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        z3 = self._bertambah(a3)
        result.append((a3, z3))
        # [R4] JIKA Lama NAIK, dan baru SEDIKIT, MAKA
        # Penghasilan BERTAMBAH.
        a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        z4 = self._bertambah(a4)
        result.append((a4, z4))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a
Footer
