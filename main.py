from flask import Flask, render_template
import base64

app = Flask(__name__)

@app.route("/")
def index():
    with open('Andi_Brim.png', 'rb') as my_file:
      file_bytes = my_file.read()

    base_64 = base64.b64encode(file_bytes)

    img = base_64.decode("utf-8") 

    return render_template('index.html', img = img)
    
    #return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)