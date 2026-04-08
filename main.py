import tkinter as tk
from tkinter import ttk
from history import HistoryManager
from colorama import init
import random

init(autoreset=True)

class CanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Canvas History (Simple Version)")
        self.root.geometry("1000x700")

        # Canvas
        self.canvas = tk.Canvas(root, bg='white', width=700, height=700)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # History Manager
        self.hm = HistoryManager(self.canvas)

        # Panel kanan
        right_frame = ttk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        # Tombol utama
        btn_frame = ttk.Frame(right_frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Tambah Persegi", command=self.add_rect).pack(pady=5)
        ttk.Button(btn_frame, text="Tambah Lingkar", command=self.add_oval).pack(pady=5)
        ttk.Button(btn_frame, text="Undo", command=self.undo).pack(pady=5)
        ttk.Button(btn_frame, text="Redo", command=self.redo).pack(pady=5)

        # History list
        ttk.Label(right_frame, text="History Timeline:").pack()
        self.history_list = tk.Listbox(right_frame, height=30)
        self.history_list.pack(fill=tk.BOTH, expand=True, pady=5)

        # Hover preview
        self.history_list.bind("<Motion>", self.on_hover_motion)
        self.history_list.bind("<Leave>", self.on_hover_leave)

        self.tooltip = None

        self.update_history_display()

    # =========================
    # ACTION
    # =========================

    def add_rect(self):
        x1, y1 = random.randint(50,200), random.randint(50,200)
        x2, y2 = x1 + random.randint(50,150), y1 + random.randint(50,150)
        colors = ['green','red','yellow','purple']

        self.canvas.create_rectangle(x1, y1, x2, y2,
                                     fill=random.choice(colors),
                                     tags='obj')

        self.hm.push("[TAMBAH] Persegi", self.hm.capture_state())
        self.update_history_display()

    def add_oval(self):
        x1, y1 = random.randint(300,500), random.randint(300,500)
        x2, y2 = x1 + random.randint(50,150), y1 + random.randint(50,150)
        colors = ['blue','orange','pink']

        self.canvas.create_oval(x1, y1, x2, y2,
                                fill=random.choice(colors),
                                tags='obj')

        self.hm.push("[TAMBAH] Lingkar", self.hm.capture_state())
        self.update_history_display()

    def undo(self):
        self.hm.undo()
        self.update_history_display()

    def redo(self):
        self.hm.redo()
        self.update_history_display()

    # =========================
    # HISTORY DISPLAY
    # =========================

    def update_history_display(self):
        self.history_list.delete(0, tk.END)

        temp = self.hm.head
        i = 0

        while temp:
            marker = " <-- CURRENT" if temp == self.hm.current else ""
            self.history_list.insert(tk.END, f"{i+1}. {temp.action}{marker}")
            temp = temp.next
            i += 1

    # =========================
    # HOVER PREVIEW (AMAN)
    # =========================

    def on_hover_motion(self, event):
        index = self.history_list.nearest(event.y)

        if not self.hm.history_nodes:
            return

        if index < 0 or index >= len(self.hm.history_nodes):
            return

        node = self.hm.history_nodes[index]

        if self.tooltip:
            self.tooltip.destroy()

        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"150x150+{event.x_root+20}+{event.y_root}")

        mini_c = tk.Canvas(self.tooltip, bg='white', width=150, height=150)
        mini_c.pack()

        if node.canvas_state:
            for _, typ, coords, color in node.canvas_state[-2:]:
                sc = [c * 150 / 700 for c in coords]

                if typ == 'rectangle':
                    mini_c.create_rectangle(sc, fill=color)
                elif typ == 'oval':
                    mini_c.create_oval(sc, fill=color)

        self.root.after(2000, self.tooltip.destroy)

    def on_hover_leave(self, event):
        if self.tooltip:
            self.tooltip.destroy()

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasApp(root)
    root.mainloop()