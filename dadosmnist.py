#Treinamento e execução realizados no ambiente do Google Colab

import numpy as np
import matplotlib.pyplot as plt

# Carregar o arquivo .npz
arquivo = np.load('mnist.npz')

# Listar os arrays contidos no arquivo
print("Arrays contidos no arquivo:")
print(arquivo.files)

# Função para exibir um conjunto de imagens
def exibir_imagens(imagens, quantidade=10):
    plt.figure(figsize=(10, 10))
    for i in range(quantidade):
        plt.subplot(1, quantidade, i + 1)
        plt.imshow(imagens[i], cmap='gray')
        plt.axis('off')
    plt.show()

# Exibir as primeiras 10 imagens de cada conjunto
for chave in arquivo.files:
    if 'x' in chave:  # assumindo que 'x' contém as imagens
        print(f"Exibindo imagens do array '{chave}':")
        exibir_imagens(arquivo[chave], quantidade=10)
