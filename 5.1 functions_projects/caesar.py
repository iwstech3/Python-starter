import string
# letters from a to z
alphabet=list(string.ascii_lowercase + string.ascii_lowercase)
shift= int(input("Enter the shift value: "))
text=input("Enter the text to process")
direction=input("Type 'encode' to encrypt and 'decode' to decrypt")
# print(alphabet)

def encrypt(text_input, shift_amount):
    final_text=""
    for letter in text_input:
        # get the index of each letter in my alphabet
        position=alphabet.index(letter)
        new_position=position + shift_amount
        new_text=alphabet[new_position]
        final_text+=new_text
    print(f"The encrypted value is {final_text}")
    
    
    
def decrypt(text_input, shift_amount):
    final_text=""
    for letter in text_input:
        # get the index of each letter in my alphabet
        position=alphabet.index(letter)
        new_position=position - shift_amount
        new_text=alphabet[new_position]
        final_text+=new_text
    print(f"The decrypted value is {final_text}")
    
    
if direction=="encode":
    encrypt(text, shift)
elif direction=="decode":
    decrypt(text, shift)
else:
    print("direction not found")
    
    

