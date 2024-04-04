import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            encrypted_image = swap_pixels(image)
            encrypted_image_path = save_image_with_suffix(encrypted_image, file_path, "_encrypted")
            messagebox.showinfo("Success", f"Image encrypted successfully.\nEncrypted image saved as: {encrypted_image_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def decrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            decrypted_image = swap_pixels(image)  # Decrypting is done the same way as encrypting
            decrypted_image_path = save_image_with_suffix(decrypted_image, file_path, "_decrypted")
            messagebox.showinfo("Success", f"Image decrypted successfully.\nDecrypted image saved as: {decrypted_image_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def swap_pixels(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (g, b, r))  # Swapping RGB values
    return image

def save_image_with_suffix(image, file_path, suffix):
    file_name, extension = file_path.split('.')
    new_file_path = f"{file_name}{suffix}.{extension}"
    image.save(new_file_path)
    return new_file_path

# Create main window
root = tk.Tk()
root.title("Image Encryption & Decryption")

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=10)

# Start the GUI
root.mainloop()
