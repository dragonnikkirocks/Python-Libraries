import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, TensorBoard
from imutils import paths
import tensorflow_addons as tfa
from functools import partial
import os
import matplotlib.pyplot as plt
from IPython.display import clear_output
from tensorflow.keras.callbacks import History 


def decode_image(image):
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.cast(image, tf.float32)
    image =tf.image.resize(image,[224,224])
    #image = tf.image.per_image_standardization(image)
    #image = tf.keras.applications.resnet50.preprocess_input(image)
    return image

def read_tfrecord(example, progress_labelled):
    tfrecord_format = (
       {
        'image/image_uri': tf.io.FixedLenFeature((), tf.string, ''),
          'image/encoded': tf.io.FixedLenFeature((), tf.string, ''),
          'image/format': tf.io.FixedLenFeature((), tf.string, 'jpeg'),
          'image/id': tf.io.FixedLenFeature([], tf.int64),
          'image/label': tf.io.FixedLenFeature([], tf.int64, -1),
          'image/progress':tf.io.FixedLenFeature([], tf.float32, -1)

    }
        
    )
    example = tf.io.parse_single_example(example, tfrecord_format)
    image = decode_image(example["image/encoded"])
    if progress_labelled:
        progress_label  = tf.cast(example["image/progress"], tf.float32)
        return image, progress_label
    return image

def load_dataset(filenames,progress_labelled=True):
    ignore_order = tf.data.Options()
    ignore_order.experimental_deterministic = False  # disable order, increase speed
    dataset = tf.data.TFRecordDataset(filenames)  
    dataset = dataset.with_options(ignore_order)
    dataset = dataset.map(partial(read_tfrecord,progress_labelled=progress_labelled), num_parallel_calls=AUTOTUNE )
    # returns a dataset of (image, label) pairs if labeled=True or just images if labeled=False
    #returns a dataset of (image,progress_label) if progress_labelled=True
    return dataset

def show_batch(image_batch, progress_label_batch):
    plt.figure(figsize=(10, 10))
    for n in range(25):
        ax = plt.subplot(5, 5, n + 1)
        plt.imshow(image_batch[n])
        plt.title([progress_label_batch[n]])
        plt.axis("off")



        