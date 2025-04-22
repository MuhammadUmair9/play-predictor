from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import joblib

app = Flask(__name__)

df = pd.read_csv('data.csv')
X_raw = df[['Day', 'Temprature']]
Y_raw = df['Class']

onehot_encoder = OneHotEncoder()
X_encoded = onehot_encoder.fit_transform(X_raw).toarray()

label_encoder = LabelEncoder()
Y_encoded = label_encoder.fit_transform(Y_raw)

X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y_encoded, test_size=0.3)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

joblib.dump(model, 'model.pkl')
joblib.dump(onehot_encoder, 'onehot.pkl')
joblib.dump(label_encoder, 'label.pkl')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        day = request.form['day']
        temperature = request.form['temperature']
        
        model = joblib.load('model.pkl')
        onehot = joblib.load('onehot.pkl')
        label = joblib.load('label.pkl')
        
        new_data = pd.DataFrame([[day, temperature]], columns=['Day', 'Temprature'])
        new_encoded = onehot.transform(new_data).toarray()
        
        prediction = model.predict(new_encoded)
        result = label.inverse_transform(prediction)[0]
        
        return render_template('index1.html', prediction_text=f'Prediction: {result}')
if __name__ == '__main__':
 app.run(debug=True)