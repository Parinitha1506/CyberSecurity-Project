import cv2
import numpy as np

def encrypt_image(image_path):
    

    secret_message = input("Enter a secret message: ")
    password = input("Enter a password for encryption: ")
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert the secret message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_message += '1111111111111110'  # Add delimiter to mark end of the message

    # Hide the binary message in the image
    data_index = 0
    for y in range(gray_image.shape[0]):
        for x in range(gray_image.shape[1]):
            if data_index < len(binary_message):
                pixel_value = gray_image[y, x]

                # Hide the binary message in the least significant bit
                if binary_message[data_index] == '1':
                    pixel_value = (pixel_value & ~1) | 1
                else:
                    pixel_value = (pixel_value & ~1) | 0

                # Update the pixel value
                gray_image[y, x] = pixel_value
                data_index += 1
            else:
                break

    # Convert the grayscale image back to BGR
    encrypted_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    # Save the encrypted image
    cv2.imwrite('encrypted_image.png', encrypted_image)
    print("Image encrypted and saved as 'encrypted_image.png'.")

# Example usage
encrypt_image('C:\\Users\\lenovo\\Documents\\cybersercurity Project\\mypic.jpg.jpg')
