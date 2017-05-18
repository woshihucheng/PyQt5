# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中单元格内的文本颜色
   
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
from PyQt5.QtGui import QBrush,  QColor ,  QFont 

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(400,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
          
        newItem = QTableWidgetItem("张三")  
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)  
                 
        newItem = QTableWidgetItem("男")  
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem("160") 
        newItem.setForeground(QBrush(QColor(255, 0, 0))) 
        tableWidget.setItem(0, 2, newItem)     
        
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
