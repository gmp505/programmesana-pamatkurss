apaksa = 1
augsa = 100
minejumi = 0

while apaksa <= augsa:
    minejums = (apaksa + augsa) // 2
    minejumi += 1

    atbilde = input(
        f"Vai tavs skaitlis ir {minejums}? "
        "(lielaks/mazaks/pareizi): "
    ).strip().lower()
    

    if atbilde == "pareizi":
        print(f"Uzvara! Dators uzmineja {minejumi} minejumos!")
        break

    elif atbilde == "lielaks":
        apaksa = minejums + 1

    elif atbilde == "mazaks":
        augsa = minejums - 1

    else:
        print("Nepareiza ievade! Megini velreiz.")

    if apaksa > augsa:
        print("Pretrunigas atbildes! Tu esi krapies!")
        break