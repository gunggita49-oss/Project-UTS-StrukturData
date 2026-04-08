class Node:
    def __init__(self, action, canvas_state=None):
        self.action = action
        self.canvas_state = canvas_state  # List: [(item_id, type, coords, color)]
        self.prev = None
        self.next = None
        self.index = None  # Untuk tree