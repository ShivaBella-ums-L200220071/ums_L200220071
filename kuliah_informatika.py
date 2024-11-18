def bayar_spp():
    print("1. Membayar SPP...")
    print("   SPP telah dibayar!\n")

def registrasi_mata_kuliah():
    print("2. Registrasi mata kuliah...")
    mata_kuliah = ["Algoritma dan Pemrograman", "Matematika Diskret", "Basis Data"]
    print(f"   Anda telah terdaftar dalam mata kuliah: {', '.join(mata_kuliah)}\n")
    return mata_kuliah

def mengikuti_perkuliahan(mata_kuliah):
    print("3. Mengikuti perkuliahan...")
    for mk in mata_kuliah:
        print(f"   Menghadiri kuliah {mk}...")
    print("   Semua perkuliahan telah diikuti!\n")

def mengerjakan_tugas_ujian():
    print("4. Mengerjakan tugas dan ujian...")
    print("   Tugas dan ujian selesai dikerjakan!\n")

def mendapatkan_nilai():
    print("5. Mendapatkan nilai akhir...")
    nilai = {
        "Algoritma dan Pemrograman": 85,
        "Matematika Diskret": 78,
        "Basis Data": 90
    }
    print("   Nilai akhir:")
    for mk, n in nilai.items():
        print(f"   {mk}: {n}")
    print("\n   Proses kuliah selesai!\n")

def main():
    print("=== Proses Mengikuti Kuliah di Informatika ===\n")
    bayar_spp()
    mata_kuliah = registrasi_mata_kuliah()
    mengikuti_perkuliahan(mata_kuliah)
    mengerjakan_tugas_ujian()
    mendapatkan_nilai()

if __name__ == "__main__":
    main()
