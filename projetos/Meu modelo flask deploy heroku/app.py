from flask import Flask, request, render_template
import os,dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

t = 'Modelo deploy flask heroku'

app = Flask(__name__)
app.debug = True

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',titulo=t)

app.run()