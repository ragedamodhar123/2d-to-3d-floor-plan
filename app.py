from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        # Read the image
        data = file.read()
        if not data:
            return "File is empty or not correctly uploaded"
        else:
            img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Perform image processing (example: edge detection)
       # Perform image processing (example: edge detection)
        edges = cv2.Canny(img, 50, 150)

# Save processed image (for demonstration purposes)
# You can use `edges` or `img` here depending on your needs
        filename = 'static/processed_image.jpg'
        cv2.imwrite(filename, edges)
        print(f"Image saved as {filename}")

        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
