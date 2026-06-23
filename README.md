# Visualisasi Silsilah Keluarga Nachrowi & Dewi Mariam 🌳

Proyek ini adalah sebuah aplikasi web interaktif untuk memvisualisasikan silsilah keluarga besar secara dinamis. Awalnya dibangun menggunakan Python (`networkx` & `matplotlib`), proyek ini kini telah sepenuhnya berevolusi menjadi sebuah aplikasi web modern berbasis antarmuka (**HTML, CSS, JS**) untuk memberikan pengalaman yang lebih fleksibel, interaktif, dan mudah digunakan.

Aplikasi ini dapat langsung dijalankan secara *offline* di browser mana saja tanpa perlu proses instalasi yang rumit.

## ✨ Fitur Utama

- **Interaktif & Dinamis:** Menggunakan teknologi D3.js untuk memetakan silsilah secara otomatis.
- **Navigasi Mudah:** Mendukung fitur *Zoom In/Out* (menggunakan scroll mouse/touchpad) dan *Drag/Pan* (menggeser layar) untuk menjelajahi keluarga besar.
- **Buka & Tutup Cabang (Expand/Collapse):** Klik pada suatu kotak (node) untuk menyembunyikan atau memunculkan garis keturunannya. Sangat berguna untuk merapikan tampilan visualisasi yang padat.
- **Custom Foto Profil:** Dilengkapi fitur unggah foto untuk setiap anggota keluarga secara individual. Foto akan langsung disimpan secara lokal di browser (`localStorage`), menjaga privasi data tanpa perlu server tambahan.
- **Desain Modern (Dark Mode):** Tampilan *user interface* dirancang estetik menggunakan **Tailwind CSS**, dengan pewarnaan *card* yang diatur bertingkat berdasarkan urutan generasi (Akar, Anak, Cucu, Cicit, dst).
- **Legenda & Tooltip:** Arahkan kursor ke *card* untuk melihat detail anggota keluarga, jumlah anak, dan posisi generasinya.

## 💻 Teknologi yang Digunakan

Proyek ini dibuat ringan tanpa ketergantungan pada *framework backend* agar mudah dikelola dan dimodifikasi oleh siapa saja.
1. **HTML5 & Vanilla JavaScript**: Struktur inti dan logika aplikasi web.
2. **Tailwind CSS (via CDN)**: *Framework utility-first* untuk merancang tampilan yang responsif dan modern dengan cepat.
3. **D3.js (Data-Driven Documents)**: *Library* JavaScript andalan untuk membangun layout graf berbentuk pohon (hierarchy) yang dinamis.
4. **Python (opsional)**: *Script* ekstraksi awal (`silsilah.py.py` dan `extract_tree.py`) untuk mengubah format teks struktur keluarga ke dalam format JSON/JS.

## 🚀 Cara Menjalankan Aplikasi

Aplikasi ini **tidak memerlukan Node.js, Web Server, atau instalasi apapun**.

1. Pastikan Anda memiliki browser modern (Google Chrome, Microsoft Edge, Firefox, atau Safari).
2. Temukan file `index.html` di dalam folder proyek ini.
3. **Klik dua kali (*double-click*)** pada `index.html`.
4. Browser akan terbuka dan silsilah keluarga Anda sudah bisa diakses!

> **Catatan:** Pada saat pertama kali dibuka, pastikan komputer/laptop Anda terhubung ke internet agar browser dapat mengunduh library D3.js dan Tailwind CSS dari CDN. Setelah termuat di *cache*, aplikasi dapat berjalan *offline*.

## 🛠️ Cara Mengubah Data Anggota Keluarga

Seluruh data anggota keluarga tersimpan di dalam file `data.js`.
Jika ada penambahan anggota keturunan baru, langkah-langkahnya adalah sebagai berikut:

1. Buka file `data.js` menggunakan *Text Editor* (Notepad, VS Code, dsb).
2. Anda akan melihat sebuah struktur list (*array of objects*) bernama `FAMILY_DATA`.
3. Untuk menambahkan anak baru, tambahkan baris data berikut di bagian bawah sebelum tutup siku `]`:
   ```javascript
   { 
     id: "node_128",              // Buat ID yang unik / belum terpakai
     name: "Nama Anak",           // Nama anggota keluarga baru
     parentId: "node_50",         // Masukkan ID dari orang tuanya
     level: 4,                    // Kedalaman generasi (Akar = 0, Anak = 1, Cucu = 2, dst)
     photo: "images/nama_file.jpg" // (Opsional) Path ke file foto lokal Anda
   }
   ```
4. Simpan (*save*) file tersebut dan *Refresh* browser Anda. Silsilah otomatis akan diperbarui!

## 📷 Cara Menambahkan Foto Profil

Terdapat dua metode untuk memasukkan foto anggota keluarga:

### Metode 1: Menggunakan Fitur Unggah di Browser (Praktis & Cepat)
1. Buka `index.html` di browser Anda.
2. **Double-click (klik dua kali)** secara cepat pada kotak/card nama orang yang ingin Anda tambahkan fotonya.
3. Jendela pop-up (modal) detail anggota akan terbuka.
4. Klik tombol **"Choose File"** (atau "Pilih File") di bawah kolom **Ganti Foto**.
5. Pilih foto dari komputer/perangkat Anda. Foto akan langsung tampil di silsilah secara otomatis!
> **Catatan:** Metode ini menyimpan foto di dalam memori penyimpanan lokal browser Anda (`localStorage`). Foto tidak diunggah ke server internet. Namun, jika Anda membersihkan *cache/history* browser, foto tersebut bisa hilang, dan foto tidak akan tampil jika dibuka dari komputer/browser lain.

### Metode 2: Menyimpan File Foto secara Permanen (Rekomendasi untuk Github/Publikasi)
Jika ingin foto tersimpan secara permanen dan bisa dilihat oleh orang lain saat web dibuka di komputer manapun:
1. Siapkan file foto yang ingin digunakan (disarankan format JPG, PNG, atau WEBP dengan rasio kotak/persegi).
2. Masukkan file foto tersebut ke dalam subfolder **`images/`** yang ada di folder proyek ini (misalnya disimpan sebagai `images/budi.jpg`).
3. Buka file `data.js` dan tambahkan baris `photo: "images/nama_file.jpg"` pada objek data anggota keluarga yang bersangkutan. Contoh:
   ```javascript
   { id: "node_1", name: "MUTMA'INAH\n& NUR HASAN", parentId: "root", level: 1, photo: "images/mutmainah.jpg" },
   ```
4. Simpan file `data.js` dan muat ulang halaman `index.html`. Foto akan tampil secara permanen dan aman walaupun cache browser dihapus.

## 🎨 Cara Mengubah Desain & Ukuran (Customization)

Anda memegang kendali penuh atas ukuran silsilah. Pengaturan ini terletak di dalam file `index.html` pada blok `<script>`.
Temukan baris di sekitar bagian `// CONSTANTS`:

- `CARD_W` & `CARD_H`: Berguna untuk memperbesar atau mengecilkan dimensi kotak/card. Angka kunci `0, 1, 2, 3, 4` merepresentasikan tingkat generasinya.
- `V_GAP`: Untuk mengubah tinggi jarak (gap vertikal) antar generasi.
- `H_GAP`: Untuk mengubah rentang kedekatan (gap horizontal) jarak antar saudara/sebelah.

---

**Selamat menelusuri sejarah silsilah keluarga besar Anda!** 👨‍👩‍👧‍👦
