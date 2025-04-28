# cara mendapatkan informasi mengenai citra

# import library opencv
import cv2

# pengaksesan file citra dengan argumen IMREAD_UNCHANGED
citra = cv2.imread(r"D:\Python\Gambar\saka.PNG", cv2.IMREAD_UNCHANGED)

# mendapatkan informasi mengenai citra, elemen pertama menyatakan jumlah baris citra,
# elemen kedua menyatakan jumlah kolom pada citra, elemen ketiga menyatakan jumlah kanal G, B, R
print(citra.shape)

