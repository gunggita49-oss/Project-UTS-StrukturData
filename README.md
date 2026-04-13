# 🎨 Creative Canvas History Manager

### 📌 Rumusan Masalah dan Solusi

**Rumusan Masalah:**

1. Bagaimana mengoptimalkan penyimpanan riwayat aksi pada aplikasi desain tanpa membebani memori secara statis?

2. Bagaimana memastikan alur navigasi Undo dan Redo berjalan sinkron secara dua arah?

3. Bagaimana sistem menangani konflik riwayat (branching) saat pengguna melakukan aksi baru di posisi tengah riwayat?

**Solusi Sistem:**

Sistem menggunakan Doubly Linked List untuk mengimplementasikan konsep Stack. Setiap perubahan status kanvas disimpan dalam sebuah node dinamis. Penggunaan dua pointer (prev dan next) memungkinkan navigasi dua arah yang instan. Untuk masalah percabangan, sistem secara otomatis menghapus node "masa depan" yang tidak valid saat ada input baru, memastikan integritas urutan aksi.

---

### 📚 Landasan Teori

Struktur data adalah fondasi dalam pengorganisasian data di memori komputer agar proses manipulasi data menjadi lebih efisien. Pemilihan struktur data yang tepat sangat krusial dalam aplikasi yang memerlukan performa tinggi seperti editor grafis, di mana setiap detik interaksi pengguna harus tercatat dengan baik.

Dalam proyek ini, diterapkan konsep **Stack (Tumpukan)** dengan prinsip **LIFO (Last-In-First-Out).** Meskipun secara tradisional Stack sering diasosiasikan dengan array, implementasi menggunakan **Linked List** menawarkan fleksibilitas alokasi memori dinamis. Hal ini sangat menguntungkan karena jumlah riwayat (history) tidak dibatasi oleh ukuran array statis di awal program.

Secara spesifik, **Doubly Linked List** digunakan agar setiap node memiliki referensi ke langkah sebelumnya (Undo) dan langkah sesudahnya (Redo). Navigasi ini memungkinkan kompleksitas waktu untuk berpindah antar status, yang jauh lebih efisien dibandingkan melakukan pencarian pada array besar.

**Sumber Ilmiah:**
* Cormen, T. H., et al. (2022). Introduction to Algorithms. MIT Press. (Membahas efisiensi Stack dalam manajemen memori).

* Aho, A. V., & Ullman, J. D. (1983). Data Structures and Algorithms. Addison-Wesley. (Konsep dasar Linked List).

* Sartaj Sahni. (2005). Data Structures, Algorithms, and Applications. McGraw-Hill. (Penerapan struktur data pada aplikasi nyata).

---

### ⚙️ Desain Sistem dan Implementasi

<img src="https://github.com/user-attachments/assets/fc628d3c-0209-483d-ae0b-136ac2db2117" width="50%" alt="FLOWCHART CANVAS" />

## 📌 Alur Kerja Sistem (Input → Proses → Output)

### 📥 Input
Pengguna melakukan aksi pada aplikasi:
- Menambah objek (Persegi / Lingkar)
- Undo
- Redo

---

### ⚙️ Proses

#### 🟢 Aksi Baru (Push)
1. Sistem membuat **Node baru** yang berisi:
   - `action` (nama aksi)
   - `canvas_state` (snapshot kondisi canvas)
2. Jika posisi `current` **tidak di akhir**:
   - Sistem menghapus semua node setelah `current` (**branching / hapus redo**)
3. Node baru disambungkan ke linked list:
   - `current.next = new_node`
   - `new_node.prev = current`
4. Pointer diperbarui:
   - `current = new_node`

---

#### 🟡 Undo
1. Sistem mengecek apakah ada node sebelumnya:
   - Jika ada → `current = current.prev`
2. Sistem melakukan **restore canvas** berdasarkan `canvas_state`

---

#### 🔵 Redo
1. Sistem mengecek apakah ada node berikutnya:
   - Jika ada → `current = current.next`
2. Sistem melakukan **restore canvas**

---

#### 🟣 Restore State
- Menghapus semua objek pada canvas
- Menggambar ulang objek berdasarkan `canvas_state` dari node saat ini

---

### 📤 Output
- Tampilan canvas berubah sesuai posisi `current`
- History ditampilkan dan diperbarui
- Posisi saat ini ditandai pada history

---

## 🔗 Struktur Data yang Digunakan

Sistem ini menggunakan **Doubly Linked List**, di mana:
- Setiap node memiliki pointer:
  - `prev` → ke node sebelumnya (Undo)
  - `next` → ke node berikutnya (Redo)
- Pointer `current` menunjukkan posisi state saat ini

---

## 🔄 Operasi Utama

- **Push (Tambah Aksi)**  
  Menambahkan node baru ke dalam history

- **Undo (Move Backward)**  
  Memindahkan pointer ke node sebelumnya (`prev`)

- **Redo (Move Forward)**  
  Memindahkan pointer ke node berikutnya (`next`)

- **Traverse / Display**  
  Menampilkan seluruh history dari `head` hingga akhir

---

## 📊 Diagram Alur (Mermaid)

```mermaid
graph TD

    A[Start] --> B[User melakukan aksi]

    B --> C{Aksi Baru?}

    C -- YA --> D[Buat Node Baru]
    D --> E{Apakah ada next?}

    E -- YA --> F[Hapus semua redo]
    E -- TIDAK --> G[Sambungkan Node Baru]

    F --> G
    G --> H[Update current ke node baru]
    H --> I[Tampilkan History]

    C -- TIDAK --> J{Undo atau Redo?}

    J -- Undo --> K[Current = Prev]
    J -- Redo --> L[Current = Next]

    K --> M[Restore Canvas]
    L --> M

    M --> I
    I --> N[End]

---

### 💻 Implementasi Program (Preview)

Implementasi menggunakan bahasa pemrograman Python dengan struktur class yang modular.

---

### 💡 Contoh Struktur Sederhana

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CanvasHistory:

    # Logika Push, Undo, Redo, Display berada di sini
    pass

---

### 🏁 Kesimpulan

Berdasarkan hasil pengembangan, dapat disimpulkan bahwa:

1. Rumusan masalah terselesaikan: Sistem mampu mengelola riwayat tanpa batas statis dan menangani percabangan aksi dengan tepat.

2. Kesesuaian Teori: Implementasi Stack melalui Doubly Linked List terbukti sangat efektif untuk fitur navigasi dua arah sesuai prinsip LIFO.

3. Manfaat: Pengguna mendapatkan pengalaman editing yang aman karena setiap kesalahan dapat dibatalkan (Undo) atau dikembalikan (Redo) secara instan.
