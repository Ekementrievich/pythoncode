#!/usr/bin/env python3

import tkinter as tk
import datetime

class Countdown:
    def __init__(self, root, target_date):
        self.root = root
        self.root.title("Countdown to Happy New Year")

        self.target_date = target_date
        self.remaining_time = tk.StringVar()

        self.time_label = tk.Label(self.root, textvariable=self.remaining_time, font=("Helvetica", 48))
        self.time_label.pack()

        self.update_countdown()

    def update_countdown(self):
        current_time = datetime.datetime.now()
        time_difference = self.target_date - current_time

        if time_difference.total_seconds() <= 0:
            self.remaining_time.set("Happy New Year!")
        else:
            days = time_difference.days
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.remaining_time.set(f"{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}")

        self.root.after(1000, self.update_countdown)

root = tk.Tk()
target_date = datetime.datetime(datetime.datetime.now().year + 1, 1, 1, 0, 0, 0)  # Set the target date to next year's January 1st
countdown = Countdown(root, target_date)
root.mainloop()
