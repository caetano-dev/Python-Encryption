print(
    "\nWelcome to the Encryption algorythm\n Usage:\n encrypt [MESSAGE]\n decrypt [MESSAGE] \n")


def encrypt(message):
    encrypted_message = ""
    for letter in message:
        encrypted_message += chr(ord(letter) + 5)
    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    for letter in message:
        decrypted_message += chr(ord(letter) - 5)
    return decrypted_message


def get_message():
    message = input("")
    if message[0:7] == "encrypt":
        print(f"Encrypted message: {encrypt(message[7:])}\n")
    elif message[0:7] == "decrypt":
        print(f"Decrypted message: {decrypt(message[7:])}\n")
    else:
        print("Invalid command\n")

    print("New command:\n")
    get_message()

get_message()
