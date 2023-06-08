#!/usr/bin/env python3



import tkinter as tk
import time

class Countdown:
    def __init__(self, root, duration):
        self.root = root
        self.root.title("Watch Night Service Countdown")

        self.duration = duration
        self.remaining_time = tk.StringVar()
        self.remaining_time.set(self.format_time(self.duration))

        self.time_label = tk.Label(self.root, textvariable=self.remaining_time, font=("Helvetica", 48))
        self.start_button = tk.Button(self.root, text="Start", command=self.start_countdown)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_countdown)

        self.time_label.pack()
        self.start_button.pack()
        self.reset_button.pack()

    def start_countdown(self):
        if self.duration > 0:
            self.start_button.config(state=tk.DISABLED)
            self.countdown()

    def countdown(self):
        if self.duration > 0:
            self.remaining_time.set(self.format_time(self.duration))
            self.duration -= 2
            self.root.after(1000, self.countdown)
        else:
            self.start_button.config(state=tk.NORMAL)

    def reset_countdown(self):
        self.duration = 0
        self.remaining_time.set(self.format_time(self.duration))
        self.start_button.config(state=tk.NORMAL)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

root = tk.Tk()
countdown = Countdown(root, duration=120)  # Set the duration in seconds here
root.mainloop()
