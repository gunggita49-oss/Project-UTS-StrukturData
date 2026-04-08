from node import Node
from colorama import Fore

class HistoryManager:
    def __init__(self, canvas=None):
        self.head = None
        self.current = None
        self.canvas = canvas
        self.history_nodes = []

    def push(self, action, state=None):
        new_node = Node(action, state)

        if self.head is None:
            self.head = new_node
            self.current = new_node
            print(Fore.GREEN + "Aksi pertama ditambahkan!")
            self.update_display()
            return

        # Hapus redo (branching)
        if self.current.next:
            print(Fore.RED + "Redo dihapus (branching terjadi!)")
            temp = self.current.next
            while temp:
                next_node = temp.next
                temp.prev = None
                temp.next = None
                temp = next_node
            self.current.next = None

        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

        print(Fore.GREEN + "Aksi ditambahkan!")
        self.update_display()

    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            if self.canvas:
                self.restore_state()
            print(Fore.YELLOW + "Undo berhasil!")
        else:
            print(Fore.RED + "Tidak bisa undo!")
        self.update_display()

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
            if self.canvas:
                self.restore_state()
            print(Fore.YELLOW + "Redo berhasil!")
        else:
            print(Fore.RED + "Tidak bisa redo!")
        self.update_display()

    def capture_state(self):
        if not self.canvas:
            return None

        items = self.canvas.find_withtag('obj')
        state = []

        for item in items:
            typ = self.canvas.type(item)
            coords = list(self.canvas.coords(item))

            color = (
                self.canvas.itemcget(item, 'fill')
                if typ != 'line'
                else self.canvas.itemcget(item, 'outline')
            )

            state.append((item, typ, coords, color))

        return state

    # 🔥 FIX TOTAL: TANPA FADE (NO ERROR)
    def restore_state(self):
        if not self.canvas:
            return

        # Hapus semua objek lama
        self.canvas.delete('obj')

        # Gambar ulang state sekarang
        if self.current and self.current.canvas_state:
            for _, typ, coords, color in self.current.canvas_state:
                if typ == 'rectangle':
                    self.canvas.create_rectangle(coords, fill=color, tags='obj')
                elif typ == 'oval':
                    self.canvas.create_oval(coords, fill=color, tags='obj')

    def update_display(self):
        self.history_nodes = []

        temp = self.head
        i = 0

        while temp:
            temp.index = i
            self.history_nodes.append(temp)

            if "HAPUS" in temp.action:
                color = Fore.RED
            elif "TAMBAH" in temp.action:
                color = Fore.GREEN
            elif "EDIT" in temp.action:
                color = Fore.YELLOW
            elif "GESER" in temp.action:
                color = Fore.BLUE
            else:
                color = Fore.WHITE

            marker = " <-- CURRENT" if temp == self.current else ""
            print(color + f"{i+1}. {temp.action}{marker}")

            temp = temp.next
            i += 1