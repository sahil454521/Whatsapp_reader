import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model

input_layer = Input(shape=(None,20))
lastm_layer = LSTM(128)(input_layer)
output_layer = Dense(10,activation='softmax')(lastm_layer)
# 10 classes for the intents

model = Model(inputs=input_layer,outputs=output_layer)
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

model.fit(x_train,y_train,epochs=10,batch_size=32)