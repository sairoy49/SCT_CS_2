# 🖼️ Image Encryption Tool using Pixel Manipulation

This project is part of my internship at **SkillCraft Technology**. The goal of this task was to build a simple image encryption and decryption tool using basic pixel-level operations like XOR.

## 🔐 What It Does

- Encrypts an image using XOR operation on each pixel's RGB values
- Decrypts the encrypted image using the same XOR key
- Helps understand low-level image manipulation and basic cryptography concepts

## 🛠️ Technologies Used

- Python 🐍
- Pillow (PIL) for image handling
- NumPy for array manipulation

## 📸 How It Works

1. Load an image (preferably `.jpg` or `.png`)
2. Apply XOR operation on each pixel using a user-defined key
3. Save the encrypted image
4. Decrypt it by applying the same XOR operation again

## 💡 Example

```python
input_image = "original.png"
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"
encryption_key = 123  # Key must be between 0-255

encrypt_decrypt_image(input_image, encrypted_image, encryption_key, mode="encrypt")
encrypt_decrypt_image(encrypted_image, decrypted_image, encryption_key, mode="decrypt")
