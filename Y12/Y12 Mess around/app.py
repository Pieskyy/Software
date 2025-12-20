import tkinter as tk

def on_button_click():
    label.config(text="OW :(")

root = tk.Tk()
root.title("Testing Grounds")

root.state("zoomed") # Open maximised window
root.configure(bg="black") # background

label = tk.Label(root, text="Please Dont click me", font=("Arial", 20), bg="black", fg="white") # Create a label
label.pack(pady=20)

button = tk.Button(root, text="PLEAAAASE DO NOT CLICK ME", command=on_button_click, font=("Arial", 16), bg="black", fg="white")# Create a button
button.pack()

root.mainloop()
