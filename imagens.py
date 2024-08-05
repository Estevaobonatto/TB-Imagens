import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ImageProcessingApp(QMainWindow):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Operações Aritméticas e Lógicas em Imagens')
      self.setGeometry(0, 0, 1280, 720)

      self.setStyleSheet("""
          QMainWindow, QWidget {
              background-color: #2b2b2b;
              color: #ffffff;
          }
          QPushButton {
              background-color: #3a3a3a;
              color: #ffffff;
              border: 1px solid #555555;
              padding: 5px;
          }
          QPushButton:hover {
              background-color: #4a4a4a;
          }
          QLabel {
              border: 1px solid #555555;
          }
          QGroupBox {
              border: 1px solid #555555;
              margin-top: 0.5em;
          }
          QGroupBox::title {
              subcontrol-origin: margin;
              left: 10px;
              padding: 0 3px 0 3px;
          }
          QLineEdit {
              background-color: #3a3a3a;
              color: #ffffff;
              border: 1px solid #555555;
          }
      """)

      central_widget = QWidget()
      self.setCentralWidget(central_widget)
      main_layout = QHBoxLayout(central_widget)

      left_column = QVBoxLayout()
      self.image_a = QLabel('Imagem A')
      self.image_a.setAlignment(Qt.AlignCenter)
      self.image_a.setMinimumSize(300, 300)
      left_column.addWidget(self.image_a)
      left_column.addWidget(QPushButton('Carregar imagem A...'))
      left_column.addWidget(QPushButton('RGB -> YIQ'))
      left_column.addWidget(QPushButton('RGB -> HSI'))
      left_column.addWidget(QPushButton('ToDouble'))

      middle_column = QVBoxLayout()
      middle_column.addWidget(self.create_arithmetic_operations_group())
      middle_column.addWidget(self.create_logical_operations_group())
      middle_column.addWidget(self.create_image_enhancement_group())
      middle_column.addWidget(self.create_edge_detection_group())
      middle_column.addWidget(self.create_gaussian_filter_group())
      middle_column.addStretch()

      right_column = QVBoxLayout()
      self.image_b = QLabel('Imagem B')
      self.image_b.setAlignment(Qt.AlignCenter)
      self.image_b.setMinimumSize(300, 200)
      right_column.addWidget(self.image_b)
      right_column.addWidget(QPushButton('Carregar imagem B...'))
      right_column.addWidget(self.create_morphological_operations_group())
      self.result_image = QLabel('Imagem Resultante')
      self.result_image.setAlignment(Qt.AlignCenter)
      self.result_image.setMinimumSize(300, 200)
      right_column.addWidget(self.result_image)
      right_column.addWidget(QPushButton('Salvar Imagem...'))

      main_layout.addLayout(left_column, 2)
      main_layout.addLayout(middle_column, 3)
      main_layout.addLayout(right_column, 2)

      histogram_layout = QHBoxLayout()
      histogram_layout.addWidget(self.create_histogram("Histograma da Imagem Original (A)"))
      histogram_layout.addWidget(self.create_histogram("Histograma Equalizado"))
      
      vertical_layout = QVBoxLayout()
      vertical_layout.addLayout(main_layout, 5)
      vertical_layout.addLayout(histogram_layout, 1)
      
      central_widget.setLayout(vertical_layout)

  def create_arithmetic_operations_group(self):
      group = QGroupBox("Operações Aritméticas")
      layout = QGridLayout()
      operations = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Média', 'Blending']
      for i, op in enumerate(operations):
          layout.addWidget(QPushButton(op), i // 2, i % 2)
      group.setLayout(layout)
      return group

  def create_logical_operations_group(self):
      group = QGroupBox("Operações Lógicas")
      layout = QGridLayout()
      operations = ['AND', 'OR', 'XOR', 'NOT']
      for i, op in enumerate(operations):
          layout.addWidget(QPushButton(op), i // 2, i % 2)
      group.setLayout(layout)
      return group

  def create_image_enhancement_group(self):
      group = QGroupBox("Realce de Imagens")
      layout = QGridLayout()
      operations = ['MAX', 'MIN', 'MÉDIA', 'MEDIANA', 'ORDEM', 'SUAV. CONSERVATIVA']
      for i, op in enumerate(operations):
          layout.addWidget(QPushButton(op), i // 2, i % 2)
      layout.addWidget(QLineEdit(), 2, 1)
      group.setLayout(layout)
      return group

  def create_edge_detection_group(self):
      group = QGroupBox("Detecção de Bordas")
      layout = QHBoxLayout()
      operations = ['Prewitt', 'Sobel', 'Laplaciano']
      for op in operations:
          layout.addWidget(QPushButton(op))
      group.setLayout(layout)
      return group

  def create_gaussian_filter_group(self):
      group = QGroupBox("Filtragem Gaussiana")
      layout = QVBoxLayout()
      layout.addWidget(QLabel("Desvio Padrão (Sigma):"))
      layout.addWidget(QLineEdit("0.1"))
      layout.addWidget(QPushButton("Gaussiano"))
      group.setLayout(layout)
      return group

  def create_morphological_operations_group(self):
      group = QGroupBox("Operações Morfológicas")
      layout = QVBoxLayout()
      operations = ['Dilatação', 'Erosão', 'Abertura', 'Fechamento', 'Contorno']
      for op in operations:
          layout.addWidget(QPushButton(op))
      group.setLayout(layout)
      return group

  def create_histogram(self, title):
      fig = Figure(figsize=(4, 1.5), dpi=100)
      canvas = FigureCanvas(fig)
      ax = fig.add_subplot(111)
      ax.set_title(title, fontsize=8, color='white')
      ax.set_xlabel('Intensidade', fontsize=6, color='white')
      ax.set_ylabel('Frequência', fontsize=6, color='white')
      ax.tick_params(axis='both', which='major', labelsize=6, colors='white')
      ax.set_facecolor('#2b2b2b')
      fig.patch.set_facecolor('#2b2b2b')
      return canvas

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = ImageProcessingApp()
  ex.show()
  sys.exit(app.exec_())
