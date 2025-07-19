def encript(text,key):
    result=""
    for char in text:
        if char.isalpha():
            base_ascii = ord("A") if char.isupper() else ord("a")
            shifted = ((ord(char) - base_ascii) + key) % 26 + base_ascii 
            result += chr(shifted)
        else:
            result += char

    return result

def decript(text,key):
    return encript(text,-key)


print("---- Welcome to the caesar Cipher Script ----\n")    

choice = input("Enter you Choice 'E' for encript and 'D' for decript: ").strip().lower()

if choice == 'e':
    try:
        text = input("Enter the text for Encript: ")
        key = int(input("Enter the Number for rotaiton: "))
        encript_txt = encript(text,key)
        print(f"This is the Encript Text: {encript_txt}")
    except ValueError:
        print("Invaild Input for Key")

elif choice == 'd':
    try:
        text = input("Enter the text for Encript: ")
        key = int(input("Enter the Number for rotaiton: "))
        decript_txt = decript(text,key)
        print(f"This is the Original Text: {decript_txt}")
    except ValueError:
        print("Invaild Input for Key")

else:
    print("invalid choice ")        

