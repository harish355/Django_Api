import face_recognition

# Function to compare images
def compareImage(original, test):
    original_image = face_recognition.load_image_file(original)
    original_encoding = face_recognition.face_encodings(original_image)[0]
    test_image = face_recognition.load_image_file(test)
    test_encoding = face_recognition.face_encodings(test_image)[0]
    results = face_recognition.compare_faces([original_encoding], test_encoding)
    return results[0]
