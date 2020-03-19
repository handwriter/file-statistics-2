from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        min = 10 ** 100
        min_s = ''
        max = 0
        max_s = ''
        with open('input.txt', 'r', encoding='utf8') as text:
            a = ''.join(list(map(lambda x: x.rstrip(), text.readlines())))
            for i in a:
                if a.count(i) < min:
                    min = a.count(i)
                    min_s = i
                if a.count(i) > max:
                    max = a.count(i)
                    max_s = i
        self.label.setText(f'Частовстречающийся: {max_s}, {max}. Редковстречающийся: {min_s}, {min}')
        m = open('output.txt', 'w')
        m.write(f'Частовстречающийся: {max_s}, {max}. Редковстречающийся: {min_s}, {min}')
        m.close()


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())