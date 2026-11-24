meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "DELULU": "Cuando alguien está loco",
            "SHEESH": "ligera desaprobación",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
        if word == "CRINGE":
            print("CRINGE - Algo excepcionalmente raro o embarazoso")
        if word == "LOL":
            print("LOL - Una respuesta común a algo gracioso")
        if word == "DELULU":
            print("DELULU - Cuando alguien está loco")
        if word == "SHEESH":
            print("SHEESH - ligera desaprobación")
else:
    # ¿Qué hacer si no se encuentra la palabra?
        print("palabra no esta en la datos")
