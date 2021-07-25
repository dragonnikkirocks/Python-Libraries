import tensorflow as tf
import os
import tensorflow.keras.layers as layers
import tensorflow.keras as keras
import tensorflow.keras.datasets.mnist as mnist
from tensorflow.python.keras.datasets.mnist import load_data
from tensorflow.python.ops.gen_nn_ops import lrn

(X_train,Y_train), (X_test,Y_test)= mnist.load_data()
X_test = X_test.astype("float32")/255.0
X_train =X_train.astype("float32") / 255.0

model = keras.Sequential()
model.add(keras.Input(shape=(None,28)))
model.add(
    layers.SimpleRNN(512,activation='relu',return_sequences=True)
)
model.add(
    layers.SimpleRNN(512,activation='relu')
)
model.add(layers.Dense(10))

print(model.summary())

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    metrics=["accuracy"]
)

model.fit(X_train,Y_train,epochs=10,batch_size=64, verbose=2)
model.evaluate(X_test,Y_test,batch_size=64, verbose=2)
