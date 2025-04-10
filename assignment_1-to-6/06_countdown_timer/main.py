import time
import tkinter as tk
from tkinter import ttk, messagebox
import winsound
import threading
import math

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Countdown Timer")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Timer variables
        self.is_running = False
        self.paused = False
        self.remaining_time = 0
        self.total_time = 0
        
        # Create GUI
        self.create_widgets()
        
        # Initialize sound (Windows only)
        self.sound_enabled = True
        try:
            winsound.Beep(440, 100)
        except:
            self.sound_enabled = False
        
    def create_widgets(self):
        # Time input frame
        input_frame = ttk.LabelFrame(self.root, text="Set Timer")
        input_frame.pack(pady=20, padx=20, fill="x")
        
        ttk.Label(input_frame, text="Hours:").grid(row=0, column=0, padx=5, pady=5)
        self.hours_entry = ttk.Entry(input_frame, width=5)
        self.hours_entry.grid(row=0, column=1, padx=5, pady=5)
        self.hours_entry.insert(0, "0")
        
        ttk.Label(input_frame, text="Minutes:").grid(row=1, column=0, padx=5, pady=5)
        self.minutes_entry = ttk.Entry(input_frame, width=5)
        self.minutes_entry.grid(row=1, column=1, padx=5, pady=5)
        self.minutes_entry.insert(0, "0")
        
        ttk.Label(input_frame, text="Seconds:").grid(row=2, column=0, padx=5, pady=5)
        self.seconds_entry = ttk.Entry(input_frame, width=5)
        self.seconds_entry.grid(row=2, column=1, padx=5, pady=5)
        self.seconds_entry.insert(0, "10")
        
        # Timer display
        self.time_display = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.time_display.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        
        # Control buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.pause_button = ttk.Button(button_frame, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.grid(row=0, column=2, padx=5)
        
        # Additional features frame
        features_frame = ttk.LabelFrame(self.root, text="Features")
        features_frame.pack(pady=10, padx=20, fill="x")
        
        self.sound_var = tk.IntVar(value=1)
        ttk.Checkbutton(features_frame, text="Enable Sound", variable=self.sound_var).pack(anchor="w", padx=5, pady=5)
        
        ttk.Label(features_frame, text="Alarm Message:").pack(anchor="w", padx=5)
        self.message_entry = ttk.Entry(features_frame)
        self.message_entry.pack(fill="x", padx=5, pady=5)
        self.message_entry.insert(0, "Time's up!")
        
    def start_timer(self):
        if not self.is_running:
            try:
                hours = int(self.hours_entry.get())
                minutes = int(self.minutes_entry.get())
                seconds = int(self.seconds_entry.get())
                
                if minutes >= 60 or seconds >= 60:
                    messagebox.showerror("Error", "Minutes and seconds must be less than 60")
                    return
                
                self.total_time = hours * 3600 + minutes * 60 + seconds
                if self.total_time <= 0:
                    messagebox.showerror("Error", "Please enter a positive time")
                    return
                
                self.remaining_time = self.total_time
                self.is_running = True
                self.paused = False
                
                self.start_button.config(state=tk.DISABLED)
                self.pause_button.config(state=tk.NORMAL)
                self.reset_button.config(state=tk.NORMAL)
                
                # Disable time inputs
                self.hours_entry.config(state=tk.DISABLED)
                self.minutes_entry.config(state=tk.DISABLED)
                self.seconds_entry.config(state=tk.DISABLED)
                
                # Start countdown in a separate thread
                threading.Thread(target=self.run_timer, daemon=True).start()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
    
    def run_timer(self):
        while self.remaining_time > 0 and self.is_running:
            if not self.paused:
                self.update_display()
                time.sleep(1)
                self.remaining_time -= 1
            else:
                time.sleep(0.1)
        
        if self.remaining_time <= 0 and self.is_running:
            self.timer_complete()
    
    def update_display(self):
        hours, remainder = divmod(self.remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.time_display.config(text=time_str)
        
        # Update progress bar
        progress_value = ((self.total_time - self.remaining_time) / self.total_time) * 100
        self.progress["value"] = progress_value
        
        # Flash when under 10 seconds
        if self.remaining_time <= 10:
            self.time_display.config(fg="red" if time.time() % 1 < 0.5 else "black")
    
    def pause_timer(self):
        if self.is_running:
            self.paused = not self.paused
            self.pause_button.config(text="Resume" if self.paused else "Pause")
            self.time_display.config(fg="blue" if self.paused else "black")
    
    def reset_timer(self):
        self.is_running = False
        self.paused = False
        self.remaining_time = 0
        
        self.time_display.config(text="00:00:00", fg="black")
        self.progress["value"] = 0
        
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="Pause")
        self.reset_button.config(state=tk.DISABLED)
        
        # Enable time inputs
        self.hours_entry.config(state=tk.NORMAL)
        self.minutes_entry.config(state=tk.NORMAL)
        self.seconds_entry.config(state=tk.NORMAL)
    
    def timer_complete(self):
        self.is_running = False
        self.time_display.config(fg="green")
        
        # Show message
        message = self.message_entry.get()
        messagebox.showinfo("Timer Complete", message)
        
        # Play sound if enabled
        if self.sound_var.get() == 1 and self.sound_enabled:
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.2)
        
        self.reset_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()