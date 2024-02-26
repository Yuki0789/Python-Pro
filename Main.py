meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "Tanggapan terhadap lelucon",
            "SHEESH" : "Sedikit ketidaksetujuan",
            "CREEPY" : "Menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Kata yang Kamu cari:", word)
    print("Terjemahannya adalah: ", meme_dict.get(word))
else:
    print("Kata tidak ada")
