import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, Activation, GlobalMaxPooling1D
from keras.utils import plot_model

from motif_finding.generate_motif_dataset import read_dataset

x_train, y_train = read_dataset("motif_finding/motif_data_train.txt")
x_test, y_test = read_dataset("motif_finding/motif_data_test.txt")

print(len(x_train))

seq_len = 20

result = {}
accs = []
params = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in params:
    print(i)
    motif_len = i
    model = Sequential()
    model.add(Conv1D(1, motif_len, input_shape=(seq_len, 4)))
    model.add(Activation('relu'))
    model.add(GlobalMaxPooling1D())
# model.add(Dropout(0.5))
    model.add(Activation('tanh'))  # sigmoidから変更
    model.add(Dropout(1.0))

#### TODO
# dropoutの効果，dropoutとは
# 3回に1回，95%識別率が出てくる理由．

# model = Sequential()
# model.add(Dense(64, input_shape=(None, 20), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])

    history = model.fit(x_train, y_train,
                        epochs=100,
                        batch_size=100,
                        validation_data=(x_test, y_test))
    print(history.history)
    plt.plot(history.history['val_acc'], label='motiflen={0}'.format(i))

    result[i] = history

    score = model.evaluate(x_test, y_test, batch_size=100)
    print('score:',score)
    accs.append(score[1])

    ss = model.predict(x_test, 100)
    print(ss)

    # plt.plot(history.history['val_acc'], label='validation')
    # plt.plot(history.history['acc'], label='training')
    # plt.legend()
    # plt.show()


    # plot_model(model, to_file='./model.png')

plt.legend()
plt.show()

print(model.get_weights())

plt.plot(np.array(params), np.array(accs))
plt.show()

