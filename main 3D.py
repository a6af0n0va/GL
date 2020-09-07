from PyQt5.QtWidgets import QApplication, QOpenGLWidget
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtCore import Qt

import OpenGL.GL as gl
class OGLQUAD(QOpenGLWidget):
	def __init__(self):
		super().__init__()
		#необходимо добавить переменные:
		#вращение относительно х
		#вращение относительно у
		#смещение координат
		self.xangle = 0
		self.yangle = 0
		self.zoom = 1
		self.angle = 0
		self.xoffset = 0
		self.yoffset = 0 
	#необходимо обработать событие mousePressEvent
		#запомним точку, где была нажата мышь

	#необходимо обработать событие mouseMoveEvent
		#рассчитаем новые значения вращения и смещения
	def wheelEvent(self, event):
		
		self.angle += event.angleDelta().y()
		self.zoom = 1 + self.angle/1000 
		print(self.zoom)
		self.update()
		
	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.mouspresd = True
			self.x = event.x()
			self.y = event.y()
		
	def mouseMoveEvent(self, event):
		if self.mouspresd == True:
			self.xangle = event.x() - self.x
			self.yangle = event.y() - self.y
			#print(self.xangle, "   ", self.yangle)
			self.update()

	def mouseReleaseEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.mouspresd = False
			
	def initializeGL(self):
		print("init")
		gl.glEnable(gl.GL_DEPTH_TEST)
		gl.glShadeModel(gl.GL_FLAT)
		gl.glClearColor(0,0,0,1)
	def resizeGL(self, width, height):
		print("resiz")
		gl.glMatrixMode(gl.GL_PROJECTION)
		gl.glLoadIdentity()
		gl.glViewport(0,0, width, height)
		gl.glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
	def paintGL(self):
		#print("paint")
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
		gl.glMatrixMode(gl.GL_MODELVIEW)
		gl.glLoadIdentity()
		
		gl.glTranslate(0.0, 0.0, -3.0)
		gl.glRotate(self.xangle, 1.0, 0.0, 0.0)
		gl.glRotate(self.yangle, 0.0, 1.0, 0.0)
		gl.glScale(self.zoom, self.zoom, self.zoom)
		#gl.glRotate(45, 0.0, 0.0, 1.0)
		
		#|1 0 0| |X| 
		#|0 1 0| |Y|
		#|0 0 1| |Z|
		
		gl.glBegin(gl.GL_TRIANGLE_FAN)
		gl.glColor4f(0.0, 1.0, 0.0, 1.0)
		gl.glVertex(0.0, 1, 0.0)
		gl.glVertex(-1, -1, 1)
		gl.glVertex(1, -1, 1)
		gl.glColor4f(1.0, 1.0, 0.0, 1.0)
		gl.glVertex(1, -1, -1)
		gl.glColor4f(0.0, 0.0, 1.0, 1.0)
		gl.glVertex(-1, -1, -1)
		gl.glColor4f(1.0, 1.0, 1.0, 1.0)
		gl.glVertex(-1, -1, 1)
		gl.glEnd()
		
		gl.glBegin(gl.GL_QUADS)
		gl.glColor4f(1.0, 0.0, 0.0, 1.0)
		gl.glVertex(-1, -1, 1)
		gl.glVertex(1, -1, 1)
		gl.glVertex(1, -1, -1)
		gl.glVertex(-1, -1, -1)
		gl.glEnd()
if __name__=="__main__":
	app = QApplication([])
	
	glquad = OGLQUAD()
	glquad.resize(200, 200)
	glquad.show()
	
	app.exec()
	
