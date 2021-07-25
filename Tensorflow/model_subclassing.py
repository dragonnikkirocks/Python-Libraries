import tensorflow as tf
import os
import tensorflow.keras.layers as layers
import tensorflow.keras as keras
import tensorflow.keras.datasets.mnist as mnist
from tensorflow.python.keras.datasets.mnist import load_data
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.ops.gen_nn_ops import lrn

(X_train,Y_train), (X_test,Y_test)= mnist.load_data()
X_test = X_test.astype("float32")/255.0
X_train =X_train.astype("float32") / 255.0


#create a class for a block
class CNNBlock(layers.Layer):
    def __init__(self, out_channels, kernel_size=3):
        super(CNNBlock,self).__init__()
        self.conv= layers.Conv2D(out_channels= out_channels,kernel_size=kernel_size,padding='same')
        self.bn = layers.BatchNormalization()
    
    def call(self, input_tensor,training =False): #same as forward method in pytorch
        x = self.conv(input_tensor)
        x= self.bn(x,training=training)
        x= tf.nn.relu(x)
        return x

model = keras.Sequential(

    [
      CNNBlock(32),
      CNNBlock(128),
      CNNBlock(256),
      layers.Flatten(),
      layers.Dense(10),

    ]
)

class ResBlock(layers.layer):
    def __init__(self, channels):
        super(CNNBlock,self).__init__()






model.compile(
    optimizer=keras.optimizers.Adam(),
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)


model.fit(X_train,Y_train,epochs=10,batch_size=64, verbose=2)
model.evaluate(X_test,Y_test,batch_size=64, verbose=2)