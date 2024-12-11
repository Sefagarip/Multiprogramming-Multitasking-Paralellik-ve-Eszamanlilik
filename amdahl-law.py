import matplotlib.pyplot as plt

def amdalh_hizlanma_seri(seri_oran, cekirdek_sayisi):
    paralel_oran = 1 - seri_oran
    hizlanma = 1 / (seri_oran + (paralel_oran / cekirdek_sayisi))
    return hizlanma

def hizlanma_grafik_seri(seri_oran):
    cekirdek_sayilari = range(1, 17)
    hizlanmalar = [amdalh_hizlanma_seri(seri_oran, cekirdek) for cekirdek in cekirdek_sayilari]

    plt.figure(figsize=(10, 6))
    plt.plot(cekirdek_sayilari, hizlanmalar, marker='o', label=f'Seri Oran: {seri_oran}')
    plt.title('Amdahl Yasası: Çekirdek Sayısına Göre Hızlanma')
    plt.xlabel('Çekirdek Sayısı')
    plt.ylabel('Hızlanma (Speedup)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    seri_oran = 0.25
    print("Amdahl Yasası ile hızlanma hesaplama (Seri Oran üzerinden):\n")
    print(f"Seri Kısım Oranı: {seri_oran}")
    print(f"{'Çekirdek Sayısı':<15}{'Hızlanma':<10}")
    print("-" * 25)
    for cekirdek in range(1, 17):
        hizlanma = amdalh_hizlanma_seri(seri_oran, cekirdek)
        print(f"{cekirdek:<15}{hizlanma:.2f}")

    hizlanma_grafik_seri(seri_oran)
