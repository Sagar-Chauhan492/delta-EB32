n = input("Enter the thing which youu want to detect a (car and pedestrian) or (face) : ")

if n == "car":
    import cv2
    
    video = cv2.VideoCapture( '''here provide your file path''' )

    # Our pre trained car and pedestrian classifiers

    car_tracker_file = 'cars.xml'
    pedestrian_tracker_file = 'pedestrian_full.xml'

    car_tracker = cv2.CascadeClassifier(car_tracker_file)
    pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)


    # Run forever until car stops or something
    while True:
        # Read the current frame
        (read_successful, frame) = video.read()

    
        if read_successful:
            grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            break
        # detect cars
        cars = car_tracker.detectMultiScale(grayscaled_frame)
        pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

        # Draw rectangles around the cars
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Draw rectangles around the pedestrians
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        
        #Showing the frame
        cv2.imshow(' Our Project ',frame)
        key = cv2.waitKey(1)

        #Stop if Q key is pressed
        if key==81 or key==113:
            break


if n == "face":    
    import cv2
    from random import randrange

    # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    #To capture video from webcam
    webcam = cv2.VideoCapture(0)

    # Iterate forever over frames 
    while True:
        # Read the current frame
        successful_frame_read, frame = webcam.read()

        # If there is an error , abort
        if not successful_frame_read:
            break

        # Must convert to greyscale
        greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

        
        # Draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255, 255), 4)
        
        #Showing the frame
        cv2.imshow('image',frame)
        key = cv2.waitKey(1)

        #Stop if Q key is pressed
        if key==81 or key==113:
            break

