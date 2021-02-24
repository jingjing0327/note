import keras.datasets.mnist as mnist
import keras


(train_image,train_lable),(test_image,test_label)= mnist.load_data();
# print(train_image.shape)
# print(type(train_image[0]))
# print(train_lable)


model=keras.Sequential()
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64,activation="relu"))
model.add(keras.layers.Dense(64,activation="relu"))
model.add(keras.layers.Dense(64,activation="relu"))

model.add(keras.layers.Dense(10,activation="softmax"))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])

model.fit(train_image,train_lable,epochs=50,batch_size=512)
