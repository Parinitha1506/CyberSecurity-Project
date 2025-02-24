import cv2
import numpy as np

def decrypt_image(image_path):

    password = input("Enter the password to decrypt the image: ")
    # Read the encrypteimd image
    encrypted_image = cv2.imread(image_path)

    if encrypted_image is None:
        print("Error: Image not found.")
        return

    # Convert the encrypted image to grayscale
    gray_image = cv2.cvtColor(encrypted_image, cv2.COLOR_BGR2GRAY)

    # Initialize an empty string to store the binary message
    binary_message = ''

    # Reveal the binary message from the image
    for y in range(gray_image.shape[0]):
        for x in range(gray_image.shape[1]):
            # Get the pixel value
            pixel_value = gray_image[y, x]

            # Get the least significant bit of the pixel value
            binary_message += str(pixel_value & 1)

    # Look for the delimiter to stop decoding (the 16 bits marking the end of the message)
    delimiter = '1111111111111110'
    end_index = binary_message.find(delimiter)
    
    # If delimiter is found, trim the binary message up to the delimiter
    if end_index != -1:
        binary_message = binary_message[:end_index]

    # Convert the binary message to text
    secret_message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        secret_message += chr(int(byte, 2))

    # Return the secret message
    return secret_message

# Example usage
print(decrypt_image('encrypted_image.png'))



