import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("/home/hruday/PycharmProjects/TNC_representation_learning/"
                 "TNC_representation_learning/data/mendeley_data/mendeley.csv")

train_x = df[['Voltage', 'Current']]
train_y = df['Ah']

n_train = int(len(df) * 0.8)
repeat = 10

test_x = np.stack([np.asarray(train_x[n_train:])] * repeat).reshape((repeat, 2, -1))
test_y = np.stack([np.asarray(train_y[n_train:])] * repeat)

train_x = np.stack([np.asarray(train_x[:n_train])] * repeat).reshape((repeat, 2, -1))
train_y = np.stack([np.asarray(train_y[:n_train])] * repeat)


with open('/home/hruday/PycharmProjects/TNC_representation_learning/TNC_representation_learning/data/mendeley_data/x_train.pkl', 'wb') as f:
    pickle.dump(train_x, f)
with open('/home/hruday/PycharmProjects/TNC_representation_learning/TNC_representation_learning/data/mendeley_data/x_test.pkl', 'wb') as f:
    pickle.dump(test_x, f)
with open('/home/hruday/PycharmProjects/TNC_representation_learning/TNC_representation_learning/data/mendeley_data/state_train.pkl', 'wb') as f:
    pickle.dump(train_y, f)
with open('/home/hruday/PycharmProjects/TNC_representation_learning/TNC_representation_learning/data/mendeley_data/state_test.pkl', 'wb') as f:
    pickle.dump(test_y, f)