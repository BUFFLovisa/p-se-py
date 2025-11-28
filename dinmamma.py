import tkinter as tk

inventory = []

main = tk.Tk()
main.title("Påsen")


main.configure(bg="#f4719b")


text_box = tk.Text(main, height=10, bg="#f2c0cc", fg="#dc3d66")
text_box.pack(padx=5, pady=5, fill="both")


input_frame = tk.Frame(main, bg="#f4719b")
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="Lägg till i påsen:", bg="#f4719b", fg="#dc3d66")
input_label.pack(side="left")

input_text = tk.Entry(input_frame, bg="#f2c0cc", fg="#dc3d66")
input_text.pack(side="left", padx=5)

def add_to_bag(event=None):
    if input_text.get() == "":
        text_box.insert(tk.END, "Du kan inte lägga till tomt i påsen.\n")
        return
    inventory.append(input_text.get())
    text_box.insert(tk.END, f"Du har lagt till {input_text.get()} i påsen.\n")
    input_text.delete(0, tk.END)

def show_bag(event=None):
    text_box.delete(1.0, tk.END)
    if not inventory:
        text_box.insert(tk.END, "Påsen är tom.\n")
    else:
        text_box.insert(tk.END, "I påsen hittar du:\n")
        text_box.insert(tk.END, "\n".join(inventory) + "\n")


button_frame = tk.Frame(main, bg="#f4719b")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Spara i påsen",
                       command=add_to_bag, bg="#f7a1bc" , fg="white")
add_button.pack(side="left", padx=5)

show_button = tk.Button(button_frame, text="Visa innehållet i påsen",
                        command=show_bag, bg="#f4719b" , fg="white")
show_button.pack(side="left", padx=5)

quit_button = tk.Button(button_frame, text="Avsluta",
                        command=quit, bg="#f35b8c" , fg="white")
quit_button.pack(side="left", padx=5)

main.mainloop()
