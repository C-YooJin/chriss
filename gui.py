import sys
import script
import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

connection = mysql.connector.connect(host='192.168.0.101',
                                         database='covid',
                                         user='root',
                                         password='Covid19!',
                                         auth_plugin='mysql_native_password')
# 리얼
class MyApp(QWidget):
    # 생성자
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 생성
    def initUI(self):
        # input StartDate
        self.lb1 = QLabel(self)
        self.lb1.move(10,40)
        self.lb1.setText("시작날짜(yyyyMMdd)")
        self.et1 = QLineEdit(self)
        self.et1.move(150,40)

        # input EndDate
        self.lb2 = QLabel(self)
        self.lb2.move(10, 80)
        self.lb2.setText("종료날짜(yyyyMMdd)")
        self.et2 = QLineEdit(self)
        self.et2.move(150, 80)

        # button
        self.btn = QPushButton(self)
        self.btn.setText("엑셀 받기")
        self.btn.move(150,150)
        # 이벰트 연결
        self.btn.clicked.connect(self.btn_clicked)

        # window
        self.setWindowTitle("Covid DB to Excel")
        self.setGeometry(300,300,300,200)
        self.show()

    # 이벤트 실행
    def btn_clicked(self):
        # 엑셀 내보내기 스크립트
        script.Excel_Out(connection, self.et1.text(), self.et2.text())




# Main 시작
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 클래스 객체화₩
    ex = MyApp()

    #x 버튼 누르면 끄지3
    sys.exit(app.exec_())