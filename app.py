from flask import Flask, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

with open("q-vercel-python.json",'r') as f:
      sdata=json.load(f)

sdict={s["name"]: s["marks"]  for s in sdata}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [sdict.get(n, "Not Found") for n in names]
    return {"marks": marks}





if __name__ == '__main__':
    app.run(debug=True)