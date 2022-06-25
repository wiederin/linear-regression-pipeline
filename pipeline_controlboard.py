import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Every PyQt6 application must create an application object.
# The application object is located in the QtWidgets module.
app = QApplication([])

# The QWidget widget is the base class of all user interface objects in PyQt6.
# We provide the default constructor for QWidget. The default constructor has no parent.
# A widget with no parent is called a window.
root = QWidget()

root.resize(320, 240)  # The resize() method resizes the widget.
root.setWindowTitle("pipeline controlboard")  # Here we set the title for our window.
root.show()  # The show() method displays the widget on the screen.

sys.exit(app.exec())  # Finally, we enter the mainloop of the application.