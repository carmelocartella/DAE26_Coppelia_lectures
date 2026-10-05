import tkinter as tk
import json
import os

STATE_FILE = "/home/carmelo/coppelia_ws/coppelia_lectures_2026/lesson_2/gui_state.json"

class FanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fan Control")

        # Variables
        self.fan_speed = 0
        self.power_state = False

        # self.load_state()  # Load state from file if exists

        # --- Layout containers ---
        main = tk.Frame(master, padx=12, pady=12)
        main.grid(column=0, row=0, sticky="nsew")

        # Make main expand with the window
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)

        # Left: Power toggle button
        self.power_btn = tk.Button(
            main,
            text="ON" if self.power_state else "OFF",
            width=6,
            command=self.toggle_power
        )
        self.power_btn.grid(column=0, row=0, sticky="nsew", padx=(0, 12))

        # Right: vertical control stack (Up, Screen, Down)
        stack = tk.Frame(main)
        stack.grid(column=1, row=0, sticky="nsew")

        stack.grid_columnconfigure(0, weight=1)
        stack.grid_rowconfigure(0, weight=1)
        stack.grid_rowconfigure(1, weight=1)
        stack.grid_rowconfigure(2, weight=1)

        self.up_btn = tk.Button(stack, text="↑", width=6, command=self.increase)
        self.up_btn.grid(column=0, row=0, pady=(0, 6), sticky="nsew")

        self.screen = tk.Label(stack, text=str(self.fan_speed),
                               width=8, height=2, relief="sunken", anchor="center")
        self.screen.grid(column=0, row=1, pady=4, sticky="nsew")

        self.down_btn = tk.Button(stack, text="↓", width=6, command=self.decrease)
        self.down_btn.grid(column=0, row=2, pady=(6, 0), sticky="nsew")

        master.bind("<Up>", lambda e: self.increase())
        master.bind("<Down>", lambda e: self.decrease())
        master.bind("<space>", lambda e: self.toggle_power())

    # --- Actions ---
    def increase(self):
        if self.fan_speed < 10:
            self.fan_speed += 1
        self.update_screen()
        self.save_state()

    def decrease(self):
        if self.fan_speed > 0:
            self.fan_speed -= 1
        self.update_screen()
        self.save_state()

    def toggle_power(self):
        self.power_state = not self.power_state
        self.power_btn.config(text="ON" if self.power_state else "OFF")
        self.save_state()

    # --- Helpers ---
    def update_screen(self):
        self.screen.config(text=str(self.fan_speed))

    def save_state(self):
        state = {
            "fan_speed": self.fan_speed,
            "power_state": self.power_state
        }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)

    def load_state(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    state = json.load(f)
                    self.fan_speed = state.get("fan_speed", 0)
                    self.power_state = state.get("power_state", False)
            except Exception:
                pass  # Ignore errors and use defaults

if __name__ == "__main__":
    root = tk.Tk()
    app = FanGUI(root)
    root.mainloop()
