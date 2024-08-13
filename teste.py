def test_imports():
  try:
      import sys
      from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
      from PyQt5.QtGui import QPixmap
      from PyQt5.QtCore import Qt
      import matplotlib
      from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
      from matplotlib.figure import Figure
      print("Todas as bibliotecas foram importadas com sucesso.")
      return QApplication, QMainWindow, QLabel, FigureCanvas, Figure
  except ImportError as e:
      print(f"Erro ao importar bibliotecas: {e}")
      return None, None, None, None, None

def test_pyqt5(QApplication, QMainWindow, QLabel):
  try:
      app = QApplication([])
      window = QMainWindow()
      label = QLabel("Teste de PyQt5")
      window.setCentralWidget(label)
      window.show()
      print("PyQt5 está funcionando corretamente.")
      app.quit()
  except Exception as e:
      print(f"Erro ao testar PyQt5: {e}")

def test_matplotlib(FigureCanvas, Figure):
  try:
      fig = Figure()
      canvas = FigureCanvas(fig)
      ax = fig.add_subplot(111)
      ax.plot([0, 1, 2], [0, 1, 4])
      print("Matplotlib está funcionando corretamente.")
  except Exception as e:
      print(f"Erro ao testar Matplotlib: {e}")

if __name__ == "__main__":
  QApplication, QMainWindow, QLabel, FigureCanvas, Figure = test_imports()
  if QApplication and QMainWindow and QLabel:
      test_pyqt5(QApplication, QMainWindow, QLabel)
  if FigureCanvas and Figure:
      test_matplotlib(FigureCanvas, Figure)