import re

def mot():
    phrase = input("type a sentence :")
    m = input("type a world :")
    search1 = re.search(r"[A-Z]|[a-z]", m)
    if m :
        print("true")
    else:
        print("false")


def number():
    phrase = input("type a sentence :")
    search2 = re.search(r"[0-9]", phrase)
    if search2 :
        print("true")
    else :
        print("false")

def espace():
    phrase = input("type a sentence :")
    x = phrase.replace(" ","_")
    print(x)

def nbrPhone():
    phone = (input("type de phone numbre :"))
    search3 = re.search(r"\d{2}+\s+\d{3}+\s+\d{3}",phone)
    if search3:
        print("correct")
    else:
        print("incorrect")

def email():
    em = input("type the email :")
    search4 = re.search(r"[a-z]|[A-Z]{3;}+@domaine.com",em)
    if search4:
        print("correct")
    else:
        print("incorrect")



