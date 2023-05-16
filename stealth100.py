from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)


# Define functions for encrypting and decrypting messages
def encrypt_message(message):
  encrypted_message = fernet.encrypt(message.encode())
  return encrypted_message


def decrypt_message(encrypted_message):
  decrypted_message = fernet.decrypt(encrypted_message).decode()
  return decrypted_message


# Define a function for sending a message
def send_message():
  print("Enter message:")
  message = input()
  encrypted_message = encrypt_message(message)
  print("Encrypted message: " + encrypted_message.decode())
  input("Press Enter to continue...")


# Define a function for receiving a message
def receive_message():
  print("Enter encrypted message:")
  encrypted_message = input()
  try:
    decrypted_message = decrypt_message(encrypted_message.encode())
    print("Decrypted message: " + decrypted_message)
  except:
    print("Error: Invalid encrypted message.")
  input("Press Enter to continue...")


# Define the main function for the UI
def main():
  while True:
    print(
      "Enter 's' to send a message, 'r' to receive a message, or 'q' to quit.")

    key = input()

    if key.lower() == 'q':
      break
    elif key.lower() == 's':
      send_message()
    elif key.lower() == 'r':
      receive_message()


# Run the main function
if __name__ == '__main__':
  main()
