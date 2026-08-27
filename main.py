from PySide6.QtWidgets import QApplication
import sys
from Dashboard import Dashboard



app = QApplication(sys.argv)

main_window = Dashboard()

#if you want to make style for your app by QSS
#I'm gonna add this part later
#with open("style.qss", "r", encoding="utf-8") as f:
#    app.setStyleSheet(f.read())

main_window.show()
app.exec()