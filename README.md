# Pertemuan 05 Perulangan Python

Nama: Iqhsan Saleh

NIM: 2225250021

Kelas: 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_arimatika.py

## Algoritma Kuis 2
1. Menerima masukan suku pertama (`a`), beda (`d`), dan banyak suku (`n`).
2. Melakukan validasi menggunakan perulangan `while` untuk memastikan `n` bernilai integer positif. Jika tidak valid, program meminta masukan ulang.
3. Menginisialisasi variabel `total = 0.0` untuk akumulasi jumlah deret.
4. Menggunakan perulangan `for` sebanyak `n` kali untuk menghitung suku ke-$i$ menggunakan rumus `a + i * d`.
5. Menampilkan nomor suku beserta nilainya, lalu menambahkan nilai suku tersebut ke akumulator `total`.
6. Setelah perulangan selesai, menampilkan hasil akhir penjumlahan seluruh suku dengan format dua angka di belakang koma.

## Hasil Pengujian
| No | Masukan ($a, d, n$) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| 1 | $a=2, d=3, n=5$ | Suku: 2, 5, 8, 11, 14<br>Jumlah = 40 | Suku: 2.0, 5.0, 8.0, 11.0, 14.0<br>Jumlah = 40.00 | Sesuai |
| 2 | $a=10, d=-2, n=4$ | Suku: 10, 8, 6, 4<br>Jumlah = 28 | Suku: 10.0, 8.0, 6.0, 4.0<br>Jumlah = 28.00 | Sesuai |
| 3 | $a=1.5, d=0.5, n=3$ | Suku: 1.5, 2.0, 2.5<br>Jumlah = 6.0 | Suku: 1.5, 2.0, 2.5<br>Jumlah = 6.00 | Sesuai |

## Refleksi
Dalam perancangan program deret aritmetika ini, kami mengidentifikasi beberapa aspek fundamental terkait kontrol alur iterasi yang perlu dijelaskan.

Jumlah perulangan sepenuhnya dikendalikan oleh variabel $n$ melalui parameter pada fungsi range(n). Kami memilih struktur for karena batas perulangannya sudah definitif, yakni berjalan sebanyak $n$ kali sesuai banyak suku yang diminta.

Terkait pengelolaan akumulator, variabel total wajib diinisialisasi bernilai nol di luar blok perulangan. Jika penugasan total = 0 diletakkan di dalam tubuh loop, variabel tersebut akan mengalami reset pada setiap iterasi, yang mengakibatkan nilai akhir hanya merekam suku terakhir alih-alih mengakumulasikan keseluruhan deret. Analoginya mirip seperti wadah penampung air yang harus diletakkan kosong di awal, bukan dikosongkan kembali di setiap pancuran air menetes.

Sementara itu, pemilihan struktur while untuk validasi nilai $n$ didasarkan pada sifatnya yang bersifat kondisional. Karena kami tidak dapat memprediksi berapa kali pengguna memasukkan angka nol atau negatif, konstruksi while memungkinkan program terus meminta masukan ulang sampai syarat bilangan bulat positif terpenuhi.

Kepastian berhentinya perulangan dapat dibuktikan secara logis melalui batasan indeksnya. Perulangan for bergerak secara teratur dari $0$ hingga $n-1$, sehingga eksekusi program dijamin terhenti begitu batas atas tercapai. Di sisi lain, perulangan while akan memutus siklusnya seketika ekspresi logika $n \le 0$ bernilai salah. Seluruh mekanisme ini memastikan program berjalan deterministik tanpa memicu perulangan tak berhingga.