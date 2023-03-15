alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text,shift_num,choice):
    end_text=""
    if choice==decrypt:
       shift_num*=-1
    for letter in text:
        position=alphabet.index(letter)
        new_position=position+shift_num
           

new_cipher_text=[]
def encrypt(plain_text,shift_number):
  for letter in plain_text:
    position=alphabet.index(letter)
    new_position=position+shift_number
    new_cipher_text.append(alphabet[new_position])
  for i in new_cipher_text:
    print(i,end="")


new_decode_text=[]
def decrypt(cipher_text,shift_number):
  for letter in cipher_text:
    position=alphabet.index(letter)
    new_position=position-shift_number
    new_decode_text.append(alphabet[new_position])
  for i in new_decode_text:
    print(i,end="")
encrypt(text,shift)
decrypt(new_cipher_text,shift)    