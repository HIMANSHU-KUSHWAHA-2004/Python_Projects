alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , ' ']
def encryption(plain_text,shift_key):
    encrypt_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_key
        if new_position > 26:
            new_position = new_position - 27
            encrypt_text += alphabet[new_position]
        else :
            encrypt_text += alphabet[new_position]
    print(f"The encrypted message is : \n")       
    print(encrypt_text)

def decryption(plain_text,shift_key):
    decrypt_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position - shift_key
        if new_position > 26:
            new_position = new_position - 26
            decrypt_text += alphabet[new_position]
        else :
            decrypt_text += alphabet[new_position]  
    print("The decrypted message is : \n")
    print(decrypt_text)

def main():
    text = input("Enter your message here : ").upper()
    what_to_do = input("For encryption then type 'encrypt' and 'decrypt' for decryption : ")
    while True:
        if what_to_do.lower() == "encrypt" or what_to_do.lower() == "e":
            key = int(input("Enter the Shift-key OR Set the Shift-key : "))
            encryption(text,key)
            break
        elif what_to_do.lower() == "decrypt" or what_to_do.lower() == "d":
            key = int(input("Enter the Shift-key OR Set the Shift-key : "))
            decryption(text,key)
            break
        else :
            print("Please enter a valid option")
            break
            
if __name__ == "__main__":
    main()