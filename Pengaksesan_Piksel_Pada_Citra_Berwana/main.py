# pengaksesan piksel pada citra berwarna

# import library opencv
import cv2

# pengaksesan file citra
citra = cv2.imread(r"D:\Python\Gambar\saka.PNG")

# pengaksesan piksel pada citra dengan menyatakan komponen dalam bentuk B, G, R
# bentuk pengaksesanya =  citra[index_baris, index_kolom]
piksel = citra[0,0]
print("B G R = ", piksel)

# ini contoh pengaksesan data warna perkomponen
piksel = citra[0,0] [0] # Blue
print("\nnilai warna biru = ", piksel)

piksel = citra[0,0] [1] #Green
print("nilai warna hijau = ", piksel)

piksel = citra[0,0] [2] # Red
print("nilai warna merah = ", piksel)