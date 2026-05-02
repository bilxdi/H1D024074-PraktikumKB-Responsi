# H1D024074-PraktikumKB-Responsi
<!-- <meta http-equiv="refresh" content="0; URL=https://bilxdi.github.io/H1D024074-PraktikumKB-Responsi/pakarfuzzycerna.html"> -->

## 1. Fungsi Membership Fuzzy
### trimf
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

### trapmf
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
Membuat fungsi untuk gejala yang membership fuzzy nya mirip (yang skala 0-10), agar tidak perlu menulis [`trimf`](#trimf) dan [`trapmf`](#trapmf) berkali-kali

## 3. Fungsi Hitung Persentase
```js
// 3. Fungsi Hitung Persentase
// Menggunakan metode Sugeno: Tinggi bobotnya 85%, Sedang bobotnya 50%
function hitungPersentase(bobot_tinggi, bobot_sedang) {
    if (bobot_tinggi === 0 && bobot_sedang === 0) return 0;
    let nilai_tinggi = 85; 
    let nilai_sedang = 50;
```
Membuat fungsi bernama `hitungPersentase` yang menerima angka `0-1` dari `bobot_tinggi` dan `bobot_sedang`, jika nilai dari kedua bobot tidak ada maka return `0`, membuat variabel yang menentukan batas maksimum persentase hasil diagnosis

```js
    // Rumus Weighted Average (Rata-rata Terbobot)
    let atas = (bobot_tinggi * nilai_tinggi) + (bobot_sedang * nilai_sedang);
    let bawah = bobot_tinggi + bobot_sedang;
    return atas / bawah;
}
```
Lanjutan dari fungsi [`hitungPersentase`](#3-fungsi-hitung-persentase) untuk menghitung persentase menggunakan Weighted Average berdasarkan bobot dan nilai maks

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
Membuat fungsi bernama `prosesDiagnosa`, membuat variabel yang menyimpan form dari html, kemudian mengecek jika form belum diisi sesuai aturan maka fungsi akan return kosong

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
Membuat 11 variabel yang menerima masing masing 11 input html dengan id dari masing masing 11 input, jika tidak ada isi dari masing masing input maka diisi `0`

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
Membuat membership fuzzy untuk variabel yang lebih spesifik (tidak skala 0-10) untuk variabel yang lain menggunakan fungsi bantuan skala 0-10<br>
`g1_sering` = segitiga dengan input `g1` dan titik `2, 4, 6`<br>
`g1_sangat_sering` = trapesium dengan input `g1` dan titik `5, 7, 15, 15`<br>
`g3_normal` = segitiga dengan input `g3` dan titik `36.0, 36.5, 37.5`<br>
`g3_sumeng` = segitiga dengan input `g3` dan titik `37.0, 38.0, 39.0`<br>
`g3_tinggi` = trapesium dengan input `g3` dan titik `38.5, 39.5, 41.0, 41.0`<br>
`g4_lama` = trapesium dengan input `g4` dan titik `5, 7, 14, 14`<br>
`g8_sering` = trapesium dengan input `g8` dan titik `6, 10, 20, 20`<br>

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
Membuat variabel `tinggi` dan `sedang` dari setiap penyakit yang diisi dengan nilai gejala terendah dari beberapa nilai gejala (setiap variabel penyakit memiliki gejala yang beda beda), `Math.min` digunakan untuk merepresentasikan operator `AND` dimana `AND`=`min`, kemudian membuat variabel hasil yang diisi dengan hasil dari memanggil fungsi `hitungPersentase` yang diisi dengan `tinggi` dan `sedang` (`bobot_tinggi` dan `bobot_sedang`)

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
Membuat array yang berisi dua bagian: `nama` dan `persen`, yang kemudian `nama` sudah diisi secara manual dan `persen` akan diisi dengan persentase dari `hasil` penerapan fuzzy di kode atas yang sudah memanggil fungsi `hitungPersentase`

```js
    // Urutkan dari yang terbesar ke terkecil
    daftarHasil.sort((a, b) => b.persen - a.persen);
```
Menggunakan `sort((a, b) => b.persen - a.persen)` untuk mengurutkan array `daftarHasil` bagian `persen` dari terbesar ke kecil, kegunaan dari `((a, b) => b - a)` biasanya digunakan untuk mengurutkan terbesar ke kecil (descending)

```js
    // Menampilkan Output di HTML
    document.getElementById("judulHasil").style.display = "block";
    let divHasil = document.getElementById("hasilDiagnosa");
    divHasil.innerHTML = ""; // Bersihkan hasil sebelumnya
```
Mengubah display dari elemen html dengan id `judulHasil` menjadi `block`, kemudian membuat variabel bernama `divHasil` yang diisi dengan elemen html dengan id `hasilDiagnosa` , membersihkan hasil dari proses diagnosa yang sebelumnya (jika ada)

```js
    let adaHasil = false;
    for (let i = 0; i < daftarHasil.length; i++) {
        if (daftarHasil[i].persen > 0) {
            divHasil.innerHTML += `<p>- <b>${daftarHasil[i].nama}</b> : ${daftarHasil[i].persen.toFixed(2)}%</p>`;
            adaHasil = true;
        }
    }
```
Membuat variabel bernama `adaHasil` dengan isi awal `false`, kemudian looping sepanjang array `daftarHasil`, mengecek isi array yang sedang di loop bagian `persen` nya apakah lebih dari 0%, jika lebih dari 0% maka ubah elemen `divHasil` dengan `nama` dan `persen` dari isi yang sedang di loop, kemudia set `adaHasil` menjadi `true`

```js
    if (!adaHasil) {
        divHasil.innerHTML = "<p>Gejala terlalu ringan atau tidak ada aturan pakar yang cocok.</p>";
    }
}
```
Jika `adaHasil` itu tetap `false` setelah melewati loop diatas maka ubah elemen dari `divHasil` dengan konfirmasi bahwa tidak ada hasil

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
Membuat fungsi bernama `scrollToBottom` yang kemudian menjalankan metode yang meng-scroll ke spesifik koordinat yang disini adalah `top`, `top` diisi dengan seluruh tinggi dari halaman yang membuat saat discroll akan ke bawah halaman, kemudian mengubah behavior dari scroll menjadi smooth