# H1D024074-PraktikumKB-Responsi
<meta http-equiv="refresh" content="0; URL=https://bilxdi.github.io/H1D024074-PraktikumKB-Responsi/pakarfuzzycerna.html">

```html
<!DOCTYPE html>
<html lang="eng">
<head>
    <meta charset="UTF-8">
    <title>Sistem Diagnosa Pencernaan</title>
</head>
<body>

    <h2>Sistem Diagnosa Gangguan Pencernaan</h2>
    <p>Jawablah pertanyaan berikut dengan angka yang sesuai. Isi dengan 0 jika tidak mengalami. Gunakan tombol keyboard TAB untuk isi dengan cepat.</p>

    <form id="formDiagnosa">
        <label>1. Berapa kali Anda BAB cair hari ini? (0-15):</label><br>
        <input type="number" id="g1" min="0" max="15" value="0" required><br><br>

        <label>2. Seberapa parah mual/muntah Anda? (Skala 0-10):</label><br>
        <input type="number" id="g2" min="0" max="10" value="0" required><br><br>

        <label>3. Berapa suhu tubuh Anda saat ini? (normal sekitar 36,5)(Celcius, misal 37.5):</label><br>
        <input type="number" id="g3" min="36.0" max="41.0" step="0.1" value="36.5" required><br><br>

        <label>4. Sudah berapa hari Anda mengalami diare? (0-14):</label><br>
        <input type="number" id="g4" min="0" max="14" value="0" required><br><br>

        <label>5. Seberapa parah gejala muncul setelah makan? (Skala 0-10):</label><br>
        <input type="number" id="g5" min="0" max="10" value="0" required><br><br>

        <label>6. Seberapa yakin Anda baru saja makan makanan mencurigakan? (Skala 0-10):</label><br>
        <input type="number" id="g6" min="0" max="10" value="0" required><br><br>

        <label>7. Seberapa parah perut kembung Anda? (Skala 0-10):</label><br>
        <input type="number" id="g7" min="0" max="10" value="0" required><br><br>

        <label>8. Berapa kali Anda buang gas hari ini? (0-20):</label><br>
        <input type="number" id="g8" min="0" max="20" value="0" required><br><br>

        <label>9. Seberapa yakin gejala muncul setelah minum/makan olahan susu? (Skala 0-10):</label><br>
        <input type="number" id="g9" min="0" max="10" value="0" required><br><br>

        <label>10. Seberapa stres Anda saat ini? (Skala 0-10):</label><br>
        <input type="number" id="g10" min="0" max="10" value="0" required><br><br>

        <label>11. Seberapa lemas badan Anda? (Skala 0-10):</label><br>
        <input type="number" id="g11" min="0" max="10" value="0" required><br><br>

        <button type="button" onclick="prosesDiagnosa(); scrollToBottom();">Proses Diagnosa</button>
    </form>

    <h3 id="judulHasil" style="display:none;">HASIL DIAGNOSA</h3>
    <div id="hasilDiagnosa"></div>

    <script>
        // 1. FUNGSI MEMBERSHIP FUZZY (Matematika Dasar)
        // Fungsi Segitiga (Trimf)
        function trimf(x, a, b, c) {
            if (x <= a || x >= c) return 0;
            if (x > a && x <= b) return (x - a) / (b - a);
            if (x > b && x < c) return (c - x) / (c - b);
            return 0;
        }

        // Fungsi Trapesium (Trapmf)
        function trapmf(x, a, b, c, d) {
            if (x <= a || x >= d) return 0;
            if (x > a && x <= b) return (x - a) / (b - a);
            if (x > b && x <= c) return 1;
            if (x > c && x < d) return (d - x) / (d - c);
            return 0;
        }

        // 2. FUNGSI BANTUAN UNTUK GEJALA BERSKALA (0-10)
        function skala_sedang(x) { return trimf(x, 3, 5, 7); }
        function skala_tinggi(x) { return trapmf(x, 6, 8, 10, 10); }

        // 3. FUNGSI DEFUZZIFIKASI (Mencari Persentase Akhir)
        // Menggunakan metode Sugeno: Tinggi bobotnya 85%, Sedang bobotnya 50%
        function hitungPersentase(bobot_tinggi, bobot_sedang) {
            if (bobot_tinggi === 0 && bobot_sedang === 0) return 0;
            let nilai_tinggi = 85; 
            let nilai_sedang = 50;
            // Rumus Weighted Average (Rata-rata Terbobot)
            let atas = (bobot_tinggi * nilai_tinggi) + (bobot_sedang * nilai_sedang);
            let bawah = bobot_tinggi + bobot_sedang;
            return atas / bawah;
        }

        // 4. PROGRAM UTAMA (Dijalankan saat tombol diklik)
        function prosesDiagnosa() {
            // Mengambil nilai input dari form HTML
            let g1 = parseFloat(document.getElementById('g1').value) || 0;
            let g2 = parseFloat(document.getElementById('g2').value) || 0;
            let g3 = parseFloat(document.getElementById('g3').value) || 0;
            let g4 = parseFloat(document.getElementById('g4').value) || 0;
            let g5 = parseFloat(document.getElementById('g5').value) || 0;
            let g6 = parseFloat(document.getElementById('g6').value) || 0;
            let g7 = parseFloat(document.getElementById('g7').value) || 0;
            let g8 = parseFloat(document.getElementById('g8').value) || 0;
            let g9 = parseFloat(document.getElementById('g9').value) || 0;
            let g10 = parseFloat(document.getElementById('g10').value) || 0;
            let g11 = parseFloat(document.getElementById('g11').value) || 0;

            // Fuzzifikasi Variabel Spesifik
            let g1_sering = trimf(g1, 2, 4, 6);
            let g1_sangat_sering = trapmf(g1, 5, 7, 15, 15);

            let g3_normal = trimf(g3, 36.0, 36.5, 37.5);
            let g3_sumeng = trimf(g3, 37.0, 38.0, 39.0);
            let g3_tinggi = trapmf(g3, 38.5, 39.5, 41.0, 41.0);

            let g4_lama = trapmf(g4, 5, 7, 14, 14);
            let g8_sering = trapmf(g8, 6, 10, 20, 20);

            // Penerapan Aturan Fuzzy (Logika AND diwakili oleh Math.min)
            
            // 1. Diare Infeksi
            let diare_tinggi = Math.min(g1_sangat_sering, skala_tinggi(g2), g3_tinggi, g4_lama);
            let diare_sedang = Math.min(g1_sering, g3_sumeng);
            let hasil_diare = hitungPersentase(diare_tinggi, diare_sedang);

            // 2. Keracunan Makanan
            let racun_tinggi = Math.min(g1_sangat_sering, skala_tinggi(g2), skala_tinggi(g5), skala_tinggi(g6));
            let racun_sedang = Math.min(skala_tinggi(g5), skala_tinggi(g6));
            let hasil_racun = hitungPersentase(racun_tinggi, racun_sedang);

            // 3. Intoleransi Laktosa
            let laktosa_tinggi = Math.min(g1_sering, skala_tinggi(g7), g8_sering, skala_tinggi(g9));
            let laktosa_sedang = Math.min(skala_sedang(g7), skala_tinggi(g9));
            let hasil_laktosa = hitungPersentase(laktosa_tinggi, laktosa_sedang);

            // 4. Irritable Bowel Syndrome (IBS)
            let ibs_tinggi = Math.min(g1_sering, g3_normal, skala_tinggi(g7), skala_tinggi(g10));
            let ibs_sedang = Math.min(g1_sering, skala_sedang(g10));
            let hasil_ibs = hitungPersentase(ibs_tinggi, ibs_sedang);

            // 5. Gastroenteritis
            let gastro_tinggi = Math.min(g1_sangat_sering, skala_tinggi(g2), g3_sumeng, skala_tinggi(g11));
            let gastro_sedang = Math.min(g1_sering, skala_sedang(g11));
            let hasil_gastro = hitungPersentase(gastro_tinggi, gastro_sedang);

            // Menyusun hasil ke dalam Array untuk diurutkan
            let daftarHasil = [
                { nama: "Diare Infeksi", persen: hasil_diare },
                { nama: "Keracunan Makanan", persen: hasil_racun },
                { nama: "Intoleransi Laktosa", persen: hasil_laktosa },
                { nama: "Irritable Bowel Syndrome (IBS)", persen: hasil_ibs },
                { nama: "Gastroenteritis", persen: hasil_gastro }
            ];

            // Urutkan dari yang terbesar ke terkecil
            daftarHasil.sort((a, b) => b.persen - a.persen);

            // Menampilkan Output di HTML
            document.getElementById("judulHasil").style.display = "block";
            let divHasil = document.getElementById("hasilDiagnosa");
            divHasil.innerHTML = ""; // Bersihkan hasil sebelumnya

            let adaHasil = false;
            for (let i = 0; i < daftarHasil.length; i++) {
                if (daftarHasil[i].persen > 0) {
                    divHasil.innerHTML += `<p>- <b>${daftarHasil[i].nama}</b> : ${daftarHasil[i].persen.toFixed(2)}%</p>`;
                    adaHasil = true;
                }
            }

            if (!adaHasil) {
                divHasil.innerHTML = "<p>Gejala terlalu ringan atau tidak ada aturan pakar yang cocok.</p>";
            }
        }

        // Fungsi scroll ke bawah
        function scrollToBottom() {
            window.scrollTo({
                top: document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
            }
    </script>

</body>
</html>
```
