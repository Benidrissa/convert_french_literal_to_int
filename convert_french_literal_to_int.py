import re


liste_chiffre = ["aucun","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix",
        "onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf","vingt",
        "vingt-un","vingt-deux","vingt-trois","vingt-quatre","vingt-cinq","vingt-six","vingt-sept","vingt-huit","vingt-neuf",
        "trente","trente-un","trente-deux","trente-trois","trente-quatre","trente-cinq","trente-six","trente-sept","trente-huit","trente-neuf",
        "quarante","quarante-un","quarante-deux","quarante-trois","quarante-quatre","quarante-cinq","quarante-six","quarante-sept","quarante-huit","quarante-neuf",
        "cinquante","cinquante-un","cinquante-deux","cinquante-trois","cinquante-quatre","cinquante-cinq","cinquante-six","cinquante-sept","cinquante-huit","cinquante-neuf",
        "soixante","soixante-un","soixante-deux","soixante-trois","soixante-quatre","soixante-cinq","soixante-six","soixante-sept","soixante-huit","soixante-neuf",
        "soixante-dix","soixante-onze","soixante-douze","soixante-treize","soixante-quatorze","soixante-quinze","soixante-seize","soixante-dix-sept","soixante-dix-huit","soixante-dix-neuf",
        "quatre-vingt-un","quatre-vingt-deux","quatre-vingt-trois","quatre-vingt-quatre","quatre-vingt-cinq","quatre-vingt-six","quatre-vingt-sept","quatre-vingt-huit","quatre-vingt-neuf","quatre-vingt-dix",
        "quatre-vingt-onze","quatre-vingt-douze","quatre-vingt-treize","quatre-vingt-quatorze","quatre-vingt-quinze","quatre-vingt-seize","quatre-vingt-dix-sept","quatre-vingt-dix-huit","quatre-vingt-dix-neuf"]        
print("recovered:")

v_test = ["deux cent quatre-vingt-dix-sept","trois cent quarante-trois","cent dix-huit","cent","soixante-dix","neuf-cent quatre-vingt-dix-neuf","quatre-vingt-neuf","deux"]

def normalize_number(s_number):
    v_number = re.split(r"cent",s_number.replace("-"," "))
    v_number.reverse()
    return v_number

def centaine(s_number):
    if s_number == "":
        s_number = "un"
    return liste_chiffre.index(s_number)*100

def dizaine(s_number):
    number = 0
    if s_number == "":
        number = liste_chiffre.index("aucun")
    else:
        v_number = s_number.split(" ")
        if len(v_number) == 1: ## unité en 1 mot
            number = liste_chiffre.index(v_number[0].strip(" "))
        if len(v_number) == 2: ## unité et dizaine en 2 mots
            number = liste_chiffre.index(v_number[0].strip(" "))+liste_chiffre.index(v_number[1].strip(" "))
        if len(v_number) == 3: ## unité et dizaine en 3 mots
            number = liste_chiffre.index(v_number[0].strip(" "))*liste_chiffre.index(v_number[1].strip(" "))+\
            liste_chiffre.index(v_number[2].strip(" "))
        if len(v_number) == 4: ## unité et dizaine en 4 mots
            number = liste_chiffre.index(v_number[0].strip(" "))*liste_chiffre.index(v_number[1].strip(" "))+\
            liste_chiffre.index(v_number[2].strip(" "))+liste_chiffre.index(v_number[3].strip(" "))
    return number

def convert_literal_to_int(s_number):
    v_number = normalize_number(s_number)
    nombre = 0
    if len(v_number) == 2: ## centaine disponible: pour les nombres < 1000
        nombre = centaine(v_number[1].strip(" "))
        nombre = nombre + dizaine(v_number[0].strip(" "))
    else:
        nombre = nombre + dizaine(v_number[0].strip(" "))
    return nombre


#test
for n in v_test:
    v_number = normalize_number(n)
    print(v_number)
    
    #test conversion
    nombre = 0
    if len(v_number) == 2: ## centaine disponible: pour les nombres < 1000
        nombre = centaine(v_number[1].strip(" "))
        print(nombre," centaine")
        nombre = nombre + dizaine(v_number[0].strip(" "))
        print(dizaine(v_number[0].strip(" ")))
        print(nombre)
    else:
        nombre = nombre + dizaine(v_number[0].strip(" "))
        print(dizaine(v_number[0].strip(" ")))
        print(nombre)

for n in v_test:
    print(convert_literal_to_int(n))


