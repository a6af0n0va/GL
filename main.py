from PyQt5.QtWidgets import QApplication, QOpenGLWidget
from PyQt5.QtGui import QOpenGLContext
import OpenGL.GL as gl
class OGLQUAD(QOpenGLWidget):
	def __init__(self):
		super().__init__()
		
	def initializeGL(self):
		print("init")
		#pfunc = QOpenGLContext.currentContext().functions()
		gl.glClearColor(0,0,0,1)
	def resizeGL(self, width, height):
		print("resiz")
		gl.glMatrixMode(GL_PROJECTION)
		gl.glLoadIdentity()
		gl.glViewport(0,0, width, height)
		gl.glOrtho(0,100,100,0,-1,1)
	def paintGL(self):
		print("paint")
		gl.glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		gl.glBegin(GL_QUADS)
		gl.glColor3f(1,0,0)
		gl.glVertex2f(0,100)
		gl.glColor3f(0,1,0)
		gl.glVertex2f(100,100)		
		gl.glColor3f(0,0,1)
		gl.glVertex2f(100,0)		
		gl.glColor3f(1,1,1)
		gl.glVertex2f(0,0)
		gl.glEnd()
if __name__=="__main__":
	app = QApplication([])
	
	glquad = OGLQUAD()
	glquad.resize(200, 200)
	glquad.show()
	
	app.exec()
	
