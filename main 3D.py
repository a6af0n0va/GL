from PyQt5.QtWidgets import QApplication, QOpenGLWidget
from PyQt5.QtGui import QOpenGLContext
import OpenGL.GL as gl
class OGLQUAD(QOpenGLWidget):
	def __init__(self):
		super().__init__()
		
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
		print("paint")
		gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
		gl.glMatrixMode(gl.GL_MODELVIEW)
		gl.glLoadIdentity()
		
		gl.glTranslate(0.0, 0.0, -3.0)
		gl.glRotate(45, 1.0, 0.0, 0.0)
		gl.glRotate(45, 0.0, 1.0, 0.0)
		gl.glRotate(10, 1.0, 0.0, 0.0)
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
	
