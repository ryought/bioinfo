import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, Activation, GlobalMaxPooling1D

from motif_finding.generate_motif_dataset import read_dataset

x_train, y_train = read_dataset("motif_finding/motif_data_train.txt")
x_test, y_test = read_dataset("motif_finding/motif_data_test.txt")

print(len(x_train))
print(x_train[0].shape)
