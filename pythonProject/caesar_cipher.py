alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, s):
    cipher_text = " "
    for char in text:
        position = alphabet.index(char)
        new_position = (position + s)%26
        cipher_text += alphabet[new_position]
    print(f"Here is the text after encryption: {cipher_text}")
def decrypt(text, s):
    cipher_text = " "
    for char in text:
        position = alphabet.index(char)
        new_position = (position - s)%26
        cipher_text += alphabet[new_position]
    print(f"Here is the text after encryption: {cipher_text}")


choice = input("chose encrypt or decrypt: ")
text = input("Enter text: ")
s = int(input("Shift pattern: "))
if choice == "encrypt":
    encrypt(text=text, s=s)
elif choice == "decrypt":
    decrypt(text=text, s=s)
