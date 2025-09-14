import cv2
import matplotlib.pyplot as plt

# Caminho completo da imagem
caminho = r"C:\Users\Ryan\Pictures\lena\lena.png"

# Carregar imagem
imagem_colorida = cv2.imread(caminho)

# Verificar se a imagem foi carregada
if imagem_colorida is None:
    print("Erro: não foi possível carregar a imagem. Verifique o caminho e o nome do arquivo.")
    exit()

# Converter de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplicar binarização (threshold)
_, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

# Exibir os resultados
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(imagem_rgb)
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(imagem_cinza, cmap="gray")
plt.title("Imagem em Cinza")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(imagem_binaria, cmap="gray")
plt.title("Imagem Binária")
plt.axis("off")

plt.show()
