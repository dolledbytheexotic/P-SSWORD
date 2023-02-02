import re 
Upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols=["!", "@","#","$","%","^","&","*","(",")","_","+","-","=","{","}" ,]
numbers=["1","2","3","4","5","6","7","8","9","0",]
 
all=Upper + lower + symbols 

all_numbers=numbers

password=input("Enter your password:")

letter_count = len(re.findall(r"[a-zA-Z]", password))

number_count = len(re.findall(r"\d", password))

symbol_count = len(re.findall(r"[!@#\$%^&*()_\-+={}|;:<,>.?/]", password))

if letter_count > 3:
    print("Password should not contain more than 3 letters.")

elif number_count > 3:

  print("Password should not contain more than 3 numbers.")

elif symbol_count > 3:
  
  print("Password should not contain more than 3 symbols.")

elif any(char not in all_chars for char in password):

  print("Password should only contain letters, numbers, and symbols.")

else:
    print("Password accepted.")
