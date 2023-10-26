
from flask import Flask, request, jsonify, render_template
from transformers import BertTokenizer, BertForSequenceClassification
import torch.nn.functional as F
import torch

app = Flask(__name__)

# Load model and tokenizer
MODEL_PATH = '2.11 Bert model2'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length', max_length=256)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = F.softmax(logits, dim=1)
    label = torch.argmax(probs, dim=1).item()
    return jsonify({
        'label': 'Hateful' if label == 1 else 'Not hateful',
        'probabilities': {
            'hateful': probs[0][1].item(),
            'not_hateful': probs[0][0].item()
        }
    })

if __name__ == '__main__':
    app.run(debug=True)

