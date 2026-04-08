🎨 Creative Canvas History Manager

Proyek UTS Struktur Data - Semester Genap 2025/2026
Implementasi Stack menggunakan Doubly Linked List untuk Sistem Undo/Redo.

👥 Identitas Kelompok

Nama Lengkap

NIM

Peran

Akun GitHub

[Nama Anda]

[NIM Anda]

Lead Developer / Report

@username

[Nama Rekan]

[NIM Rekan]

UI Designer / Tester

@username

📌 1. Rumusan Masalah dan Solusi

Rumusan Masalah:

Bagaimana mengoptimalkan penyimpanan riwayat aksi pada aplikasi desain tanpa membebani memori secara statis?

Bagaimana memastikan alur navigasi Undo dan Redo berjalan sinkron secara dua arah?

Bagaimana sistem menangani konflik riwayat (branching) saat pengguna melakukan aksi baru di posisi tengah riwayat?

Solusi Sistem:

Sistem menggunakan Doubly Linked List untuk mengimplementasikan konsep Stack. Setiap perubahan status kanvas disimpan dalam sebuah node dinamis. Penggunaan dua pointer (prev dan next) memungkinkan navigasi dua arah yang instan. Untuk masalah percabangan, sistem secara otomatis menghapus node "masa depan" yang tidak valid saat ada input baru, memastikan integritas urutan aksi.

📚 2. Landasan Teori

Struktur data adalah fondasi dalam pengorganisasian data di memori komputer agar proses manipulasi data menjadi lebih efisien. Pemilihan struktur data yang tepat sangat krusial dalam aplikasi yang memerlukan performa tinggi seperti editor grafis, di mana setiap detik interaksi pengguna harus tercatat dengan baik.

Dalam proyek ini, diterapkan konsep Stack (Tumpukan) dengan prinsip LIFO (Last-In-First-Out). Meskipun secara tradisional Stack sering diasosiasikan dengan array, implementasi menggunakan Linked List menawarkan fleksibilitas alokasi memori dinamis. Hal ini sangat menguntungkan karena jumlah riwayat (history) tidak dibatasi oleh ukuran array statis di awal program.

Secara spesifik, Doubly Linked List digunakan agar setiap node memiliki referensi ke langkah sebelumnya (Undo) dan langkah sesudahnya (Redo). Navigasi ini memungkinkan kompleksitas waktu $O(1)$ untuk berpindah antar status, yang jauh lebih efisien dibandingkan melakukan pencarian pada array besar.

Sumber Ilmiah:

Cormen, T. H., et al. (2022). Introduction to Algorithms. MIT Press. (Membahas efisiensi Stack dalam manajemen memori).

Aho, A. V., & Ullman, J. D. (1983). Data Structures and Algorithms. Addison-Wesley. (Konsep dasar Linked List).

Sartaj Sahni. (2005). Data Structures, Algorithms, and Applications. McGraw-Hill. (Penerapan struktur data pada aplikasi nyata).

⚙️ 3. Desain Sistem dan Implementasi

<img width="842" height="1264" alt="FLOWCHART CANVAS" src="https://github.com/user-attachments/assets/fc628d3c-0209-483d-ae0b-136ac2db2117" />

Alur Kerja (Input → Proses → Output)

Input: Pengguna melakukan aksi (misal: "Draw Circle", "Change Color").

Proses: - Aksi dibungkus ke dalam Node.

Melakukan operasi Push ke dalam Doubly Linked List.

Jika posisi bukan di akhir, potong jalur next.

Update pointer current ke node terbaru.

Output: Visualisasi status kanvas saat ini sesuai posisi pointer.

Operasi Minimal (Stack)

Push: Menambahkan status baru ke dalam riwayat.

Pop (Undo): Mengambil status sebelumnya dan memindahkan pointer ke belakang.

Peek (Redo): Melihat status berikutnya dan memindahkan pointer ke depan.

Display: Menampilkan seluruh urutan riwayat yang tersimpan di memori.

Diagram Proses (Mermaid)

graph LR
    A[Start] --> B[Aksi Baru]
    B --> C{Posisi Current?}
    C -- Di Tengah --> D[Hapus Node Depan]
    C -- Di Akhir --> E[Tambah Node Baru]
    D --> E
    E --> F[Update Current Pointer]
    F --> G[End]


💻 4. Implementasi Program (Preview)

Implementasi menggunakan bahasa pemrograman Python dengan struktur class yang modular.

# Contoh struktur sederhana
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CanvasHistory:
    # Logika Push, Undo, Redo, Display berada di sini
    pass


🏁 4. Kesimpulan

Berdasarkan hasil pengembangan, dapat disimpulkan bahwa:

Rumusan masalah terselesaikan: Sistem mampu mengelola riwayat tanpa batas statis dan menangani percabangan aksi dengan tepat.

Kesesuaian Teori: Implementasi Stack melalui Doubly Linked List terbukti sangat efektif untuk fitur navigasi dua arah sesuai prinsip LIFO.

Manfaat: Pengguna mendapatkan pengalaman editing yang aman karena setiap kesalahan dapat dibatalkan (Undo) atau dikembalikan (Redo) secara instan.

🚀 Dibuat untuk memenuhi kriteria penilaian UTS Struktur Data 2025.
