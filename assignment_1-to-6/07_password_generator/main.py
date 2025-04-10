import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import string
import pyperclip  # For copy to clipboard functionality
import secrets    # Cryptographically secure random generator

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("600x500")
        
        self.create_widgets()
        self.setup_layout()
        
    def create_widgets(self):
        # Password settings frame
        settings_frame = ttk.LabelFrame(self.root, text="Password Settings")
        settings_frame.pack(pady=10, padx=10, fill="x")
        
        # Length control
        ttk.Label(settings_frame, text="Length:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(settings_frame, from_=4, to=32, variable=self.length_var, 
                                     command=lambda e: self.length_display.config(text=str(self.length_var.get())))
        self.length_slider.grid(row=0, column=1, sticky="ew", padx=5)
        self.length_display = ttk.Label(settings_frame, text="12")
        self.length_display.grid(row=0, column=2, padx=5)
        
        # Character types
        self.upper_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="Uppercase (A-Z)", variable=self.upper_var).grid(
            row=1, column=0, columnspan=3, sticky="w", padx=5)
        
        self.digits_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="Digits (0-9)", variable=self.digits_var).grid(
            row=2, column=0, columnspan=3, sticky="w", padx=5)
        
        self.special_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(settings_frame, text="Special Characters (!@#)", variable=self.special_var).grid(
            row=3, column=0, columnspan=3, sticky="w", padx=5)
        
        # Strength presets
        ttk.Label(settings_frame, text="Presets:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.preset_var = tk.StringVar()
        presets = ttk.Combobox(settings_frame, textvariable=self.preset_var, 
                              values=["Custom", "Weak", "Medium", "Strong", "Very Strong"])
        presets.current(0)
        presets.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5)
        presets.bind("<<ComboboxSelected>>", self.apply_preset)
        
        # Generation controls
        ttk.Label(settings_frame, text="Number to generate:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.count_var = tk.IntVar(value=5)
        self.count_spin = ttk.Spinbox(settings_frame, from_=1, to=20, textvariable=self.count_var, width=5)
        self.count_spin.grid(row=5, column=1, sticky="w", padx=5)
        
        generate_btn = ttk.Button(settings_frame, text="Generate Passwords", command=self.generate_passwords)
        generate_btn.grid(row=5, column=2, padx=5)
        
        # Password output
        output_frame = ttk.LabelFrame(self.root, text="Generated Passwords")
        output_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.output_area = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_area.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Copy button
        copy_btn = ttk.Button(output_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)
        
        # Strength meter
        self.strength_meter = ttk.Progressbar(output_frame, orient="horizontal", length=200, mode="determinate")
        self.strength_meter.pack(pady=5)
        self.strength_label = ttk.Label(output_frame, text="Password Strength: -")
        self.strength_label.pack()
        
    def setup_layout(self):
        # Configure grid weights
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
    
    def apply_preset(self, event):
        preset = self.preset_var.get()
        if preset == "Weak":
            self.length_var.set(8)
            self.upper_var.set(False)
            self.digits_var.set(True)
            self.special_var.set(False)
        elif preset == "Medium":
            self.length_var.set(12)
            self.upper_var.set(True)
            self.digits_var.set(True)
            self.special_var.set(False)
        elif preset == "Strong":
            self.length_var.set(16)
            self.upper_var.set(True)
            self.digits_var.set(True)
            self.special_var.set(True)
        elif preset == "Very Strong":
            self.length_var.set(24)
            self.upper_var.set(True)
            self.digits_var.set(True)
            self.special_var.set(True)
        
        self.length_display.config(text=str(self.length_var.get()))
    
    def generate_passwords(self):
        length = self.length_var.get()
        use_upper = self.upper_var.get()
        use_digits = self.digits_var.get()
        use_special = self.special_var.get()
        count = self.count_var.get()
        
        # Validate settings
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters")
            return
        
        if not any([use_upper, use_digits, use_special]):
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        # Generate passwords
        passwords = []
        for _ in range(count):
            password = self.generate_single_password(length, use_upper, use_digits, use_special)
            passwords.append(password)
        
        # Display passwords
        self.output_area.delete(1.0, tk.END)
        for i, pwd in enumerate(passwords, 1):
            self.output_area.insert(tk.END, f"Password {i}: {pwd}\n")
        
        # Calculate and display strength
        self.calculate_strength(passwords[0])
    
    def generate_single_password(self, length, use_upper, use_digits, use_special):
        """Generate a single password with specified parameters"""
        chars = string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_special:
            chars += string.punctuation
        
        # Ensure at least one character from each selected category
        password = []
        if use_upper:
            password.append(secrets.choice(string.ascii_uppercase))
        if use_digits:
            password.append(secrets.choice(string.digits))
        if use_special:
            password.append(secrets.choice(string.punctuation))
        
        # Fill the rest with random characters
        remaining_length = length - len(password)
        password.extend(secrets.choice(chars) for _ in range(remaining_length))
        
        # Shuffle to avoid predictable patterns
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)
    
    def calculate_strength(self, password):
        """Estimate password strength (simple heuristic)"""
        length = len(password)
        complexity = 1  # base complexity for lowercase
        
        if any(c in string.ascii_uppercase for c in password):
            complexity += 1
        if any(c in string.digits for c in password):
            complexity += 1
        if any(c in string.punctuation for c in password):
            complexity += 1
        
        # Simple strength calculation
        strength = min(100, length * complexity * 2)
        self.strength_meter["value"] = strength
        
        # Descriptive label
        if strength < 40:
            level = "Weak"
        elif strength < 70:
            level = "Moderate"
        elif strength < 90:
            level = "Strong"
        else:
            level = "Very Strong"
        
        self.strength_label.config(text=f"Password Strength: {level} ({strength:.0f}/100)")
    
    def copy_to_clipboard(self):
        """Copy the generated passwords to clipboard"""
        content = self.output_area.get(1.0, tk.END).strip()
        if content:
            pyperclip.copy(content)
            messagebox.showinfo("Success", "Passwords copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No passwords to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()