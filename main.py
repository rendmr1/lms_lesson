import sys
import sqlite3


from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow, QPushButton
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap, QIcon


class WorkWindow(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("main.ui", self)

        self.init_table()

    def init_table(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Степень обжарки",
                                                                      "Молотый/в зёрнах", "Описание", "Цена", "Объём"])

        with sqlite3.connect("coffee.sqlite") as con:
            # Создание курсора
            cur = con.cursor()

            data = cur.execute("""
            SELECT * FROM info
            """).fetchall()
        self.tableWidget.setRowCount(len(data))

        for index, item in enumerate(data):
            self.add_coffe_to_table(index, item)

    def add_coffe_to_table(self, row, item):
        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(item[2]))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(item[3]))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(item[4]))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(str(item[5])))
        self.tableWidget.setItem(row, 6, QTableWidgetItem(str(item[6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWindow()
    ex.show()

    sys.exit(app.exec())
