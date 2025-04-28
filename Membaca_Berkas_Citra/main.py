# program membaca berkas citra

# import library opencv
import cv2

# pengaksesan file citra
citra = cv2.imread(r"D:\Python\Gambar\saka.PNG")

# menampilkan citra pada layar
if not citra is None:
    cv2.imshow("Menampilkan Citra", citra)
    cv2.waitKey(0)