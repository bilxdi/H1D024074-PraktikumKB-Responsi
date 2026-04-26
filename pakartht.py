# Data penyakit dan gejala (lebih lengkap)
rules_penyakit = {
    "Diare Infeksi (Bakteri/Virus)" : {"G1", "G2", "G3", "G4"},
    "Keracunan Makanan" : {"G1", "G2", "G5", "G6"},
    "Intoleransi Laktosa" : {"G1", "G7", "G8", "G9"},
    "Irritable Bowel Syndrome (IBS)" : {"G1", "G3", "G7", "G10"},
    "Gastroenteritis" : {"G1", "G2", "G3", "G11"},
    "Celiac (Intoleransi Gluten)" : {"G1", "G7", "G12", "G13"},
    "Inflammatory Bowel Disease (IBD)" : {"G1", "G3", "G14", "G15"},
    "Infeksi Parasit" : {"G1", "G7", "G16"},
    "Efek samping obat" : {"G1", "G2", "G7", "G17"}
}

# Kode gejala
list_gejala = {
    "G1" : "mengalami BAB cair",
    "G2" : "mengalami Mual atau muntah",
    "G3" : "mengalami Demam",
    "G4" : "mengalami Diare lebih dari 3 hari",
    "G5" : "mengalami gejala yang muncul setelah makan",
    "G6" : "makan makanan yang mencurigakan",
    "G7" : "mengalami perut kembung",
    "G8" : "sering buang gas",
    "G9" : "mengalami gejala setelah konsumsi olahan susu",
    "G10" : "sedang Stres",
    "G11" : "mengalami badan lemas",
    "G12" : "mengalami tinja berminyak atau penurunan berat badan",
    "G13" : "mengalami kelelahan atau anemia",
    "G14" : "mengalami diare berdarah",
    "G15" : "nyeri perut berkepanjangan",
    "G16" : "penurunan berat badan perlahan",
    "G17" : "mengalami diare setelah minum obat"
}

gejala = []

# Fungsi menanyakan gejala
def tanya_gejala(kode_gejala, detail_gejala):
    while True:
        jawaban = input(f"Apakah anda {detail_gejala}? (y/t): ").lower()
        if jawaban in ['y', 't']:
            break
        else:
            print("Input tidak valid! Harap masukkan 'y' atau 't'\n")

    if jawaban == 'y':
        gejala.append(kode_gejala)

# Fungsi diagnosa berdasarkan gejala
def diagnosa_gejala(input_gejala):
    hasil_diagnosa = []

    for penyakit, syarat in rules_penyakit.items():
        cocok = len(syarat.intersection(input_gejala))
        total = len(syarat)
        persentase = (cocok / total) * 100
        hasil_diagnosa.append((penyakit, persentase))

    hasil_diagnosa.sort(key=lambda x: x[1], reverse=True)
    return hasil_diagnosa

# Program utama
print("=== SISTEM DIAGNOSA GANGGUAN PENCERNAAN ===")
print("Jawablah dengan 'y' atau 't'\n")

for kode, nama in list_gejala.items():
    tanya_gejala(kode, nama)

if not gejala:
    print("\nTidak ada gejala dipilih.")
else:
    hasil = diagnosa_gejala(gejala)

    print("\nHasil Diagnosa (top 3 kemungkinan):")
    for penyakit, persen in hasil[:3]:
        if persen >= 25:
            print(f"- {penyakit}: {persen:.2f}%")