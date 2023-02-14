from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
#Must also work on PySide2, PyQt5
import sys



class HiQHeader(QHeaderView):
    pass #To be implemented

class MyTable(QTableWidget):

    def __init__(self, col1_label, table_name=None, data_sep=False):
        super().__init__()
        self.table_name = table_name
        self.show()
    
    def add_data(self, xval, text_span, col_text, col_data):
        '''
        Add data set to the table widget.
        Text span should span the number of cols in col text.
        '''
        pass #To be implemented

    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    table = MyTable('Xval', 'My Table')

    d1 = {
        'label': 'Date 1',
        'xval': [10, 20, 30, 40, 50],
        'param1': [1, 2,3,4,5],
        'param2': [1.5,2.5,3.5,4.5, 5.5]
    }

    d2 = {
        'label': 'Date 2',
        'xval': [50, 60, 70, 80, 90],
        'param1': [1, 2,3,4,5],
        'param2': [1.5,2.5,3.5,4.5, 5.5],
        'param3': [15,25,35,45,55],
    }

    table.add_data(d1['xval'], d1['label'], ['param1', 'param2'], [d1['param1'], d1['param2']])
    table.add_data(d2['xval'], d2['label'], ['param1', 'param2', 'param3'], [d2['param1'], d2['param2'],d2['param3']])

    sys.exit(app.exec_())