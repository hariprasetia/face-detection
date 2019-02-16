import cv2

cap = cv2.VideoCapture(0)
 # Set lebar
cap.set(3, 640)
 # Set tinggi
cap.set(4, 480)

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

while(True):
    # Capture setiap frame dari kamera perekam
    ret, frame = cap.read()
    # Pengoperasian frame yang sudah di-capture
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        continue
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Menampilkan hasil dari frame
    for (x,y,w,h) in faces:
        # Set frame kotak deteksi wajah
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
             # set fram kotak deteksi mata
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tampilkan hasil capture dari kamera perekam
cap.release()
cv2.destroyAllWindows()
