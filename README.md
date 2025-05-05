# 🚖 NYC Taxi Tip Predictor App

This Streamlit app predicts whether a taxi rider is likely to leave a **generous tip** based on features like trip distance, time of day, and more. It's built using a machine learning model trained on a simplified version of the **2017 TLC Taxi dataset**.

## 🎯 Project Goal

To help taxi drivers identify potentially generous tippers before or during the ride using a lightweight prediction tool based on patterns in historical data.

## 🧠 Model Information

- **Model Type**: Random Forest Classifier  
- **Training Set**: 2017 TLC Yellow Taxi Data (subset)  
- **Target Variable**: `generous` (1 = above-average tip, 0 = otherwise)  
- **Selected Features**:
  - `passenger_count`
  - `avg_distance` (average distance between pickup & dropoff)
  - Time of day: `am_rush`, `daytime`, `pm_rush`, `nighttime`
  - Day of week: `day_monday`, `day_tuesday`, etc.
  - Month: `month_jan`, `month_feb`, etc.

## 🛠 Features

- Interactive form to input trip details
- Predicts whether the customer is likely to leave a generous tip
- Designed to be fast, minimal, and easy to use

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/gitalcak/tip-predictor-app.git
   cd tip-predictor-app

## Install required packages
pip install -r requirements.txt

## Run the app
streamlit run app.py

Notes
The dataset was filtered to include only credit card payments for consistency.

This project is for educational and demonstration purposes only. It does not make real-time predictions and is not intended for deployment in commercial settings.

Ethical considerations were acknowledged but simplified for the scope of this prototype.

This dataset is also introduced in Google's Advanced Data Analytics Certificate Program.

📂 File Structure
tip-predictor-app/
│
├── app.py                      # Main Streamlit app
├── nextgentipper_model.pkl     # Trained Random Forest model
├── requirements.txt            # Dependencies
├── README.md                   # Project overview
└── data/                       # Folder for original dataset 

Created by Alper Kokcu

---

Let me know if you'd like me to update the GitHub or Streamlit links once you have them!
