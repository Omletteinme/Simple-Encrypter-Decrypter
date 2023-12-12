import tkinter as tk
from tkinter import ttk, messagebox

def encrypt_text(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt_text(text, shift):
    return encrypt_text(text, -shift)

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def show_popup(message):
    messagebox.showinfo("Notification", message)

def process_text():
    user_text = text_entry.get("1.0",'end-1c')
    user_choice = choice_var.get()

    if user_choice.lower() == 'encrypt':
        encrypted_text = encrypt_text(user_text, shift=3)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, encrypted_text)
        write_to_file("encrypted_decrypted_texts.txt", f"Encrypted: {encrypted_text} (Original: {user_text})")
        show_popup("Your encryption has been stored in encrypted_decrypted_texts.txt")

    elif user_choice.lower() == 'decrypt':
        decrypted_text = decrypt_text(user_text, shift=3)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, decrypted_text)
        write_to_file("encrypted_decrypted_texts.txt", f"Decrypted: {decrypted_text} (Original: {user_text})")
        show_popup("Your decryption has been stored in encrypted_decrypted_texts.txt")

    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error: Invalid choice. Please enter 'encrypt' or 'decrypt'.")
        result_entry.config(state=tk.NORMAL)  # Make entry editable in case of error

# Create the main window
root = tk.Tk()
root.title("Text Encryptor/Decryptor")

# Text input
text_label = ttk.Label(root, text="Enter the text:")
text_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=1, column=0, padx=10, pady=5)

# Choice input
choice_label = ttk.Label(root, text="Choose 'encrypt' or 'decrypt':")
choice_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
choice_var = tk.StringVar()
choice_combobox = ttk.Combobox(root, textvariable=choice_var, values=['Encrypt', 'Decrypt'])
choice_combobox.grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Result entry
result_label = ttk.Label(root, text="Result:")
result_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
result_entry = ttk.Entry(root, width=40)
result_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')

# Process button
process_button = ttk.Button(root, text="Process", command=process_text)
process_button.grid(row=6, column=0, padx=10, pady=10)

# Run the main loop
root.mainloop()
