import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from tkinter import Tk, filedialog

# Função para converter a imagem para escala de cinza pixel por pixel
def convert_to_gray_pixel_by_pixel(image, luma=False):
  if luma:
      params = [0.299, 0.587, 0.114]
  else:
      params = [0.2125, 0.7154, 0.0721]
  
  # Inicializar a matriz da imagem em escala de cinza
  gray_image = np.zeros((image.shape[0], image.shape[1]))
  
  # Iterar sobre cada pixel
  for i in range(image.shape[0]):
      for j in range(image.shape[1]):
          gray_image[i, j] = np.dot(image[i, j, :3], params)
  
  # Saturando os valores em 255
  gray_image[gray_image > 255] = 255
  
  return gray_image

# Função para abrir o diálogo de seleção de arquivo
def upload_image():
  root = Tk()
  root.withdraw()  # Esconde a janela principal do Tkinter
  file_path = filedialog.askopenfilename()
  root.destroy()
  return file_path

# Carregar a imagem selecionada pelo usuário
file_path = upload_image()
if file_path:
  image = io.imread(file_path)
  
  # Converter a imagem para escala de cinza pixel por pixel
  gray_image = convert_to_gray_pixel_by_pixel(image, luma=True)
  
  # Criar uma interface simples para visualizar as imagens
  fig, axes = plt.subplots(1, 2, figsize=(12, 6))
  ax = axes.ravel()
  
  ax[0].imshow(image)
  ax[0].set_title("Imagem Original")
  ax[0].axis('off')
  
  ax[1].imshow(gray_image, cmap='gray')
  ax[1].set_title("Imagem em Escala de Cinza")
  ax[1].axis('off')
  
  plt.tight_layout()
  plt.show()
else:
  print("Nenhuma imagem foi selecionada.")