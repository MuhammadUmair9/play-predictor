---


# 🎮 Play Predictor

A simple Flask web application that uses a machine learning model to predict whether to **Play** or **Not Play** based on weather conditions like **Day** and **Temperature**.

## 🚀 Features

- Built using **Flask** for the web interface
- Uses **Random Forest Classifier** from Scikit-Learn
- Encodes categorical features using **OneHotEncoder** and **LabelEncoder**
- Takes user input and predicts live using a trained model
- HTML frontend with dropdowns for quick predictions

## 📊 Dataset

The dataset (`data.csv`) contains the following columns:

- `Day`: Sunny or Windy
- `Temperature`: Hot or Cool
- `Class`: Play or Not Play

Example:

```
Day,Temperature,Class
Sunny,Cool,Play
Windy,Cool,Not Play
...
```

## 🧠 Model

- Model: `RandomForestClassifier`
- Encoders: `OneHotEncoder` for features, `LabelEncoder` for labels
- Training split: 70% training / 30% testing

## 🖥️ How to Run

1. **Clone the repo**
```bash
git clone https://github.com/your-username/play-predictor.git
cd play-predictor
```

2. **Install dependencies**
```bash
pip install flask pandas scikit-learn joblib
```

3. **Run the app**
```bash
python app.py
```

4. **Open in browser**
```
http://127.0.0.1:5000/
```

## 📁 File Structure

```
play-predictor/
│
├── app.py                # Main Flask application
├── data.csv              # Dataset used for training
├── index1.html           # HTML template
├── model.pkl             # Saved Random Forest model
├── onehot.pkl            # Saved OneHotEncoder
├── label.pkl             # Saved LabelEncoder
├── README.md             # This file
```

## 🧪 Example Prediction

1. Select:
   - **Day**: Sunny
   - **Temperature**: Cool
2. Click **Predict**
3. Output:
   ```
   Prediction: Play
   ```

## 📜 License

MIT License

---

Made with ❤️ using Flask + Scikit-Learn
```

---
