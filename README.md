# Olá, bem vindo ao meu projeto de uma IA que reconhece dígitos manuscritos

![image](https://github.com/user-attachments/assets/40d2110f-e9e9-4efe-8420-1147025d0cec)

## :hammer: Ferramentas utilizadas:

* Phyton
  
* Google Colab
  
* MNIST Dataset

## ❗Descrição do projeto:

O projeto desenvolvido é de uma Inteligência Artificial que utiliza de uma Rede Neural Convolucional (CNN) para o reconhecimento de dígitos manuscritos. 

Foi utilizado um Dataset com mais de 60000 imagens de dígitos manuscritos, conhecido como MNIST, além de bibliotecas poderosas dedicadas ao treinamento de redes neurais,como por exemplo a TenserFlow. 

## ✔️ Funcionalidades:

- `1)`: Utilizar um banco de dados para realizar o treinamento de uma IA
- `2)`: Realizar o reconhecimento de imagens
- `3)`: Gerar como resultado que a IA retorne o número da imagem correspondente

## 🍷🗿 Explicação do código:

### Realizando o treinamento da CNN com 3 convoluções e seus respectivos pooling e variados filtros:

<img src="https://github.com/user-attachments/assets/0c73fcb3-41f1-47b9-8359-d97a0a4fff29" alt="Foto do codigo" width="950" height="350">

### Executando esse treinamento em 10 epochs (vai mostrar a precisão e os erros):
O certo é que durante esse treinamento os erros diminuam e a precisão aumente !

<img src="https://github.com/user-attachments/assets/6f4c72ae-8766-4660-8efd-e36ea68e9ba8" alt="Foto execusão treinamento" width="950" height="400" >

### Na etapa abaixo você consulta o valor que mais corresponde a imagem:
As imagens ficam armazenadas em um vetor gigantesco, portanto no exemplocitado o vetor 0 armazenava o valor 7, que a IA identificou corretamente.Lá em baixo vou dar a explicação do "dadosmnist.py",para que você possa ver os valores em cada vetor!

<img src="https://github.com/user-attachments/assets/93e3c4fa-0c8d-4644-9c90-4469beac2c81" alt="Foto valor vetor" width="600" height="150" > 

### Para verificar no dadosmnist.py qual valor tem nos dados de teste e treinamento:
Caso queira ver mais que 10 vetores,é só alterar os valores onde tem 10 !

<img src="https://github.com/user-attachments/assets/7bebedcf-39e1-49cb-886b-062afc0e6e5d" alt="Foto valor vetor" width="700" height="250" >
  
## 🔗 Você pode acessar meu projeto utilizando o Google Colab, siga os passos abaixo:
- `1)` Acesse o [Google Colab](https://colab.research.google.com/)
- `2)` Vá em "Arquivo" e crie um "Novo Notebook" 
- `3)` Cole o código lá e execute
- `4)` Para executar o "dadosmnist.py" é só criar uma nova seção no próprio notebook ou crie um novo notebook

## 🔧 Feito por:

João Monferrari
