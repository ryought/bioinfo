import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, Activation, GlobalMaxPooling1D

from motif_finding.generate_motif_dataset import read_dataset

x_train, y_train = read_dataset("motif_finding/motif_data_train.txt")
x_test, y_test = read_dataset("motif_finding/motif_data_test.txt")

print(len(x_train))

motif_len = 5
seq_len = 20

model = Sequential()
model.add(Conv1D(1, motif_len, input_shape=(seq_len, 4)))
# model.add(Dropout(0.5))
model.add(Activation('relu'))
model.add(GlobalMaxPooling1D())
model.add(Activation('tanh'))
# model.add(Activation('sigmoid'))

# model = Sequential()
# model.add(Dense(64, input_shape=(None, 20), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=100,
          batch_size=100)

score = model.evaluate(x_test, y_test, batch_size=100)
print('score:',score)

ss = model.predict(x_test, 100)
print(ss)
