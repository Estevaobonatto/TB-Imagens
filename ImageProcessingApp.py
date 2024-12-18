import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import math
import matplotlib.pyplot as plt

class ImageProcessingApp(tk.Tk):
  def __init__(self):
      super().__init__()
      self.title('Trabalho de Processamento de Imagens - Semestre 2024-2')
      self.geometry('1820x920')
      self.configure(bg='#000000')

      style = ttk.Style(self)
      style.theme_use('clam')
      style.configure('TButton', background='#3a3a3a', foreground='white', borderwidth=1, focusthickness=3, focuscolor='none')
      style.map('TButton', background=[('active', '#4a4a4a')])
      style.configure('TLabel', background='#2b2b2b', foreground='white')
      style.configure('TFrame', background='#2b2b2b')
      style.configure('TLabelFrame', background='#2b2b2b', foreground='white', borderwidth=1)

      self.image_a = None
      self.image_b = None
      self.result_image = None
      self.result_image_pil = None  # Store the PIL image for saving
      self.create_widgets()

  def create_widgets(self):
      main_frame = ttk.Frame(self, padding=5)
      main_frame.pack(fill='both', expand=True)

      left_frame = ttk.Frame(main_frame, padding=5)
      left_frame.pack(side='left', fill='y')

      self.image_a_label = ttk.Label(left_frame, text='Imagem A')
      self.image_a_label.pack(pady=5)

      self.image_a_display = ttk.Label(left_frame)
      self.image_a_display.pack(pady=5)

      ttk.Button(left_frame, text='Carregar imagem A...', command=self.load_image_a).pack(pady=5)
      ttk.Button(left_frame, text='Escala de Cinza', command=self.convert_to_grayscale).pack(pady=5)
      ttk.Button(left_frame, text='Calcular Histograma', command=self.calculate_and_equalize_histogram).pack(pady=5)

      operations_frame = ttk.Frame(main_frame, padding=5)
      operations_frame.pack(side='left', fill='both', expand=True)

      self.create_arithmetic_operations_group(operations_frame)
      self.create_logical_operations_group(operations_frame)
      self.create_image_enhancement_group(operations_frame)
      self.create_edge_detection_group(operations_frame)
      self.create_gaussian_filter_group(operations_frame)
      self.create_morphological_operations_group(operations_frame)

      right_frame = ttk.Frame(main_frame, padding=5)
      right_frame.pack(side='left', fill='y')

      self.image_b_label = ttk.Label(right_frame, text='Imagem B')
      self.image_b_label.pack(pady=5)

      self.image_b_display = ttk.Label(right_frame)
      self.image_b_display.pack(pady=5)

      ttk.Button(right_frame, text='Carregar imagem B...', command=self.load_image_b).pack(pady=5)

      self.result_image_label = ttk.Label(right_frame, text='Imagem Resultante')
      self.result_image_label.pack(pady=5)

      ttk.Button(right_frame, text='Salvar Imagem...', command=self.save_result_image).pack(pady=5)

  def create_arithmetic_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Aritméticas", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Button(group, text='Adição', command=self.add_images_with_value).pack(side='left', padx=2)
      ttk.Button(group, text='Subtração', command=self.subtract_images_with_value).pack(side='left', padx=2)
      ttk.Button(group, text='Multiplicação', command=self.multiply_images).pack(side='left', padx=2)
      ttk.Button(group, text='Divisão', command=self.divide_images).pack(side='left', padx=2)
      ttk.Button(group, text='Blending', command=self.blend_images).pack(side='left', padx=2)

  def create_logical_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Lógicas", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Button(group, text='LIMIAR', command=self.limiar_images).pack(side='left', padx=2)
      ttk.Button(group, text='AND', command=self.and_images).pack(side='left', padx=2)
      ttk.Button(group, text='OR', command=self.or_images).pack(side='left', padx=2)
      ttk.Button(group, text='XOR', command=self.xor_images).pack(side='left', padx=2)
      ttk.Button(group, text='NOT', command=self.not_image_a).pack(side='left', padx=2)

  def create_image_enhancement_group(self, parent):
      group = ttk.LabelFrame(parent, text="Realce de Imagens", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Button(group, text='MÉDIA', command=self.apply_media).pack(side='left', padx=2)
      ttk.Button(group, text='MEDIANA', command=self.apply_mediana).pack(side='left', padx=2)
      ttk.Button(group, text='MINIMO', command=self.apply_mediana).pack(side='left', padx=2)
      ttk.Button(group, text='MÁXIMO', command=self.apply_mediana).pack(side='left', padx=2)

  def create_edge_detection_group(self, parent):
      group = ttk.LabelFrame(parent, text="Detecção de Bordas", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Button(group, text='Prewitt', command=self.apply_prewitt).pack(side='left', padx=2)
      ttk.Button(group, text='Sobel', command=self.apply_sobel).pack(side='left', padx=2)
      ttk.Button(group, text='Laplaciano', command=self.apply_laplacian).pack(side='left', padx=2)

  def create_gaussian_filter_group(self, parent):
      group = ttk.LabelFrame(parent, text="Filtragem Gaussiana", padding=5)
      group.pack(pady=5, fill='x')
      
      ttk.Label(group, text="Desvio Padrão (Sigma):").pack(side='left', padx=2)
      self.gaussian_sigma = tk.Scale(group, from_=0.1, to=3.0, resolution=0.1, orient='horizontal', length=100)
      self.gaussian_sigma.pack(side='left', padx=2)
      self.gaussian_sigma.set(1.0)
      
      ttk.Label(group, text="Intensidade:").pack(side='left', padx=2)
      self.gaussian_intensity = tk.Scale(group, from_=0, to=100, orient='horizontal', length=100)
      self.gaussian_intensity.pack(side='left', padx=2)
      self.gaussian_intensity.set(50)
      
      ttk.Button(group, text="Gaussiano", command=self.apply_gaussian).pack(side='left', padx=2)

  def create_morphological_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Morfológicas", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Button(group, text='DILATAÇÃO', command=self.limiar_images).pack(side='left', padx=2)
      ttk.Button(group, text='EROSÃO', command=self.and_images).pack(side='left', padx=2)
      ttk.Button(group, text='ABERTURA', command=self.or_images).pack(side='left', padx=2)
      ttk.Button(group, text='FECHAMENTO', command=self.xor_images).pack(side='left', padx=2)
      ttk.Button(group, text='CONTORNO', command=self.not_image_a).pack(side='left', padx=2)

  def load_image_a(self):
      file_path = filedialog.askopenfilename()
      if file_path:
          self.image_a_label.config(text=f'Imagem A: {file_path}')
          image = Image.open(file_path).convert('RGB')
          image.thumbnail((200, 200))
          self.image_a = ImageTk.PhotoImage(image)
          self.image_a_display.config(image=self.image_a)

  def load_image_b(self):
      file_path = filedialog.askopenfilename()
      if file_path:
          self.image_b_label.config(text=f'Imagem B: {file_path}')
          image = Image.open(file_path).convert('RGB')
          image.thumbnail((200, 200))
          self.image_b = ImageTk.PhotoImage(image)
          self.image_b_display.config(image=self.image_b)

############################################################
#            INICIO OPERAÇÕES ARITIMETICAS
############################################################

  def convert_to_grayscale(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a conversão.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      grayscale_image = image_a.convert('L')  # Converte para escala de cinza
      grayscale_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(grayscale_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = grayscale_image

  def add_images_with_value(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Error", "Carregue ambas as imagens antes de realizar a operação.")
          return

      addition_value = simpledialog.askinteger(
          "Adição de Valor", "Adicione o valor do brilho (0 a 255), 1 para apenas adição", minvalue=0, maxvalue=255)
      if addition_value is None:
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)

      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = min(255, image_a.getpixel((i, j))[0] + image_b.getpixel((i, j))[0] + addition_value)
              g = min(255, image_a.getpixel((i, j))[1] + image_b.getpixel((i, j))[1] + addition_value)
              b = min(255, image_a.getpixel((i, j))[2] + image_b.getpixel((i, j))[2] + addition_value)
              result_image.putpixel((i, j), (r, g, b))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def subtract_images_with_value(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return

      subtraction_value = simpledialog.askinteger(
          "Valor de Subtração", "Adicione o valor da subtração (0 a 255), 1 para apenas subtração padrão", minvalue=0, maxvalue=255)
      if subtraction_value is None:
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)

      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = max(0, image_a.getpixel((i, j))[0] - image_b.getpixel((i, j))[0] - subtraction_value)
              g = max(0, image_a.getpixel((i, j))[1] - image_b.getpixel((i, j))[1] - subtraction_value)
              b = max(0, image_a.getpixel((i, j))[2] - image_b.getpixel((i, j))[2] - subtraction_value)
              result_image.putpixel((i, j), (r, g, b))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def multiply_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return


      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)


      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = min(255, (image_a.getpixel((i, j))[0] * image_b.getpixel((i, j))[0]) // 255)
              g = min(255, (image_a.getpixel((i, j))[1] * image_b.getpixel((i, j))[1]) // 255)
              b = min(255, (image_a.getpixel((i, j))[2] * image_b.getpixel((i, j))[2]) // 255)
              result_image.putpixel((i, j), (r, g, b))


      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def divide_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return


      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)


      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = min(255, int(image_a.getpixel((i, j))[0] / (image_b.getpixel((i, j))[0] + 1e-6) * 255))
              g = min(255, int(image_a.getpixel((i, j))[1] / (image_b.getpixel((i, j))[1] + 1e-6) * 255))
              b = min(255, int(image_a.getpixel((i, j))[2] / (image_b.getpixel((i, j))[2] + 1e-6) * 255))
              result_image.putpixel((i, j), (r, g, b))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def save_result_image(self):
      if self.result_image_pil:
          file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
          if file_path:
              self.result_image_pil.save(file_path)
              messagebox.showinfo("Imagem Salva", "A imagem foi salva com sucesso!")
      else:
          messagebox.showerror("Erro", "Nenhuma imagem resultante para salvar.")

  def convert_rgb_to_yiq(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a conversão.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size

      result_image = Image.new('RGB', (width, height))
      for x in range(width):
          for y in range(height):
              r, g, b = image_a.getpixel((x, y))

              y_val = 0.299 * r + 0.587 * g + 0.114 * b
              i_val = 0.596 * r - 0.274 * g - 0.322 * b
              q_val = 0.211 * r - 0.523 * g + 0.312 * b

              r = y_val + 0.956 * i_val + 0.621 * q_val
              g = y_val - 0.272 * i_val - 0.647 * q_val
              b = y_val - 1.106 * i_val + 1.703 * q_val
              r, g, b = [int(max(0, min(255, x))) for x in (r, g, b)]
              result_image.putpixel((x, y), (r, g, b))


      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def convert_rgb_to_hsi(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a conversão.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size

      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r, g, b = [x / 255.0 for x in image_a.getpixel((i, j))]  
              intensity = (r + g + b) / 3
              min_rgb = min(r, g, b)
              saturation = 0 if (r + g + b) == 0 else 1 - (3 / (r + g + b)) * min_rgb

              if saturation == 0:
                  hue = 0
              else:
                  num = 0.5 * ((r - g) + (r - b))
                  den = math.sqrt((r - g) ** 2 + (r - b) * (g - b))
                  theta = math.acos(num / (den + 1e-6))
                  if b <= g:
                      hue = theta
                  else:
                      hue = 2 * math.pi - theta

              h = hue * 180 / math.pi  
              if h < 120:
                  b = intensity * (1 - saturation)
                  r = intensity * (1 + (saturation * math.cos(h)) / math.cos(60 - h))
                  g = 3 * intensity - (r + b)
              elif h < 240:
                  h = h - 120
                  r = intensity * (1 - saturation)
                  g = intensity * (1 + (saturation * math.cos(h)) / math.cos(60 - h))
                  b = 3 * intensity - (r + g)
              else:
                  h = h - 240
                  g = intensity * (1 - saturation)
                  b = intensity * (1 + (saturation * math.cos(h)) / math.cos(60 - h))
                  r = 3 * intensity - (g + b)
              r, g, b = [int(max(0, min(255, x * 255))) for x in (r, g, b)]
              result_image.putpixel((i, j), (r, g, b))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def to_double(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a conversão.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size

      result_image = Image.new('RGB', (width, height))
      for x in range(width):
          for y in range(height):
              r, g, b = image_a.getpixel((x, y))
              r_double = r / 255.0
              g_double = g / 255.0
              b_double = b / 255.0

              r_display = int(r_double * 255)
              g_display = int(g_double * 255)
              b_display = int(b_double * 255)
              result_image.putpixel((x, y), (r_display, g_display, b_display))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image
      
  def blend_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return
    
      alpha = simpledialog.askfloat("Valor de Alpha", "Insira o valor de alpha (0.0 a 1.0):", minvalue=0.0, maxvalue=1.0)
      if alpha is None:
          return
    
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)
    
      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r_a, g_a, b_a = image_a.getpixel((i, j))
              r_b, g_b, b_b = image_b.getpixel((i, j))
              r = int(alpha * r_a + (1 - alpha) * r_b)
              g = int(alpha * g_a + (1 - alpha) * g_b)
              b = int(alpha * b_a + (1 - alpha) * b_b)
              result_image.putpixel((i, j), (r, g, b))
    
      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

############################################################
#            FIM OPERAÇÕES ARITIMETICAS
############################################################

############################################################
#            INICIO OPERAÇÕES LÓGICAS
############################################################


  def and_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return
    
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)
    
      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = image_a.getpixel((i, j))[0] & image_b.getpixel((i, j))[0]
              g = image_a.getpixel((i, j))[1] & image_b.getpixel((i, j))[1]
              b = image_a.getpixel((i, j))[2] & image_b.getpixel((i, j))[2]
              result_image.putpixel((i, j), (r, g, b))
    
      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image
      
  def or_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return
    
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)
    
      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = image_a.getpixel((i, j))[0] | image_b.getpixel((i, j))[0]
              g = image_a.getpixel((i, j))[1] | image_b.getpixel((i, j))[1]
              b = image_a.getpixel((i, j))[2] | image_b.getpixel((i, j))[2]
              result_image.putpixel((i, j), (r, g, b))
    
      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image
      
  def xor_images(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")
          return
    
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)
    
      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = image_a.getpixel((i, j))[0] ^ image_b.getpixel((i, j))[0]
              g = image_a.getpixel((i, j))[1] ^ image_b.getpixel((i, j))[1]
              b = image_a.getpixel((i, j))[2] ^ image_b.getpixel((i, j))[2]
              result_image.putpixel((i, j), (r, g, b))
    
      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image
      
  def not_image_a(self):
        if not self.image_a:
            messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
            return
    
        image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
        width, height = image_a.size
    
        result_image = Image.new('RGB', (width, height))
        for i in range(width):
            for j in range(height):
                r, g, b = image_a.getpixel((i, j))
                r = 255 - r
                g = 255 - g
                b = 255 - b
                result_image.putpixel((i, j), (r, g, b))
    
        result_image.thumbnail((200, 200))
        self.result_image = ImageTk.PhotoImage(result_image)
        self.result_image_label.config(image=self.result_image)
        self.result_image_pil = result_image

  def limiar_images(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      threshold = simpledialog.askinteger("Limiar", "Digite o valor do limiar (0-255):", minvalue=0, maxvalue=255)
      if threshold is None:
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size

      result_image = Image.new('RGB', (width, height))

      for x in range(width):
          for y in range(height):
              r, g, b = image_a.getpixel((x, y))

              gray = int(0.299 * r + 0.587 * g + 0.114 * b)

              if gray > threshold:
                  result_image.putpixel((x, y), (255, 255, 255))  
              else:
                  result_image.putpixel((x, y), (0, 0, 0))  

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

############################################################
#            FIM OPERAÇÕES LÓGICAS
############################################################

  def calculate_and_equalize_histogram(self):
        if not self.image_a:
            messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
            return
        
        image_path = self.image_a_label.cget("text").split(": ")[1]
        image = Image.open(image_path).convert('L')
        width, height = image.size

        histogram = [0] * 256
        for i in range(width):
            for j in range(height):
                intensity = image.getpixel((i, j))
                histogram[intensity] += 1

        cdf = [0] * 256
        cdf[0] = histogram[0]
        for i in range(1, 256):
            cdf[i] = cdf[i - 1] + histogram[i]

        cdf_min = min(cdf)
        cdf_max = max(cdf)
        cdf_normalized = [(cdf[i] - cdf_min) / (cdf_max - cdf_min) * 255 for i in range(256)]

        equalized_image = Image.new('L', (width, height))
        for i in range(width):
            for j in range(height):
                intensity = image.getpixel((i, j))
                new_intensity = int(cdf_normalized[intensity])
                equalized_image.putpixel((i, j), new_intensity)

        equalized_histogram = [0] * 256
        for i in range(width):
            for j in range(height):
                intensity = equalized_image.getpixel((i, j))
                equalized_histogram[intensity] += 1

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.bar(range(256), histogram, width=1.0, edgecolor='blue')
        plt.title('Histograma Original')
        plt.xlabel('Intensidade de Pixel')
        plt.ylabel('Número de Pixels')
        plt.xlim([0, 255])

        plt.subplot(1, 2, 2)
        plt.bar(range(256), equalized_histogram, width=1.0, edgecolor='blue')
        plt.title('Histograma Equalizado')
        plt.xlabel('Intensidade de Pixel')
        plt.ylabel('Número de Pixels')
        plt.xlim([0, 255])

        plt.show()

############################################################
#            COMEÇO OPERAÇÕES DE REALCE DE IMAGENS
############################################################

  def apply_media(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
      width, height = image_a.size

      result_image = Image.new('L', (width, height))

      for i in range(1, height - 1):
          for j in range(1, width - 1):
              window = [
                  image_a.getpixel((x, y))
                  for y in range(i-1, i+2)
                  for x in range(j-1, j+2)
              ]
              avg_val = sum(window) // 9
              result_image.putpixel((j, i), avg_val)

      for i in range(height):
          result_image.putpixel((0, i), image_a.getpixel((0, i)))
          result_image.putpixel((width-1, i), image_a.getpixel((width-1, i)))
      for j in range(width):
          result_image.putpixel((j, 0), image_a.getpixel((j, 0)))
          result_image.putpixel((j, height-1), image_a.getpixel((j, height-1)))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def apply_mediana(self, window_size=3):
    if not self.image_a:
        messagebox.showerror("Error", "Load image A before performing the operation.")
        return

    image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
    width, height = image_a.size

    result_image = Image.new('L', (width, height))

    def calculate_median(values):
        sorted_values = sorted(values)
        size = len(sorted_values)
        middle = size // 2
        if size % 2 == 0:
            return (sorted_values[middle - 1] + sorted_values[middle]) // 2
        else:
            return sorted_values[middle]

    half_window = window_size // 2
    for i in range(half_window, height - half_window):
        for j in range(half_window, width - half_window):
            window = [
                image_a.getpixel((x, y))
                for y in range(i - half_window, i + half_window + 1)
                for x in range(j - half_window, j + half_window + 1)
            ]
            median_val = calculate_median(window)
            result_image.putpixel((j, i), median_val)

    for i in range(height):
        result_image.putpixel((0, i), image_a.getpixel((0, i)))
        result_image.putpixel((width-1, i), image_a.getpixel((width-1, i)))
    for j in range(width):
        result_image.putpixel((j, 0), image_a.getpixel((j, 0)))
        result_image.putpixel((j, height-1), image_a.getpixel((j, height-1)))

    result_image.thumbnail((200, 200))
    self.result_image = ImageTk.PhotoImage(result_image)
    self.result_image_label.config(image=self.result_image)
    self.result_image_pil = result_image


############################################################
#            FIM OPERAÇÕES DE REALCE DE IMAGENS
############################################################

############################################################
#            COMEÇO OPERAÇÕES DE DETECÇÃO DE BORDAS
############################################################

  def apply_prewitt(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
      width, height = image_a.size

      kernel_x = [[-1, 0, 1],
                  [-1, 0, 1],
                  [-1, 0, 1]]
      kernel_y = [[-1, -1, -1],
                  [0, 0, 0],
                  [1, 1, 1]]

      gradient_x = self.convolve(image_a, kernel_x)
      gradient_y = self.convolve(image_a, kernel_y)

      result_image = Image.new('L', (width, height))
      max_magnitude = 0

      for y in range(height):
          for x in range(width):
              gx = gradient_x[y][x]
              gy = gradient_y[y][x]
              magnitude = int(math.sqrt(gx**2 + gy**2))
              max_magnitude = max(max_magnitude, magnitude)
              result_image.putpixel((x, y), magnitude)

      for y in range(height):
          for x in range(width):
              normalized = int(result_image.getpixel((x, y)) / max_magnitude * 255)
              result_image.putpixel((x, y), normalized)

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def apply_sobel(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
      width, height = image_a.size

      kernel_x = [[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]]
      kernel_y = [[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]]

      gradient_x = self.convolve(image_a, kernel_x)
      gradient_y = self.convolve(image_a, kernel_y)

      result_image = Image.new('L', (width, height))
      max_magnitude = 0

      for y in range(height):
          for x in range(width):
              gx = gradient_x[y][x]
              gy = gradient_y[y][x]
              magnitude = int(math.sqrt(gx**2 + gy**2))
              max_magnitude = max(max_magnitude, magnitude)
              result_image.putpixel((x, y), magnitude)

      for y in range(height):
          for x in range(width):
              normalized = int(result_image.getpixel((x, y)) / max_magnitude * 255)
              result_image.putpixel((x, y), normalized)

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def apply_laplacian(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
      width, height = image_a.size

      kernel = [[0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]]

      result_image = Image.new('L', (width, height))

      for y in range(1, height - 1):
          for x in range(1, width - 1):
              sum = 0
              for ky in range(3):
                  for kx in range(3):
                      pixel = image_a.getpixel((x + kx - 1, y + ky - 1))
                      sum += pixel * kernel[ky][kx]
              sum = max(0, min(255, sum + 128))
              result_image.putpixel((x, y), int(sum))

      for y in range(height):
          result_image.putpixel((0, y), image_a.getpixel((0, y)))
          result_image.putpixel((width-1, y), image_a.getpixel((width-1, y)))
      for x in range(width):
          result_image.putpixel((x, 0), image_a.getpixel((x, 0)))
          result_image.putpixel((x, height-1), image_a.getpixel((x, height-1)))

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

  def convolve(self, image, kernel):
      width, height = image.size
      k_height = len(kernel)
      k_width = len(kernel[0])

      pad_height = k_height // 2
      pad_width = k_width // 2

      output = [[0 for _ in range(width)] for _ in range(height)]

      for y in range(height):
          for x in range(width):
              sum = 0
              for ky in range(k_height):
                  for kx in range(k_width):
                      img_x = x + kx - pad_width
                      img_y = y + ky - pad_height
                      if 0 <= img_x < width and 0 <= img_y < height:
                          pixel = image.getpixel((img_x, img_y))
                          sum += pixel * kernel[ky][kx]
              output[y][x] = sum

      return output

############################################################
#            FIM OPERAÇÕES DE DETECÇÃO DE BORDAS
############################################################

############################################################
#            COMEÇO OPERAÇÕES DE FILTROS
############################################################

  def apply_gaussian(self):
      if not self.image_a:
          messagebox.showerror("Erro", "Carregue a imagem A antes de realizar a operação.")
          return

      sigma = float(self.gaussian_sigma.get())
      
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('L')
      width, height = image_a.size

      kernel_size = int(6 * sigma)
      if kernel_size % 2 == 0:
          kernel_size += 1

      kernel = [[0 for _ in range(kernel_size)] for _ in range(kernel_size)]
      center = kernel_size // 2
      kernel_sum = 0
      for y in range(kernel_size):
          for x in range(kernel_size):
              dx = x - center
              dy = y - center
              value = math.exp(-(dx**2 + dy**2) / (2 * sigma**2))
              kernel[y][x] = value
              kernel_sum += value

      for y in range(kernel_size):
          for x in range(kernel_size):
              kernel[y][x] /= kernel_sum

      result_image = Image.new('L', (width, height))
      for y in range(height):
          for x in range(width):
              pixel_sum = 0
              weight_sum = 0
              for ky in range(kernel_size):
                  for kx in range(kernel_size):
                      nx = x + kx - center
                      ny = y + ky - center
                      if 0 <= nx < width and 0 <= ny < height:
                          weight = kernel[ky][kx]
                          pixel = image_a.getpixel((nx, ny))
                          pixel_sum += pixel * weight
                          weight_sum += weight
              
              new_pixel = int(pixel_sum / weight_sum)
              result_image.putpixel((x, y), new_pixel)

      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)
      self.result_image_pil = result_image

############################################################
#            FIM OPERAÇÕES DE FILTROS
############################################################

############################################################
#            COMEÇO OPERAÇÕES DE MORFOLOGICAS
############################################################



############################################################
#            FIM OPERAÇÕES DE MORFOLOGICAS
############################################################

if __name__ == "__main__":
    app = ImageProcessingApp()
    app.mainloop()
