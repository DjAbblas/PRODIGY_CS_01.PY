import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def scramble_pixels(image_array):
    np.random.shuffle(image_array.flat)
    return image_array

def unscramble_pixels(image_array):
    return np.sort(image_array.flat).reshape(image_array.shape)

def encrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            image_array = np.array(image)
            scrambled_array = scramble_pixels(image_array)
            scrambled_image = Image.fromarray(scrambled_array)
            encrypted_image_path = file_path.split('.')[0] + "_encrypted.png"
            scrambled_image.save(encrypted_image_path)
            messagebox.showinfo("Success", "Image encrypted successfully.\nEncrypted image saved as: " + encrypted_image_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def decrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            image_array = np.array(image)
            unscrambled_array = unscramble_pixels(image_array)
            unscrambled_image = Image.fromarray(unscrambled_array)
            decrypted_image_path = file_path.split('_encrypted')[0] + "_decrypted.png"
            unscrambled_image.save(decrypted_image_path)
            messagebox.showinfo("Success", "Image decrypted successfully.\nDecrypted image saved as: " + decrypted_image_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=10)

# Start the GUI
root.mainloop()
