import tkinter as tk
from tkinter import messagebox

# ------------------ BMI Logic ------------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category, tip, scale, color = "Underweight", "Need to gain weight. Consult a pro.", "BMI Scale: [■□□□□]", "#F59E0B"
        elif bmi < 25:
            category, tip, scale, color = "Normal", "Healthy range. Keep it up!", "BMI Scale: [■■■□□]", "#10B981"
        elif bmi < 30:
            category, tip, scale, color = "Overweight", "Consider diet and exercise.", "BMI Scale: [■■■■□]", "#F97316"
        else:
            category, tip, scale, color = "Obese", "Health risk! Seek medical advice.", "BMI Scale: [■■■■■]", "#EF4444"

        result_label.config(text=f"BMI Score: {bmi}", fg=color)
        category_label.config(text=category, fg=color)
        tip_label.config(text=tip)
        scale_label.config(text=scale, fg=color)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

def reset_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="BMI Score: --", fg="#EC4899")
    category_label.config(text="Category: --", fg="#475569")
    tip_label.config(text="")
    scale_label.config(text="")

# ------------------ UI Setup ------------------
root = tk.Tk()
root.title("Peach BMI Calculator")
root.geometry("900x780")
root.config(bg="#FFE4E6")  # Peach pink background

# Main Card
main_card = tk.Frame(root, bg="#FFF7ED", padx=90, pady=35, highlightthickness=1, highlightbackground="#FBCFE8")
main_card.place(relx=0.5, rely=0.5, anchor="center")

# Header
header_section = tk.Frame(main_card, bg="#FFF7ED")
header_section.pack(fill=tk.X)

tk.Label(header_section, text="BMI Tracker", font=("Segoe UI", 32, "bold"),
         fg="#EC4899", bg="#FFF7ED").pack()
tk.Label(header_section, text="Your Personal Health Analyzer",
         font=("Segoe UI", 11), fg="#9F1239", bg="#FFF7ED").pack(pady=(4, 18))

# Inputs
weight_label = tk.Label(main_card, text="Weight (kg)", font=("Segoe UI", 12, "bold"), fg="#9F1239", bg="#FFF7ED")
weight_label.pack(anchor="w")
weight_entry = tk.Entry(main_card, font=("Segoe UI", 16), justify="center",
                        bd=0, bg="#FFE4E6", fg="#9F1239", insertbackground="#9F1239",
                        highlightbackground="#F472B6", highlightthickness=2)
weight_entry.pack(fill=tk.X, pady=(4, 18), ipady=10)

height_label = tk.Label(main_card, text="Height (m)", font=("Segoe UI", 12, "bold"), fg="#9F1239", bg="#FFF7ED")
height_label.pack(anchor="w")
height_entry = tk.Entry(main_card, font=("Segoe UI", 16), justify="center",
                        bd=0, bg="#FFE4E6", fg="#9F1239", insertbackground="#9F1239",
                        highlightbackground="#F472B6", highlightthickness=2)
height_entry.pack(fill=tk.X, pady=(4, 20), ipady=10)

# Buttons
btn_container = tk.Frame(main_card, bg="#FFF7ED")
btn_container.pack(fill=tk.X)

calc_btn = tk.Button(btn_container, text="Calculate Now", font=("Segoe UI", 14, "bold"),
                     bg="#EC4899", fg="white", relief="flat", cursor="hand2", command=calculate_bmi)
calc_btn.pack(fill=tk.X, ipady=12, pady=6)

secondary_btns = tk.Frame(btn_container, bg="#FFF7ED")
secondary_btns.pack(fill=tk.X, pady=6)

reset_btn = tk.Button(secondary_btns, text="Reset", font=("Segoe UI", 11),
                      bg="#FBCFE8", fg="#9F1239", relief="flat", command=reset_fields, width=15)
reset_btn.pack(side=tk.LEFT, padx=(0, 6), ipady=7)

exit_btn = tk.Button(secondary_btns, text="Exit App", font=("Segoe UI", 11),
                     bg="#FB7185", fg="white", relief="flat", command=root.destroy, width=15)
exit_btn.pack(side=tk.RIGHT, padx=(6, 0), ipady=7)

# Results
results_section = tk.Frame(main_card, bg="#FFF7ED", pady=12)
results_section.pack(fill=tk.X)

result_label = tk.Label(results_section, text="BMI Score: --", font=("Segoe UI", 24, "bold"), fg="#EC4899", bg="#FFF7ED")
result_label.pack()
category_label = tk.Label(results_section, text="Category: --", font=("Segoe UI", 15), fg="#475569", bg="#FFF7ED")
category_label.pack()
scale_label = tk.Label(results_section, text="", font=("Consolas", 14), fg="#EC4899", bg="#FFF7ED")
scale_label.pack(pady=5)
tip_label = tk.Label(results_section, text="", font=("Segoe UI", 10, "italic"), fg="#9F1239", bg="#FFF7ED", wraplength=400)
tip_label.pack(pady=5)

root.bind("<Return>", lambda e: calculate_bmi())
root.mainloop()
