import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. DEFINISI ANTECEDENT (GEJALA / INPUT)

# G1: BAB Cair (0 - 15 kali/hari)
g1_bab = ctrl.Antecedent(np.arange(0, 16, 1), 'G1')
g1_bab['normal'] = fuzz.trimf(g1_bab.universe, [0, 1, 3])
g1_bab['sering'] = fuzz.trimf(g1_bab.universe, [2, 4, 6])
g1_bab['sangat_sering'] = fuzz.trapmf(g1_bab.universe, [5, 7, 15, 15])

# G3: Demam (36.0 - 41.0 °C)
g3_demam = ctrl.Antecedent(np.arange(36, 41.1, 0.1), 'G3')
g3_demam['normal'] = fuzz.trimf(g3_demam.universe, [36.0, 36.5, 37.5])
g3_demam['sumeng'] = fuzz.trimf(g3_demam.universe, [37.0, 38.0, 39.0])
g3_demam['tinggi'] = fuzz.trapmf(g3_demam.universe, [38.5, 39.5, 41.0, 41.0])

# G4: Diare > 3 hari (0 - 14 hari)
g4_hari = ctrl.Antecedent(np.arange(0, 15, 1), 'G4')
g4_hari['baru'] = fuzz.trimf(g4_hari.universe, [0, 1, 3])
g4_hari['sedang'] = fuzz.trimf(g4_hari.universe, [2, 4, 6])
g4_hari['lama'] = fuzz.trapmf(g4_hari.universe, [5, 7, 14, 14])

# G8: Sering buang gas (0 - 20 kali/hari)
g8_gas = ctrl.Antecedent(np.arange(0, 21, 1), 'G8')
g8_gas['normal'] = fuzz.trimf(g8_gas.universe, [0, 3, 7])
g8_gas['sering'] = fuzz.trapmf(g8_gas.universe, [6, 10, 20, 20])

# Gejala lain menggunakan Skala Keparahan/Keyakinan 0 - 10
# (0 = Tidak sama sekali, 10 = Sangat Parah / Sangat Yakin)
skala_gejala = {
    'G2': 'Mual/Muntah',
    'G5': 'Gejala pasca makan',
    'G6': 'Makan makanan mencurigakan',
    'G7': 'Perut kembung',
    'G9': 'Gejala pasca minum susu',
    'G10': 'Stres',
    'G11': 'Badan lemas'
}

# Membuat Antecedent otomatis untuk gejala berskala 0-10
gejala_skala = {}
for kode in skala_gejala.keys():
    var = ctrl.Antecedent(np.arange(0, 11, 1), kode)
    var['rendah'] = fuzz.trimf(var.universe, [0, 0, 4])
    var['sedang'] = fuzz.trimf(var.universe, [3, 5, 7])
    var['tinggi'] = fuzz.trapmf(var.universe, [6, 8, 10, 10])
    gejala_skala[kode] = var

# 2. DEFINISI CONSEQUENT (PENYAKIT / OUTPUT)

nama_penyakit = [
    "Diare_Infeksi", "Keracunan_Makanan", "Intoleransi_Laktosa", 
    "IBS", "Gastroenteritis"
]

output_penyakit = {}
for nama in nama_penyakit:
    out = ctrl.Consequent(np.arange(0, 101, 1), nama)
    out['rendah'] = fuzz.trimf(out.universe, [0, 0, 50])
    out['sedang'] = fuzz.trimf(out.universe, [25, 50, 75])
    out['tinggi'] = fuzz.trimf(out.universe, [50, 100, 100])
    output_penyakit[nama] = out

# 3. MEMBUAT FUZZY RULES (ATURAN PAKAR)

rules = []

# 1. Diare Infeksi (G1, G2, G3, G4)
rules.append(ctrl.Rule(g1_bab['sangat_sering'] & gejala_skala['G2']['tinggi'] & g3_demam['tinggi'] & g4_hari['lama'], output_penyakit['Diare_Infeksi']['tinggi']))
rules.append(ctrl.Rule(g1_bab['sering'] & g3_demam['sumeng'], output_penyakit['Diare_Infeksi']['sedang']))

# 2. Keracunan Makanan (G1, G2, G5, G6)
rules.append(ctrl.Rule(g1_bab['sangat_sering'] & gejala_skala['G2']['tinggi'] & gejala_skala['G5']['tinggi'] & gejala_skala['G6']['tinggi'], output_penyakit['Keracunan_Makanan']['tinggi']))
rules.append(ctrl.Rule(gejala_skala['G5']['tinggi'] & gejala_skala['G6']['tinggi'], output_penyakit['Keracunan_Makanan']['sedang']))

