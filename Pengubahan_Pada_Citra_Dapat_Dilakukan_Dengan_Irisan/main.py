# Pengubahan Pada Citra Dapat Dilakukan Dengan Irisan

# import library opencv
import cv2

# pengaksesan file
citra = cv2.imread(r"D:\Python\Gambar\Timnas.jpeg")

# mendapatkan informasi mengenai citra, elemen pertama menyatakan jumlah baris citra,
# elemen kedua menyatakan jumlah kolom pada citra, elemen ketiga menyatakan jumlah kanal G, B, R
print(citra.shape)

# mengubah warna pada citra dengan irisan
#     baris, kolom,   warna dalam BGR
citra[0:250, 0:250] = [23, 122, 23]

# menampilkan hasil citra dengan irisan yang sudah diganti warnanya
cv2.imshow("Hasil", citra)
cv2.waitKey(0)