from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

test=pd.read_csv("insomniaa test.csv",error_bad_lines=False)
x_test=test.drop('insomnia',axis=1)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        col=x_test.columns
        inputt = [str(x) for x in request.form.values()]

        b=[0]*4
        for x in range(0,4):
            for y in inputt:
                if(col[x]==y):
                    b[x]=1
        b=np.array(b)
        b=b.reshape(1,4)
        prediction = model.predict(b)
        prediction=prediction[0]
    return render_template('index.html', pred="Your insomnia level could be {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
