from PyQt5.QtWidgets import QApplication, QOpenGLWidget
#ЭТОКВАДРАТИГ
class OGLQUAD(QOpenGLWidget):
	def initializeGL(self):
		pass
	def resizeGL(self, width, height):
		pass
	def paintGL(self):
		pass

if __name__=="__main__":
	app = QApplication([])
	
	glquad = OGLQUAD()
	glquad.resize(200, 200)
	glquad.show()
	
	app.exec()
	
