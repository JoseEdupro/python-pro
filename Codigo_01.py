meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
      
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("ya existe")
    else:
         meaning = input("Escribe el significado (¡con minusculas!): ")
         meme_dict[word] =  meaning
        
print(meme_dict)
