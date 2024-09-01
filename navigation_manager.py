class NavigationManager:
    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget
        self.windows = {}

    def register_window(self, name, window):
        """Registers a window with a name identifier."""
        self.windows[name] = window

    def go_to_window(self, name):
        """Switch to a registered window by its name."""
        if name in self.windows:
            self.stacked_widget.setCurrentWidget(self.windows[name])
        else:
            raise ValueError(f"Window '{name}' not registered in NavigationManager.")

    def go_to_home(self):
        self.go_to_window('home')

    def go_to_theory(self):
        self.go_to_window('theory')

    def go_to_analytical(self):
        self.go_to_window('analytical')

    def go_to_euler(self):
        self.go_to_window('euler')

    def go_to_modified_euler(self):
        self.go_to_window('modified_euler')
