# data penyakit dan gejalanya
rules_penyakit = {
    "Diare Infeksi" : {"G1", "G2", "G3", "G4"},
    "Keracunan Makanan" : {"G1", "G2", "G5", "G6"},
    "Intoleransi Laktosa" : {"G1", "G7", "G8", "G9"},
    "Irritable Bowel Syndrome (IBS)" : {"G1", "G3", "G7", "G10"},
    "Gastroenteritis (Flu Perut)" : {"G1", "G2", "G3", "G11"}
}

# kode gejala
list_gejala = {
    "G1" : "BAB cair",
    "G2" : "Mual atau muntah",
    "G3" : "Demam",
    "G4" : "Diare lebih dari 3 hari",
    "G5" : "Gejala muncul cepat setelah makan",
    "G6" : "Makan makanan yang mencurigakan",
    "G7" : "Perut kembung",
    "G8" : "Sering buang gas",
    "G9" : "Gejala setelah minum susu",
    "G10" : "Gejala dipicu stres atau kambuhan",
    "G11" : "Badan lemas"
}

gejala = []

def tanya_gejala(kode_gejala, nama_gejala):
    while True:
        jawaban = input(f"Apakah anda mengalami {nama_gejala}? (y/t): ").lower()
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