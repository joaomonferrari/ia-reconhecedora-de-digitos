#Treinamento e execução realizados no ambiente do Google Colab

#Importação das bibliotecas:

import tensorflow as tf  #Framework para construção de redes neurais
from tensorflow.keras import layers,models #API para modelos de Deep Learning
from tensorflow import keras
import numpy as np #Operações numéricas

#Carregar os dados do MNIST:
(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()

#Normalizar os dados (valores dos pixels de 0 a 255):
X_train = X_train / 255
X_test = X_test / 255

#Acessa a primeira imagem (mais para verificação dos dados)
X_train[0]

#Forma do conjunto de treinamento (60000 imagens de dimensão 28 x 28):
X_train.shape

#Redimensionamento dos canais (treinamento):
X_train = X_train.reshape(-1,28,28,1)
X_train.shape

#Redimensionamento dos canais (teste):
X_test = X_test.reshape(-1,28,28,1)
X_test.shape

convolutional_neural_network = models.Sequential([
    layers.Conv2D(filters=25, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)),#Camada convolucional
    layers.MaxPooling2D((2, 2)), #Reduzir a dimensionalidade

    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

#optimizer='adam' - peso ; loss='sparse_categorical_crossentropy' - perda ; metrics=['accuracy'] - avaliar desempenho)
convolutional_neural_network.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
convolutional_neural_network.fit(X_train, y_train, epochs=10)#Treina o modelo por 10 épocas

#Avalia o desempenho do modelo (perda e precisão)
convolutional_neural_network.evaluate(X_test, y_test)

#Previsões dos dados de teste (probabilidade de cada classe):
y_predicted_by_model = convolutional_neural_network.predict(X_test)
y_predicted_by_model[0]   #getting probability score for each class digits

#Retorna o índice da classe com maior probabilidade pra primeira imagem no caso:
np.argmax(y_predicted_by_model[0])

#Converte as probabilidades em rótulos:
y_predicted_labels = [np.argmax(i) for i in y_predicted_by_model]

#Mostra os 6 (no caso) rótulos previstos:
y_predicted_labels[:6]

#Mostra a imagem correspondente ao vetor 0 (no caso):
import matplotlib.pyplot as plt

# Visualizar a primeira imagem do conjunto de teste
plt.imshow(X_test[0], cmap='gray')
plt.axis('off')  # Desativar os eixos
plt.show()

