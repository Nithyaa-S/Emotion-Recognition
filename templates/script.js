document.getElementById('fetchImage').addEventListener('click', function() {
    const photo = document.getElementById('photo');
    const imageURL = 'http://127.0.0.1:5501/emotion-recognition-python-scikit-learn-mediapipe-main/uploads/captured_image.png'; // Replace with your actual image URL

    photo.src = imageURL;
});