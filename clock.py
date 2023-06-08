#!/usr/bin/env python3

import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.elapsed_time = 0

        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.start_button = tk.Button(self.root, text="Start", command=self.start_stopwatch)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_stopwatch)

        self.time_label.pack()
        self.start_button.pack()
        self.reset_button.pack()

    def start_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(text="Start")
        else:
            self.is_running = True
            self.start_button.config(text="Stop")
            self.start_time = time.time()
            self.update_time()

    def reset_stopwatch(self):
        self.is_running = False
        self.start_button.config(text="Start")
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        if self.is_running:
            elapsed = time.time() - self.start_time + self.elapsed_time
            minutes, seconds = divmod(elapsed, 60)
            hours, minutes = divmod(minutes, 60)
            time_string = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
            self.time_label.config(text=time_string)
            self.root.after(1000, self.update_time)

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
