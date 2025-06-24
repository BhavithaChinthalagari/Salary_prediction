from flask import Flask, render_template, request
import numpy as np
import joblib
import os

file_path = os.path.abspath('C:\Users\Bhavitha\OneDrive\Desktop\Salary prediction\salary_prediction.pkl')

model = joblib.load(file_path)


#model = joblib.load('model = joblib.load('C:\\Users\\Bhavitha\\OneDrive\\Desktop\\Salary prediction\\salary_prediction.pkl')

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('your_html_file.html')

@app.route('/predict_salary', methods=['POST'])
def predict_salary():
    try:
        age = int(request.form['age'])
        gender = request.form['gender']
        degree = int(request.form['degree'])
        specialization = int(request.form['specialization'])
        experience = int(request.form['experience'])
        logical = int(request.form['logical'])
        english = int(request.form['english'])
        programming = int(request.form['programming'])
        electrical = int(request.form['electrical'])
        job_title = int(request.form['job_title'])

        input_data = np.array([[age, gender, degree, specialization, experience, logical, english, programming, electrical, job_title]])
        predicted_salary = model.predict(input_data)[0]

        return render_template('result.html', predicted_salary=predicted_salary)

    except Exception as e:
        return "Error occurred: " + str(e), 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
