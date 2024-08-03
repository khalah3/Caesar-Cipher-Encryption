alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as def encrypt(plain_text, shift_amount):
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#   encrypt(plain_text = text, shift_amount= shift)
  
# elif direction == "decode":
#   decrypt(cipher_text = text,shift_amount=shift)

#Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar (message, shift_amount, cipher_direction):
   encode_decode = ""
   code=""
   for letter in message:
     if letter not in alphabet:
       code+=letter
   
     elif cipher_direction == "encode":
       position=alphabet.index(letter)
       newposition= position+shift_amount%26
       encode_decode="True"
       code+=alphabet[newposition]
       
     elif cipher_direction == "decode":
       position=alphabet.index(letter)
       newposition=position-shift_amount%26
       encode_decode="False"
       code+=alphabet[newposition]
     
   if encode_decode == "True":
     print(f"The encoded text is: {code}")
   elif encode_decode == "False":
     print(f"The decoded text is: {code}")
   
   

caesar(text,shift,direction)


print("Do you want to do this again?Yes or No?\n")
repeat=input()


while repeat.lower()=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  repeat=input(print("Do you want to do this again?\n"))

   

  
  


print("Goodbye")
