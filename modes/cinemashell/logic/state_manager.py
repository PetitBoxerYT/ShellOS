class StateManager:
    def __init__(self):
        self.next_view = None

    def switch_to(self, view):
        self.next_view = view
