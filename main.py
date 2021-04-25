import os
import cv2
import face_recognition as fr
import numpy as np

pathlib = 'ImagesAttendance'
images = []
Names = []
myList = os.listdir(pathlib)
print(myList)
for cl in myList:
    currImg = cv2.imread(f'{pathlib}/{cl}')
    images.append(currImg)
    Names.append(os.path.splitext(cl)[0])
print(Names)

def DbEncodings(images):
    encList = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        enc = fr.face_encodings(image)[0]
        encList.append(enc)
    return encList

def Attendance(name):
    with open('Attendance_Register.csv', 'r+') as f:
        DataList = f.readlines()
        names = []
        for data in DataList:
            ent = data.split(',')
            names.append(ent[0])
        if name not in names:
            # curr = datetime.now()
            # dt = curr.strftime('%H:%M:%S')
            st = 'Present'
            f.writelines(f'\n{name}, {st}')

encodeKnown = DbEncodings(images)
print('Encoding Complete')

facesInFrame=[]
face_names=[]
process_this_frame=True
cap = cv2.VideoCapture(0)

while True:
    _, img= cap.read()
    image = cv2.resize(img,(0,0),None,0.25,0.25)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    facesInFrame = fr.face_locations(image)
    encodesInFrame = fr.face_encodings(image,facesInFrame)
    if process_this_frame:
        face_names=[]
        for encodeFace,faceLoc in zip(encodesInFrame, facesInFrame):
            matchList = fr.compare_faces(encodeKnown, encodeFace)
            faceDist = fr.face_distance(encodeKnown, encodeFace)
            match = np.argmin(faceDist)
            name="unknown"
            if matchList[match]:
                name = Names[match].upper()
                Attendance(name)
            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(facesInFrame, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        if name != "unknown":
            cv2.putText(img, name+" is present", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        else:
            cv2.putText(img, name , (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
    cv2.imshow('Video', img)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

