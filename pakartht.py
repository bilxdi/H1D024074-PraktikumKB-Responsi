# data penyakit dan gejalanya
rules_penyakit = {
    "Diare Infeksi" : {"G1", "G2", "G3", "G4"},
    "Keracunan Makanan" : {"G1", "G2", "G5", "G6"},
    "Intoleransi Laktosa" : {"G1", "G7", "G8", "G9"},
    "Irritable Bowel Syndrome" : {"G1", "G3", "G7", "G10"},
    "Gastroenteritis" : {"G1", "G2", "G3", "G11"}
}

# kode gejala
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
    "G11" : "mengalami badan lemas"
}

gejala = []

def tanya_gejala(kode_gejala, detail_gejala):
    while True:
        jawaban = input(f"Apakah anda {detail_gejala}? (y/t): ").lower()
        if jawaban in ['y', 't']:
            break
        else:
            print("Input tidak valid! Harap masukkan 'y' atau 't'\n")

    if jawaban == 'y':
        gejala.append(kode_gejala)

def diagnosa_gejala(input_gejala):
    hasil_diagnosa = []

    for penyakit, syarat in rules_penyakit.items():
        cocok = len(syarat.intersection(input_gejala))
        total = len(syarat)
        persentase = (cocok / total) * 100
        hasil_diagnosa.append((penyakit, persentase))

    hasil_diagnosa.sort(key=lambda x: x[1], reverse=True)
    return hasil_diagnosa

print("=== SISTEM DIAGNOSA GANGGUAN PENCERNAAN ===")
print("Jawablah dengan 'y' atau 't'\n")

for kode, nama in list_gejala.items():
    tanya_gejala(kode, nama)

if not gejala:
    print("\nTidak ada gejala dipilih.")
else:
    hasil = diagnosa_gejala(gejala)

    print("\nHasil Diagnosa:")
    for penyakit, persen in hasil[:3]:
        if persen >= 25:
            print(f"- {penyakit}: {persen:.2f}%")