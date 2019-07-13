
# Menampilkan String

text1 = 'saya adalah rizky khapidsyah'
text2 = 'lahir di hari jum\'at'
text3 = "Merupakan orang Medan"
print(text1 + " " + text2 + "\n" + text3 + "\n\n")

# Multiline
text4 = """
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Unicode data files and any associated documentation
(the "Data Files") or Unicode software and any associated documentation
(the "Software") to deal in the Data Files or Software
without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, and/or sell copies of
the Data Files or Software, and to permit persons to whom the Data Files
or Software are furnished to do so, provided that either
(a) this copyright and permission notice appear with all copies
of the Data Files or Software, or
(b) this copyright and permission notice appear in associated
Documentation.
"""
print(text4)


# Penggunaan RAW String
text5 = r'Data tersebut berada di direktory C:\nyanyian\Lagu\MP3' # r merupakan raw string
print(text5 + "\n")

# Mengakses Array String
text6 = "Aku Sangat Menyayanginya"  #Array dimulai dari 0 terurut dari kiri, dan minus (-) terurut jika dari kanan
print(text6[2] + "\n")              #Mencetak karater 'u'
print(text6[0:5] + "\n")            #Mencetak karakter 1 sampai 5





