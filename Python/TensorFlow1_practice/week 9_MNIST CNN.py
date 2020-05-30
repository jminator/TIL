import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

img_rows = 28
img_cols = 28

input_shape = (img_rows, img_cols, 1)
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

print('x_train shape: ', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

batch_size = 128
num_classes = 10
epochs = 1

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, kernel_size=(5,5), strides(1,1), padding='same', activation='relu',input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
hist=model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_Data=(X_test, y_test))
