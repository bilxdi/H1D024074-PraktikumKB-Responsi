# H1D024074-PraktikumKB-Responsi
<meta http-equiv="refresh" content="0; URL=https://bilxdi.github.io/H1D024074-PraktikumKB-Responsi/pakarfuzzycerna.html">

## 1. Fungsi Membership Fuzzy
```js
// 1. Fungsi Membership Fuzzy
// Fungsi Segitiga (Trimf)
function trimf(x, a, b, c) {
    if (x <= a || x >= c) return 0;
    if (x > a && x <= b) return (x - a) / (b - a);
    if (x > b && x < c) return (c - x) / (c - b);
    return 0;
}
```
Membuat fungsi custom untuk menggantikan `fuzz.trimf`<br>
Jika diluar segitiga return `0`<br>
Jika di segitiga naik return `(x - a) / (b - a)`<br>
Jika di segitiga turun return `(c - x) / (c - b)`<br>
Jika tidak ada kondisi return `0`

```js
// Fungsi Trapesium (Trapmf)
function trapmf(x, a, b, c, d) {
    if (x < a || x > d) return 0;
    if (x >= b && x <= c) return 1;
    if (x > a && x < b) return (x - a) / (b - a);
    if (x > c && x < d) return (d - x) / (d - c);
    return 0;
}
```
Membuat fungsi custom untuk menggantikan `fuzz.trapmf`<br>
Jika diluar trapesium return `0`<br>
Jika diatas trapesium return `1`<br>
Jika di sisi naik return `(x - a) / (b - a)`<br>
Jika di sisi turun return `(d - x) / (d - c)`<br>
Jika tidak ada kondisi return `0`

## 2. Fungsi Bantuan Untuk Skala 0-10
```js
// 2. Fungsi Bantuan Untuk Skala 0-10
function skala_sedang(x) { return trimf(x, 3, 5, 7); }
function skala_tinggi(x) { return trapmf(x, 6, 8, 10, 10); }
```
Membuat fungsi untuk gejala yang membership fuzzy nya mirip (yang skala 0-10)

## 3. Fungsi Hitung Persentase
```js
// 3. Fungsi Hitung Persentase
// Menggunakan metode Sugeno: Tinggi bobotnya 85%, Sedang bobotnya 50%
function hitungPersentase(bobot_tinggi, bobot_sedang) {
    if (bobot_tinggi === 0 && bobot_sedang === 0) return 0;
    let nilai_tinggi = 85; 
    let nilai_sedang = 50;
```

```js
    // Rumus Weighted Average (Rata-rata Terbobot)
    let atas = (bobot_tinggi * nilai_tinggi) + (bobot_sedang * nilai_sedang);
    let bawah = bobot_tinggi + bobot_sedang;
    return atas / bawah;
}
```
Membuat fungsi untuk menghitung persentase menggunakan weighted average

## 4. Fungsi Proses Diagnosa
```js
// 4. Fungsi Proses Diagnosa
function prosesDiagnosa() {
    // Cek apakah input valid
    let form = document.getElementById("formDiagnosa");
    if (!form.reportValidity()) {
        return;
    }
```

```js
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
```

```js
    // Fuzzifikasi Variabel Spesifik
    let g1_sering = trimf(g1, 2, 4, 6);
    let g1_sangat_sering = trapmf(g1, 5, 7, 15, 15);

    let g3_normal = trimf(g3, 36.0, 36.5, 37.5);
    let g3_sumeng = trimf(g3, 37.0, 38.0, 39.0);
    let g3_tinggi = trapmf(g3, 38.5, 39.5, 41.0, 41.0);

    let g4_lama = trapmf(g4, 5, 7, 14, 14);
    let g8_sering = trapmf(g8, 6, 10, 20, 20);
```

```js
    // Penerapan Aturan Fuzzy (Menggunakan Math.min untuk memenuhi aturan AND=min)
    
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
```

```js
    // Menyusun hasil ke dalam Array untuk diurutkan
    let daftarHasil = [
        { nama: "Diare Infeksi", persen: hasil_diare },
        { nama: "Keracunan Makanan", persen: hasil_racun },
        { nama: "Intoleransi Laktosa", persen: hasil_laktosa },
        { nama: "Irritable Bowel Syndrome (IBS)", persen: hasil_ibs },
        { nama: "Gastroenteritis", persen: hasil_gastro }
    ];
```

```js
    // Urutkan dari yang terbesar ke terkecil
    daftarHasil.sort((a, b) => b.persen - a.persen);
```

```js
    // Menampilkan Output di HTML
    document.getElementById("judulHasil").style.display = "block";
    let divHasil = document.getElementById("hasilDiagnosa");
    divHasil.innerHTML = ""; // Bersihkan hasil sebelumnya
```

```js
    let adaHasil = false;
    for (let i = 0; i < daftarHasil.length; i++) {
        if (daftarHasil[i].persen > 0) {
            divHasil.innerHTML += `<p>- <b>${daftarHasil[i].nama}</b> : ${daftarHasil[i].persen.toFixed(2)}%</p>`;
            adaHasil = true;
        }
    }
```

```js
    if (!adaHasil) {
        divHasil.innerHTML = "<p>Gejala terlalu ringan atau tidak ada aturan pakar yang cocok.</p>";
    }
}
```

## 5. Fungsi Tambahan
```js
// 5. FUNGSI TAMBAHAN (Untuk lain-lain)
// Fungsi scroll ke bawah
function scrollToBottom() {
    window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: 'smooth'
    });
    }
```
Membuat fungsi untuk keperluan lain lain (diluar program utama)