from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result ,proba= load_image(file_path)
        result = result.title()

        d = {'Biber Dolmasi': " 🌍 ",'Borek':" 💣 " ,'Enginar': " ✅ ",\
             'Icli Kofte': " 📚 ",'Kisir': " 💡 ",'Manti': " 🔗 ", \
             'Hamsi':"💥 ","Ispanak":" 💊 ","Kuru Fasulye":" 🐞 ","Simit":" 💫 ",\
             "Cig Kofte":" 📧 ","Hunkar Bengendi":" ♻️ ","Kebap":" ☀️i ","Lokum":" ⚠ ",\
             "Yaprak Sarma":" 📌 "}
        result = result+d[result]
        
        print(result+ "With probability: "+str(proba))
        result +="  Accuracy: "
        result += str( round(proba*100,2))+" %"

        os.remove(file_path)
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)
