
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "EZ": "Çok Kolay Olan Bir Şeye Denir"
            }
if word in meme_dict.keys():
    print("kelime var")
else:
    print("kelime sözlükte yok")
    
