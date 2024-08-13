import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ImageProcessingApp(tk.Tk):
  def __init__(self):
      super().__init__()
      self.title('Trabalho de Procesamento de Imagens - Semestre 2024-2')
      self.geometry('800x600')  # Ajuste a largura e altura da janela
      self.configure(bg='#2b2b2b')

      # Configure style
      style = ttk.Style(self)
      style.theme_use('clam')
      style.configure('TButton', background='#3a3a3a', foreground='white', borderwidth=1, focusthickness=3, focuscolor='none')
      style.map('TButton', background=[('active', '#4a4a4a')])
      style.configure('TLabel', background='#2b2b2b', foreground='white')
      style.configure('TFrame', background='#2b2b2b')
      style.configure('TLabelFrame', background='#2b2b2b', foreground='white', borderwidth=1)

      self.create_widgets()

  def create_widgets(self):
      # Left column
      left_frame = ttk.Frame(self, padding=5)
      left_frame.grid(row=0, column=0, sticky='ns')
      
      self.image_a_label = ttk.Label(left_frame, text='Imagem A')
      self.image_a_label.pack(pady=5)
      
      ttk.Button(left_frame, text='Carregar imagem A...', command=self.load_image_a).pack(pady=5)
      ttk.Button(left_frame, text='RGB -> YIQ').pack(pady=5)
      ttk.Button(left_frame, text='RGB -> HSI').pack(pady=5)
      ttk.Button(left_frame, text='ToDouble').pack(pady=5)

      # Middle column
      middle_frame = ttk.Frame(self, padding=5)
      middle_frame.grid(row=0, column=1, sticky='ns')

      self.create_arithmetic_operations_group(middle_frame)
      self.create_logical_operations_group(middle_frame)
      self.create_image_enhancement_group(middle_frame)
      self.create_edge_detection_group(middle_frame)
      self.create_gaussian_filter_group(middle_frame)

      # Right column
      right_frame = ttk.Frame(self, padding=5)
      right_frame.grid(row=0, column=2, sticky='ns')

      self.image_b_label = ttk.Label(right_frame, text='Imagem B')
      self.image_b_label.pack(pady=5)
      
      ttk.Button(right_frame, text='Carregar imagem B...', command=self.load_image_b).pack(pady=5)
      self.create_morphological_operations_group(right_frame)
      
      self.result_image_label = ttk.Label(right_frame, text='Imagem Resultante')
      self.result_image_label.pack(pady=5)
      
      ttk.Button(right_frame, text='Salvar Imagem...').pack(pady=5)

  def create_arithmetic_operations_group(self, parent):
      group = ttk.LabelFrame(parent, text="Operações Aritméticas", padding=5)
      group.pack(pady=5, fill='x')
      operations = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Média', 'Blending']
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

  def load_image_b(self):
      file_path = filedialog.askopenfilename()
      if file_path:
          self.image_b_label.config(text=f'Imagem B: {file_path}')

if __name__ == '__main__':
  app = ImageProcessingApp()
  app.mainloop()