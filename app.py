import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function

from flask import Flask, request, url_for, redirect, render_template
from flask import jsonify
import numpy as np

app = Flask(__name__)


forestDB=[{
    'Temperature':'20',
    'Oxygen':'12',
    'Humidity':'30'
}]

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    ###########/model/#############
    data = pd.read_csv("C:/Users/Ayoub/Desktop/flask/Forest_fire.csv", sep = ";") # use the absolute path
    # split dataset in features and target variable
    feature_cols = ['Oxyg''en', 'Temperature', 'Humidity']
    X = data[feature_cols]  # Features
    y = data.Fire_Occurrence  # Target variable
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)  # 70% training and 30% test
    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()
    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)
    model=clf
    #################################
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    prediction = model.predict(final)
    output=prediction[0]

    if output == 1:
        return render_template('result.html', pred = 'Your Forest is in Danger')
    else:
        return render_template('result.html', pred = 'Your Forest is safe')


if __name__ == '__main__':
    app.run(debug = True)