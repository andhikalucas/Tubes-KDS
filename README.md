# Tubes-KDS
Repository ini merupakan pemodelan komputasi untuk penelitian berjudul Analisis Struktur Lipid untuk Prediksi Risiko Penyakit Kardiovaskular (CVD), diimplementasikan menggunakan bahasa pemrograman Python dan Jupyter Notebook untuk analisis.

## Abstrak Penelitian
Penyakit kardiovaskular (CVD) memiliki tingkat mortalitas yang tinggi, bergantung pada variasi dan karakteristik molekul lipid di tingkat atom. Sebagai alternatif deteksi yang lebih efisien dari segi biaya, pendekatan komputasional diusulkan untuk melengkapi uji klinis konvensional. Penelitian ini bertujuan untuk menentukan pengaruh variasi struktur molekul lipid terhadap estimasi risiko penyakit kardiovaskuler melalui pemodelan komputasional. Sistem ini mengadaptasi metode medis Lipidomic Risk Score (LRS) ke dalam bentuk proksi heuristik Skor Risiko Struktural Lipid (SRS). Pemodelan dieksekusi menggunakan Rule-Based Mathematical Scoring Model yang beroperasi melalui empat arsitektur modular: inisialisasi data (parameter karbon, ikatan rangkap, tipe isomer), ekstraksi fitur ke matriks biner, perhitungan nilai pada mesin inferensi, serta kategorisasi diskrit ke dalam label Risiko Rendah, Sedang, atau Tinggi. Hasil simulasi menunjukkan bahwa model komputasi berhasil mengkuantifikasi parameter kualitatif makromolekul lipid secara sistematis, di mana metrik struktural isomer trans berkontribusi pada penalti risiko tertinggi terhadap potensi dislipidemia, diikuti oleh ketiadaan ikatan rangkap pada asam lemak jenuh, sedangkan konfigurasi kelengkungan cis efektif mereduksi akumulasi skor risiko. Penelitian menemukan bahwa variasi struktur penyusun lipid sangat memengaruhi potensi aterogeniknya, dan implementasi heuristik SRS dapat difungsikan sebagai kerangka skrining awal yang cukup akurat untuk mengklasifikasikan risiko penyakit kardiovaskular.
Kata Kunci: Penyakit kardiovaskuler, lipid, lipidomics, Skor Risiko Struktural Lipid (SRS)


### Fitur Utama:
- Analisis data lipid yang komprehensif
- Model prediksi risiko CVD
- Visualisasi data dan hasil analisis

## Tim Pengembang

| Nama Lengkap | NIM | Email |
|---|---|---|
| Nicholas Andhika Lucas | 13523014 | realandhikalucas@gmail.com |
| Stefan Mattew Susanto | 13523020 | stefanmattew246@gmail.com |
| Kenneth Ricardo Chandra | 13523022 | kenneth.ricardo.chandra@gmail.com |

## Instalasi

### Prasyarat
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository ini:**
```bash
git clone https://github.com/andhikalucas/Tubes-KDS.git
cd Tubes-KDS
```

### Cara Menjalankan
1. **Menjalankan Analisis Utama**
```
python lipid_analysis.py
# Atau navigasi ke file lipid_analisis.py dan jalankan program
```

2. ***Menjalankan Plotting Hasil Penelitian**
```
jupyter notebook plot.ipynb
# Atau navigasi ke file plot.ipynb dan jalankan program
```
