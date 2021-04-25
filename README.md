# Face-Recognition-Attendence-System

***As now a days most of the classes and other are happening online so to make it easier for the management... it would be better to help them through attendence like this***

***It's a prettu simple concept and very much self explanatory... Whenever the camera detects a face that which it has been trained with the original photos then it will directly mark that person's name(the name on the original image) as "Present" into a "Attendance.csv" file***

*Without using any database the attendance of everyperson can be taken down into a normal .csv file*

***The enrollment.py is the file that window which gives the display of the choice of enrollment into the class... In that phase the photo is taken using OpenCV and then saves it the folder for training the data for face-identification later on***
```bash
def take_photo():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            global name1
            name1=str(name.get())
            img_name = name1+".jpg"
            cv2.imwrite(img_name, frame)
            label()
            break
            #print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()
```
***For the face-identification part during attendance I am using the python package - 'face_recognition', this will do the part of face_capture, face_encoding, face_location(), and all other parts of work that comrprises of the recognition part... then only now we have to do the identification by comparing every encoded image with the previously saved image and compare all the face_distance() and face_recognition.compare_faces()... The face_recognition.compare_faces() will compare the encodings and locations and give the result which will go to the face_distance()... now out of all possibilities.. the one will be selected if matched with least face_distance()***

**The less the face_distance() the better is the match**
```bash
// the basic operations to check for the face distance

# imgAng = fr.load_image_file('ImagesAttendance/4.jpg')
# Test = fr.load_image_file('ImagesAttendance/6.jpg')
# fLoc = fr.face_locations(imgAng)[0]
# encodeAng = fr.face_encodings(imgAng)[0]
# fLocTest = fr.face_locations(Test)[0]
# encTest = fr.face_encodings(Test)[0]
# result = fr.compare_faces([encodeAng],encTest)
# faceDist = fr.face_distance([encodeAng],encTest)
# print(result,faceDist)
```
***If matched then it will gives the command to write the result into the .csv file and also display that user's attendance has been taaken on the screen***

***I have been trying to solve the edge cases and to implement the voice-recognition and develop it into two-way-secure rogram to have accurate results...***
