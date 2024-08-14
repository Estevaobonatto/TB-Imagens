import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageOps
import numpy as np

class ImageProcessingApp(tk.Tk):
  def __init__(self):
      super().__init__()
      self.title('Trabalho de Procesamento de Imagens - Semestre 2024-2')
      self.geometry('800x600')
      self.configure(bg='#2b2b2b')

      # Configure style
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
      # Main frame
      main_frame = ttk.Frame(self, padding=5)
      main_frame.pack(fill='both', expand=True)

      # Image A
      left_frame = ttk.Frame(main_frame, padding=5)
      left_frame.pack(side='left', fill='y')

      self.image_a_label = ttk.Label(left_frame, text='Imagem A')
      self.image_a_label.pack(pady=5)

      self.image_a_display = ttk.Label(left_frame)
      self.image_a_display.pack(pady=5)

      ttk.Button(left_frame, text='Carregar imagem A...', command=self.load_image_a).pack(pady=5)
      ttk.Button(left_frame, text='RGB -> YIQ').pack(pady=5)
      ttk.Button(left_frame, text='RGB -> HSI').pack(pady=5)
      ttk.Button(left_frame, text='ToDouble').pack(pady=5)

      # Operations
      operations_frame = ttk.Frame(main_frame, padding=5)
      operations_frame.pack(side='left', fill='both', expand=True)

      self.create_arithmetic_operations_group(operations_frame)
      self.create_logical_operations_group(operations_frame)
      self.create_image_enhancement_group(operations_frame)
      self.create_edge_detection_group(operations_frame)
      self.create_gaussian_filter_group(operations_frame)
      self.create_morphological_operations_group(operations_frame)

      # Image B
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
      operations = ['Multiplicação', 'Divisão', 'Média', 'Blending']
      for op in operations:
          ttk.Button(group, text=op).pack(side='left', padx=2)

  def create_logical_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Lógicas", padding=5)
      group.pack(pady=5, fill='x')
      operations = ['AND', 'OR', 'XOR', 'NOT']
      for op in operations:
          ttk.Button(group, text=op).pack(side='left', padx=2)

  def create_image_enhancement_group(self, parent):
      group = ttk.LabelFrame(parent, text="Realce de Imagens", padding=5)
      group.pack(pady=5, fill='x')
      operations = ['MAX', 'MIN', 'MÉDIA', 'MEDIANA', 'ORDEM', 'SUAV. CONSERVATIVA']
      for op in operations:
          ttk.Button(group, text=op).pack(side='left', padx=2)

  def create_edge_detection_group(self, parent):
      group = ttk.LabelFrame(parent, text="Detecção de Bordas", padding=5)
      group.pack(pady=5, fill='x')
      operations = ['Prewitt', 'Sobel', 'Laplaciano']
      for op in operations:
          ttk.Button(group, text=op).pack(side='left', padx=2)

  def create_gaussian_filter_group(self, parent):
      group = ttk.LabelFrame(parent, text="Filtragem Gaussiana", padding=5)
      group.pack(pady=5, fill='x')
      ttk.Label(group, text="Desvio Padrão (Sigma):").pack(side='left', padx=2)
      ttk.Entry(group, width=5).pack(side='left', padx=2)
      ttk.Button(group, text="Gaussiano").pack(side='left', padx=2)

  def create_morphological_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Morfológicas", padding=5)
      group.pack(pady=5, fill='x')
      operations = ['Dilatação', 'Erosão', 'Abertura', 'Fechamento', 'Contorno']
      for op in operations:
          ttk.Button(group, text=op).pack(side='left', padx=2)

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

  def add_images_with_value(self):
      if not self.image_a or not self.image_b:
          messagebox.showerror("Error", "Load both images before performing the operation.")
          return

      # Ask for the addition value
      addition_value = simpledialog.askinteger(
          "Addition Value", "Adicione o valor do brilho (0 a 255), 1 para apenas adição", minvalue=0, maxvalue=255)
      if addition_value is None:
          return

      # Open images and resize them to the same size
      image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGB')
      image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGB')
      width, height = image_a.size
      image_b = image_b.resize((width, height), Image.LANCZOS)

      # Add images with the given value
      result_image = Image.new('RGB', (width, height))
      for i in range(width):
          for j in range(height):
              r = min(255, image_a.getpixel((i, j))[0] + image_b.getpixel((i, j))[0] + addition_value) if addition_value > 0 else max(0, image_a.getpixel((i, j))[0] + image_b.getpixel((i, j))[0] - addition_value)
              g = min(255, image_a.getpixel((i, j))[1] + image_b.getpixel((i, j))[1] + addition_value) if addition_value > 0 else max(0, image_a.getpixel((i, j))[1] + image_b.getpixel((i, j))[1] - addition_value)
              b = min(255, image_a.getpixel((i, j))[2] + image_b.getpixel((i, j))[2] + addition_value) if addition_value > 0 else max(0, image_a.getpixel((i, j))[2] + image_b.getpixel((i, j))[2] - addition_value)
              result_image.putpixel((i, j), (r, g, b))

      # Convert result to image
      result_image.thumbnail((200, 200))
      self.result_image = ImageTk.PhotoImage(result_image)
      self.result_image_label.config(image=self.result_image)

  def subtract_images_with_value(self):
      if self.image_a and self.image_b:
          # Ask for the subtraction value
          value = simpledialog.askinteger("Valor de Subtração", "Insira o valor a ser subtraído:", minvalue=0, maxvalue=255)
          if value is None:
              return

          # Open images
          image_a = Image.open(self.image_a_label.cget("text").split(": ")[1]).convert('RGBA')
          image_b = Image.open(self.image_b_label.cget("text").split(": ")[1]).convert('RGBA')

          # Resize images to the same size
          width, height = image_a.size
          image_b = image_b.resize((width, height), Image.LANCZOS)

          # Convert images to arrays
          image_a_array = np.array(image_a)
          image_b_array = np.array(image_b)

          # Subtract images with the given value
          result_array = np.abs(image_a_array - image_b_array - value)

          # Clip values to ensure they're in the valid range (0-255)
          result_array = np.clip(result_array, 0, 255).astype(np.uint8)

          # Convert result to image
          self.result_image_pil = Image.fromarray(result_array, 'RGBA')
          result_image = self.result_image_pil.copy()
          result_image.thumbnail((200, 200))
          self.result_image = ImageTk.PhotoImage(result_image)
          self.result_image_label.config(image=self.result_image)
      else:
          messagebox.showerror("Erro", "Carregue ambas as imagens antes de realizar a operação.")

  def save_result_image(self):
      if self.result_image_pil:
          file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
          if file_path:
              self.result_image_pil.save(file_path)
              messagebox.showinfo("Imagem Salva", "A imagem foi salva com sucesso!")
      else:
          messagebox.showerror("Erro", "Nenhuma imagem resultante para salvar.")

if __name__ == '__main__':
  app = ImageProcessingApp()
  app.mainloop()