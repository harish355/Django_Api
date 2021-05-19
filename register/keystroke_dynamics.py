# Functions to process keystroke dynamics
import pandas as pd
import joblib

# Load the models
classifier_model = joblib.load('./model/net.joblib')
train_mode = joblib.load('./model/train_mode.joblib')

# Features for the model
features=['H.period', 'DD.period.t', 'UD.period.t', 'H.t', 'DD.t.i', 'UD.t.i', 'H.i', 'DD.i.e', 'UD.i.e', 'H.e', 'DD.e.five', 'UD.e.five',
 'H.five', 'DD.five.Shift.r', 'UD.five.Shift.r', 'H.Shift.r', 'DD.Shift.r.o', 'UD.Shift.r.o', 'H.o', 'DD.o.a', 'UD.o.a', 'H.a', 'DD.a.n', 'UD.a.n',
 'H.n', 'DD.n.l', 'UD.n.l', 'H.l', 'DD.l.Return', 'UD.l.Return', 'H.Return']

# Helper functions for parsing 
def string_parser(s):
    nums = [float(n) for n in s.split(',')]
    return nums

def dd_time(s):
    d=string_parser(s)
    s1 = list((d[i + 1] - d[i]) / 1000 for i in range(len(d) - 1))
    return s1

def hold_period(hold):
    d = string_parser(hold)
    return d

def release_time(keyup):
    d = string_parser(keyup)
    return d

def press_time(keyup, hold):
    d=list(set(release_time(keyup))-set(hold_period(hold)))
    return d

def input_array(keyup,hold):
    s=[]
    h=hold_period(hold)
    p=release_time(keyup)
    r=release_time(keyup)
    for i in range(len(release_time(keyup))-1):
        s.extend([h[i],p[i+1]-p[i],p[i+1]-r[i]])
    s.append(h[len(h)-1])
    return s

def input_array(keyup, hold):
    s=[]
    h=hold_period(hold)
    p=release_time(keyup)
    r=release_time(keyup)
    for i in range(len(release_time(keyup))-1):
        s.extend([h[i],p[i+1]-p[i],p[i+1]-r[i]])
    s.append(h[len(h)-1])
    return s

# Convert the input to dictionary of features
def input_dict(keyup, hold):
    if len(input_array(keyup,hold))>=len(features):
        result = {features[i]: input_array(keyup,hold)[i] for i in range(len(features))}
        return result
    else:
        result1 = {features[i]: input_array(keyup, hold)[i] for i in range(len(input_array(keyup,hold)))}
        result2 = {features[i]: train_mode[features[i]] for i in range(len(input_array(keyup,hold)),len(features))}
        result = {**result1, **result2}
        return result

# Preprocessing the test data and saving it to a csv file
def preprocessing(test1):
    test1 = pd.DataFrame(test1, index=[0])
    test2 = pd.DataFrame(test1,columns=['H.period', 'DD.period.t', 'UD.period.t', 'H.t', 'DD.t.i', 'UD.t.i', 'H.i', 'DD.i.e', 'UD.i.e', 'H.e', 'DD.e.five', 'UD.e.five',
            'H.five', 'DD.five.Shift.r', 'UD.five.Shift.r', 'H.Shift.r', 'DD.Shift.r.o', 'UD.Shift.r.o', 'H.o', 'DD.o.a', 'UD.o.a', 'H.a', 'DD.a.n', 'UD.a.n',
            'H.n', 'DD.n.l', 'UD.n.l', 'H.l', 'DD.l.Return', 'UD.l.Return', 'H.Return'])
    test2.to_csv('./model/data.csv',mode='a+',header=False,index=False)
    return test1

# Predict based on the model
def predict(up_time, press_time_array):
    test_data = preprocessing(input_dict(up_time, press_time_array))
    login_prediction = classifier_model.predict(test_data)[0]
    return login_prediction