
# Flask QR Code Generator

This is a simple Flask-based web application that generates QR codes dynamically based on either text input or file upload. The application uses the `qrcode` Python library to generate the QR codes and includes basic error handling for data overflow situations.

## Features:
- **Text Input**: Users can input text to generate a QR code.
- **File Upload**: Users can upload a file, and the QR code for the file's content will be generated.
- **Dynamic Version Handling**: The application automatically adjusts the QR code's version to accommodate the data size.
- **Error Handling**: If the data is too large for a QR code, an error message is shown.

## Requirements:
To run this project, ensure that you have the following Python packages installed:
- Flask
- qrcode
- uuid

You can install them using pip:

```bash
pip install Flask qrcode
```

## Project Structure:
```
.
├── app.py               # Main Flask application
├── static/
│   └── qr_codes/        # Folder where generated QR code images are stored
├── templates/
│   ├── index.html       # Main page for text input and file upload
│   └── show_qr.html     # Page to display generated QR code
└── README.md            # Project documentation (this file)
```

## How to Run:
1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your web browser and visit `http://127.0.0.1:5000` to start generating QR codes.


## Acknowledgements:
- [Flask](https://flask.palletsprojects.com/) for web framework.
- [qrcode](https://pypi.org/project/qrcode/) for generating QR codes.
