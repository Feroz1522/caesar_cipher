from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z']

caesar_status = True
while caesar_status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(direction,plain_text,shift_text):
        word = ""
        for char in plain_text:
            if char not in alphabet:
                word += char
            elif direction == 'encode':
                position = alphabet.index(char) + shift_text
                word += alphabet[position]
            elif direction =='decode':
                position = alphabet.index(char) - shift_text
                word += alphabet[position]
                
        print(f"The {direction} text is {word}.")
    caesar(direction,plain_text=text,shift_text=shift ) 
    response = input("Wanna try again type 'yes' or 'no'")
    if response == 'no':
        caesar_status = False