# 3. Intoleransi Laktosa (G1, G7, G8, G9)
rules.append(ctrl.Rule(g1_bab['sering'] & gejala_skala['G7']['tinggi'] & g8_gas['sering'] & gejala_skala['G9']['tinggi'], output_penyakit['Intoleransi_Laktosa']['tinggi']))
rules.append(ctrl.Rule(gejala_skala['G7']['sedang'] & gejala_skala['G9']['tinggi'], output_penyakit['Intoleransi_Laktosa']['sedang']))

# 4. Irritable Bowel Syndrome / IBS (G1, G3, G7, G10)
rules.append(ctrl.Rule(g1_bab['sering'] & g3_demam['normal'] & gejala_skala['G7']['tinggi'] & gejala_skala['G10']['tinggi'], output_penyakit['IBS']['tinggi']))
rules.append(ctrl.Rule(g1_bab['sering'] & gejala_skala['G10']['sedang'], output_penyakit['IBS']['sedang']))

# 5. Gastroenteritis (G1, G2, G3, G11)
rules.append(ctrl.Rule(g1_bab['sangat_sering'] & gejala_skala['G2']['tinggi'] & g3_demam['sumeng'] & gejala_skala['G11']['tinggi'], output_penyakit['Gastroenteritis']['tinggi']))
rules.append(ctrl.Rule(g1_bab['sering'] & gejala_skala['G11']['sedang'], output_penyakit['Gastroenteritis']['sedang']))

# 4. SISTEM KONTROL & INPUT PENGGUNA

sistem_diagnosa = ctrl.ControlSystem(rules)
simulasi = ctrl.ControlSystemSimulation(sistem_diagnosa)

print("=== SISTEM DIAGNOSA GANGGUAN PENCERNAAN ===")
print("Jawablah pertanyaan berikut dengan angka yang sesuai.\n")

def minta_input(pesan, min_val, max_val):
    while True:
        try:
            nilai = float(input(f"{pesan} ({min_val}-{max_val}): "))
            if min_val <= nilai <= max_val:
                return nilai
            else:
                print(f"Harap masukkan angka antara {min_val} dan {max_val}.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

# Meminta input ke pengguna
input_data = {}
input_data['G1'] = minta_input("1. Berapa kali Anda BAB cair hari ini?", 0, 15)
input_data['G2'] = minta_input("2. Seberapa parah mual/muntah Anda? (Skala 0-10)", 0, 10)
input_data['G3'] = minta_input("3. Berapa suhu tubuh Anda saat ini? (Celcius)", 36.0, 41.0)
input_data['G4'] = minta_input("4. Sudah berapa hari Anda mengalami diare?", 0, 14)
input_data['G5'] = minta_input("5. Seberapa parah gejala muncul setelah makan? (Skala 0-10)", 0, 10)
input_data['G6'] = minta_input("6. Seberapa yakin Anda baru saja makan makanan mencurigakan? (Skala 0-10)", 0, 10)
input_data['G7'] = minta_input("7. Seberapa parah perut kembung Anda? (Skala 0-10)", 0, 10)
input_data['G8'] = minta_input("8. Berapa kali Anda buang gas hari ini?", 0, 20)
input_data['G9'] = minta_input("9. Seberapa yakin gejala muncul setelah minum/makan olahan susu? (Skala 0-10)", 0, 10)
input_data['G10'] = minta_input("10. Seberapa stres Anda saat ini? (Skala 0-10)", 0, 10)
input_data['G11'] = minta_input("11. Seberapa lemas badan Anda? (Skala 0-10)", 0, 10)

# Memasukkan data ke dalam simulasi
for kunci, nilai in input_data.items():
    simulasi.input[kunci] = nilai

# 5. PERHITUNGAN & HASIL DIAGNOSA

print("\nMemproses diagnosa...\n")
try:
    simulasi.compute()
    
    hasil_diagnosa = []
    for penyakit in nama_penyakit:
        # Menyimpan hasil perhitungan (jika aturan untuk penyakit tersebut terpicu)
        persentase = simulasi.output.get(penyakit, 0) 
        hasil_diagnosa.append((penyakit.replace("_", " "), persentase))
    
    # Mengurutkan berdasarkan persentase terbesar
    hasil_diagnosa.sort(key=lambda x: x[1], reverse=True)
    
    print("=== HASIL DIAGNOSA ===")
    for penyakit, persen in hasil_diagnosa[:3]:
        if persen > 0:
            print(f"- {penyakit}: {persen:.2f}%")
            
except ValueError:
    # ValueError terjadi jika tidak ada satupun rule yang cocok (misal semua input bernilai 0 / sangat normal)
    print("=== HASIL DIAGNOSA ===")
    print("Gejala terlalu ringan atau tidak ada aturan pakar yang cocok dengan kombinasi gejala Anda.")