# CLASS DAN OBJECT

class Kantor:
    def __init__(self):
        self.nama = ""

class Karyawan:
    # Class Attribute
    perusahaan = "PT Jaya Abadi"

    # Constructor karyawan
    def __init__(self, nama, jabatan, kantor):
        self.nama = nama
        self.jabatan = jabatan
        self.kantor = kantor

    # Method percakapan antara atasan dan karyawan
    def percakapan(self, lawan_bicara):
        print("\\n===== PERCAKAPAN DI KANTOR =====")

        print(f"{self.nama}: Selamat pagi, {lawan_bicara.nama}.")
        print(f"{lawan_bicara.nama}: Selamat pagi, Pak {self.nama}.")

        print(f"{self.nama}: Bagaimana pekerjaan kamu hari ini?")
        print(f"{lawan_bicara.nama}: Baik, Pak. Pekerjaan sedang saya selesaikan.")

        print(f"{self.nama}: Apakah ada kendala dalam pekerjaan?")
        print(f"{lawan_bicara.nama}: Ada sedikit kendala, Pak, tetapi sedang saya atasi.")

        print(f"{self.nama}: Baik, jika ada kesulitan, jangan ragu untuk bertanya.")
        print(f"{lawan_bicara.nama}: Baik, Pak. Terima kasih atas arahannya.")

        print(f"{self.nama}: Tolong selesaikan tugas tersebut tepat waktu.")
        print(f"{lawan_bicara.nama}: Siap, Pak. Saya akan menyelesaikannya dengan baik.")

        print(f"{self.nama}: Bagus. Semoga kita bisa mencapai target perusahaan.")
        print(f"{lawan_bicara.nama}: Siap, Pak. Saya akan berusaha semaksimal mungkin.")

# Membuat object kantor
kantor1 = Kantor()

# Membuat object karyawan pertama (Atasan)
karyawan1 = Karyawan(
    "Khoirul", "Supervisor", kantor1.nama,
)
# Membuat object karyawan kedua
karyawan2 = Karyawan(
    "Teuku", "Operator Produksi", kantor1.nama,
)
# Percakapan antara atasan dan karyawan
karyawan1.percakapan(karyawan2)
