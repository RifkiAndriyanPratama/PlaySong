import pywhatkit

try:
    lagu = input("masukkan nama lagu: ")
    pywhatkit.playonyt(lagu)
    print("lagu: ", lagu)
    print("Berhasil diputar")
except:
    print("video tidak dapat diputar")