from flask import Flask, render_template, request, send_file, redirect, url_for
import qrcode
import os
import uuid
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = ''
        if 'text' in request.form and request.form['text']:
            data = request.form['text']
        elif 'file' in request.files and request.files['file']:
            uploaded_file = request.files['file']
            data = uploaded_file.read()

        if data:
            # Determine the QR code version dynamically, handling potential overflow
            qr = qrcode.QRCode(
                version=None,  # Start with no version specified, qrcode will determine
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            try:
                qr.make(fit=True) # Let qrcode.make() choose the version and fit the data
            except qrcode.exceptions.DataOverflowError:
                return render_template('index.html', error_message="Data too large for a QR code. Please provide less data.")
            except ValueError as e:
                return render_template('index.html', error_message=f"Error generating QR code: {e}")

            # Generate a unique file name
            unique_filename = f"{uuid.uuid4()}.png"
            qr_path = os.path.join('static', 'qr_codes', unique_filename)

            # Use BytesIO to save the image to memory and then to a file
            img_io = BytesIO()
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(img_io, 'PNG')  # Save to BytesIO object
            img_io.seek(0)  # Reset the stream position to the beginning
            
            # Save the image to a file
            with open(qr_path, 'wb') as f:
                f.write(img_io.getvalue())
            
            return redirect(url_for('show_qr', filename=unique_filename))

    return render_template('index.html')

@app.route('/show_qr')
def show_qr():
    filename = request.args.get('filename')
    return render_template('show_qr.html', filename=filename)

@app.route('/download_qr/<filename>')
def download_qr(filename):
    qr_path = os.path.join('static', 'qr_codes', filename)
    return send_file(qr_path, mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('static/qr_codes'):
        os.makedirs('static/qr_codes')  # Create the folder if it doesn't exist
    app.run(debug=True)
