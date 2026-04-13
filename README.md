# 🎨 Creative Canvas History Manager

## 📌 Rumusan Masalah dan Solusi

### ❓ Rumusan Masalah
1. Bagaimana mengoptimalkan penyimpanan riwayat aksi pada aplikasi desain tanpa membebani memori secara statis?
2. Bagaimana memastikan alur navigasi Undo dan Redo berjalan sinkron secara dua arah?
3. Bagaimana sistem menangani konflik riwayat (branching) saat pengguna melakukan aksi baru di posisi tengah riwayat?

### 💡 Solusi
Sistem menggunakan **Doubly Linked List** untuk mengimplementasikan konsep **Stack (LIFO)**.  
Setiap perubahan canvas disimpan dalam node yang bersifat dinamis.

- Pointer `prev` digunakan untuk **Undo**
- Pointer `next` digunakan untuk **Redo**
- Jika terjadi aksi baru di tengah history, sistem akan **menghapus semua redo (branching)**

---

## 📚 Landasan Teori

Struktur data merupakan cara untuk mengorganisasi dan menyimpan data agar dapat diakses dan dimanipulasi secara efisien. Pemilihan struktur data sangat penting dalam aplikasi yang membutuhkan performa tinggi seperti editor grafis.

Stack adalah struktur data yang menggunakan prinsip **LIFO (Last In First Out)**, di mana data terakhir yang masuk akan menjadi yang pertama keluar. Konsep ini sangat cocok untuk fitur Undo.

Namun, implementasi Stack menggunakan **Doubly Linked List** memberikan fleksibilitas lebih karena:
- Alokasi memori dinamis
- Mendukung navigasi dua arah (Undo dan Redo)

Dalam sistem ini, Linked List digunakan agar setiap node memiliki referensi ke node sebelumnya (`prev`) dan berikutnya (`next`).

### 📖 Sumber Ilmiah
- Cormen, T. H., et al. (2022). *Introduction to Algorithms*. MIT Press.
- Aho, A. V., & Ullman, J. D. (1983). *Data Structures and Algorithms*. Addison-Wesley.
- Sahni, S. (2005). *Data Structures, Algorithms, and Applications*. McGraw-Hill.

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

Menggunakan **Doubly Linked List**:

- `prev` → untuk Undo
- `next` → untuk Redo
- `current` → posisi saat ini

📌 Catatan:
Meskipun konsepnya Stack (LIFO), implementasi menggunakan Doubly Linked List agar mendukung Redo.

---

## 🔄 Operasi Utama

- **Push** → Menambahkan aksi baru
- **Pop (Undo)** → Kembali ke state sebelumnya
- **Peek (Redo)** → Melihat/mengakses state berikutnya
- **Display** → Menampilkan seluruh history

---

## 📊 Diagram Alur (Mermaid)

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

Contoh struktur utama:

```python
class Node:
    def __init__(self, action, canvas_state=None):
        self.action = action
        self.canvas_state = canvas_state
        self.prev = None
        self.next = None

class HistoryManager:
    def push(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass
```
class CanvasHistory:

    # Logika Push, Undo, Redo, Display berada di sini
    pass

---

### 🏁 Kesimpulan

Berdasarkan hasil pengembangan, dapat disimpulkan bahwa:

1. Sistem berhasil mengelola riwayat aksi secara dinamis tanpa batasan ukuran statis.
2. Implementasi sesuai dengan konsep Stack (LIFO) menggunakan Doubly Linked List.
3. Sistem mampu menangani Undo, Redo, dan branching dengan baik.
4. Penggunaan struktur data ini memberikan efisiensi serta pengalaman pengguna yang lebih aman dalam proses editing.
