from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key, mode="encrypt"):
   
    img = Image.open(input_path).convert('RGB')
    data = np.array(img)

    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            r, g, b = data[row, col]
            if mode == "encrypt":
                data[row, col] = [r ^ key, g ^ key, b ^ key]
            elif mode == "decrypt":
                data[row, col] = [r ^ key, g ^ key, b ^ key]

    
    result_img = Image.fromarray(data)
    result_img.save(output_path)
    print(f"Image {mode}ed and saved to {output_path}")


input_image = "/content/WhatsApp Image 2025-06-03 at 11.52.10_0d1c17a3.jpg"        
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"
encryption_key = 123             

# Encrypt the image
encrypt_decrypt_image(input_image, encrypted_image, encryption_key, mode="encrypt")

# Decrypt the image
encrypt_decrypt_image(encrypted_image, decrypted_image, encryption_key, mode="decrypt")
