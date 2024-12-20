from metaflow import FlowSpec, step

class KuliahFlow(FlowSpec):

    @step
    def start(self):
        print("=== Proses Mengikuti Kuliah di Informatika ===\n")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        print("1. Membayar SPP...")
        print("   SPP telah dibayar!\n")
        self.next(self.registrasi_mata_kuliah)

    @step
    def registrasi_mata_kuliah(self):
        print("2. Registrasi mata kuliah...")
        self.mata_kuliah = ["Algoritma dan Pemrograman", "Matematika Diskret", "Basis Data"]
        print(f"   Anda telah terdaftar dalam mata kuliah: {', '.join(self.mata_kuliah)}\n")
        self.next(self.mengikuti_perkuliahan)

    @step
    def mengikuti_perkuliahan(self):
        print("3. Mengikuti perkuliahan...")
        for mk in self.mata_kuliah:
            print(f"   Menghadiri kuliah {mk}...")
        print("   Semua perkuliahan telah diikuti!\n")
        self.next(self.mengerjakan_tugas_ujian)

    @step
    def mengerjakan_tugas_ujian(self):
        print("4. Mengerjakan tugas dan ujian...")
        print("   Tugas dan ujian selesai dikerjakan!\n")
        self.next(self.mendapatkan_nilai)

    @step
    def mendapatkan_nilai(self):
        print("5. Mendapatkan nilai akhir...")
        self.nilai = {
            "Algoritma dan Pemrograman": 85,
            "Matematika Diskret": 78,
            "Basis Data": 90
        }
        print("   Nilai akhir:")
        for mk, n in self.nilai.items():
            print(f"   {mk}: {n}")
        print("\n   Proses kuliah selesai!\n")

if __name__ == '__main__':
    KuliahFlow()
