from multiprocessing import Process
import threading
import time

def faktoriyel_hesapla(n):
    if n <= 1:
        return 1
    return n * faktoriyel_hesapla(n - 1)

def faktoriyel_hesaplama(sayi):
    sonuc = faktoriyel_hesapla(sayi)
    print(f"Hesaplaniyor (Thread ID: {threading.get_ident()}): {sayi}! -> {sonuc}")
    time.sleep(1)

def kare_hesaplama(sayi):
    print(f"Hesaplaniyor (Process ID: {threading.get_ident()}): {sayi} -> {sayi * sayi}")
    time.sleep(1)

def coklu_programlama():
    sayilar = [1, 2, 3, 4, 5, 6]
    print("Coklu Programlama Başladi (Thread)...\n")
    
    thread_list = []
    for sayi in sayilar:
        t = threading.Thread(target=faktoriyel_hesaplama, args=(sayi,))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()
    
    print("\nCoklu Programlama Tamamlandi")

def coklu_islemci():
    sayilar = [1, 2, 3, 4, 5, 6]
    print("Coklu islemci Basladi (Process)...\n")
    
    process_list = []
    for sayi in sayilar:
        islem = Process(target=kare_hesaplama, args=(sayi,))
        process_list.append(islem)
        islem.start()

    for islem in process_list:
        islem.join()
    
    print("\nCoklu islemci Tamamlandi")

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()
