# -*- coding: utf-8 -*-

import tkinter as tk
import random


class SensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Sensor Data GUI")
        self.running = False

        # Display Label
        self.label = tk.Label(root, text="Data: --", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=5)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)

    def start(self):
        self.running = True
        self.update_data()

    def stop(self):
        self.running = False

    def update_data(self):
        if self.running:
            # Simulate sensor data
            data = round(random.uniform(20.0, 30.0), 2)  # e.g., temperature in Celsius
            self.label.config(text=f"Data: {data} °C")
            self.root.after(1000, self.update_data)  # update every 1 second

# Create window
root = tk.Tk()
app = SensorApp(root)
root.mainloop()