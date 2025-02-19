import tensorflow as tf 
model.save("nmt_model.h5") 
from flask import Flask, request, jsonify import tensorflow as tf 
 

import numpy as np 
app = Flask(__name__) 
# Load the trained model 
model = tf.keras.models.load_model("nmt_model.h5") 
@app.route('/translate', methods=['POST']) 
def translate(): 
data = request.get_json() 
input_text = data['text'] 
translated_text = model.predict(input_text)  # Placeholder for actual translation logic 
return jsonify({'translated_text': translated_text.tolist()}) 
if __name__ == '__main__': 
app.run(debug=True) 
