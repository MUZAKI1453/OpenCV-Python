# membaca berkas cira dalam skala ke abu-abuan

# import library opencv
import cv2

# pengaksesan file citra, dengan argumen skala ke abu-abuan
citra = cv2.imread(r"D:\Python\Gambar\saka.PNG", cv2.IMREAD_GRAYSCALE)

# menampilkan citra pada layar
if not citra is None:
    cv2.imshow("Berkas Citra dalam Skala Ke abu - abuan", citra)
    cv2.waitKey(0)
