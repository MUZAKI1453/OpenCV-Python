# Penggunaan Irisan Untuk Memilih Area Dalam Citra
# menggunakan irisan untuk mengakses sekumpulan piksel

# import library opencv python
import cv2

# pengaksesan file citra
citra = cv2.imread(r"D:\Python\Gambar\Timnas.jpeg", -1) # irisan ini berarti dari m hingga n-1

# melihat informasi dari citra
# mendapatkan informasi mengenai citra, elemen pertama menyatakan jumlah baris citra,
# elemen kedua menyatakan jumlah kolom pada citra, elemen ketiga menyatakan jumlah kanal G, B, R
print(citra.shape)

# penggunaan irisan untuk mengakses sekumpulan piksel
bagian = citra[0:410, 0:200]

# menampilkan irisan dalam citra
cv2.imshow("Irisan", bagian)
cv2.waitKey(0)