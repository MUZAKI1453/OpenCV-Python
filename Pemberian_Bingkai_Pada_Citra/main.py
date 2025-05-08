# Pemberian bingkai pada citra

# import library opencv
import cv2

# Pengaksesan citra
citra = cv2.imread(r"D:\Python\Gambar\Timnas_2.jpg")

# Copy / salin isi citra
hasil = citra.copy()

# pengolahan citra
TEBAL = 20
HITAM = 0

jumbaris = hasil.shape[0]
jumkolom = hasil.shape[1]

# membuat bingkai diatas
for baris in range(TEBAL):
    for kolom in range(jumkolom):
        hasil[baris, kolom] = HITAM

# membuat bingkai dibawah
for baris in range(jumbaris - TEBAL - 1, jumbaris):
    for kolom in range(jumkolom):
        hasil[baris, kolom] = HITAM

# membuat bingkai di kiri
for baris in range(TEBAL, jumbaris - TEBAL - 1):
    for kolom in range(TEBAL):
        hasil[baris, kolom] = HITAM

#  membuat bingkai di kanan
for baris in range(TEBAL, jumbaris - TEBAL - 1):
    for kolom in range(jumkolom - TEBAL - 1, jumkolom):
        hasil[baris, kolom] = HITAM

# menampilkan gambar asal dan gambar hasil
cv2.imshow("Gambar asal", citra)
cv2.imshow("Gambar hasil", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()