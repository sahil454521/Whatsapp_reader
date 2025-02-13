from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D

input_layer = Input(shape=(100,))
embedding_layer = Embedding(input_dim=1000,output_dim=64)(input_layer)
embedding_layer = GlobalAvergaePooling1D()(embedding_layer)
output_layer = Dense(5,activation='softmax')(pooling_layer)
# 5 intents
model = Model(inputs=input_layer,outputs=output_layer)
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# X_train: Text sequences, y_train: Intent labels
model.fit(X_train, y_train, epochs=10, batch_size=32)