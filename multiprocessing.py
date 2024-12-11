import multiprocessing
import os

def faktoriyel_hesapla(n):
    if n <= 1:
        return 1
    return n * faktoriyel_hesapla(n - 1)

def Islemi_Goster(sayilar):
    sayi = faktoriyel_hesapla(sayilar)
    print(f"Islem Kimligi (PID): {os.getpid()} - Sayi: {sayilar}, Faktoriyeli: {sayi}")

if __name__ == "__main__":
    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    for sayi in sayilar:
        p = multiprocessing.Process(target=Islemi_Goster, args=(sayi,))
        islemler.append(p)
        p.start()
    
    for p in islemler:
        p.join()
