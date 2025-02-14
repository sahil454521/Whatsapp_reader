from tensorflow.keras.layers import Bidirectional, LSTM

input_layer = Input(shape=(100,))
embedding_layer = Embedding(input_dim=1000,output_dim=64)(input_layer)
lstm_layer = Bidirectional(LSTM(64))(embedding_layer)
output_layer = Dense(1,activation='sigmoid')(lstm_layer)

model=Model(input=input_layer,output=output_layer)
model.compile(optimizer='adam,loss='binary_crossentropy',metrics=['accuracy'])
              
model.fit(X_train,y_train,epochs=10,batch_size=64)