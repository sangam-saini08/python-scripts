import string
import random   
import getpass


def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")        
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")        
    if not any(c.isdigit() for c in password):
        issues.append("Missing digits")  
    if not any (c in string.punctuation for c in password):
        issues.append("Missing special characters")          
    return issues

def generate_strong_password(length=12):
    if not 7 < length < 25  :
        return ""

    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    digits_num = string.digits
    punchuation = string.punctuation

    strong_password = ""

    for _ in range(int(length/4)):
        a = random.choice(lower_char)
        strong_password = strong_password + a
        b = random.choice(upper_char)
        strong_password = strong_password + b
        c = random.choice(digits_num)
        strong_password = strong_password + c
        d = random.choice(punchuation)
        strong_password = strong_password + d

    return strong_password    



def password_checker_genrator():
    print("---- Welcome to the Password Checker and Genrator app ----\n")
    while True:
        password = getpass.getpass("Enter a Strong Password :")
        issues = check_password_strength(password)
        if len(issues) == 0:
            print("Your Password is Very Strong ✅")
            break
            
        for issue in issues:
            print(f"- {issue} ❌")
        sugested_pass = generate_strong_password()    
        print(f"Your suggested Strong Password : {sugested_pass}")       

password_checker_genrator()        