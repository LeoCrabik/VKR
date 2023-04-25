from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow
import sys
from UI.open_excel import Ui_Form
from UI.global_info import Ui_Global_info
from UI.examUnitWindow import Ui_examUnitWindow
from UI.examUnitWidget import Ui_examUnitWidget
from UI.blockWidget import Ui_blockWidget
from excel.main import ExcelReader
from word.main import FillTemplate
from collections import Counter


class Window1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.choose_file)
        self.setWindowTitle('Выбор файла')
        self.excel = self.label.text()

    def choose_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выберите файл...', '', 'Excel file (*.xlsx)')
        self.label.setText(file_name[0])
        self.excel = file_name[0]


class ExamUnitWidget(QWidget, Ui_examUnitWidget):
    def __init__(self, subject_name):
        super().__init__()
        self.setupUi(self)
        self.examName.setText(subject_name)


class BlockWidget(QWidget, Ui_blockWidget):
    def __init__(self, block_name):
        super().__init__()
        self.setupUi(self)
        self.blockName.setText(block_name)


class Window2(QWidget, Ui_examUnitWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Зачетные единицы')
        self.examWidgets = []
        self.blockWidgets = []

    def get_exam_units(self):
        exam_dict = {}
        for exam in self.examWidgets:
            exam_dict[exam.examName.text()] = exam.examUnit.toPlainText()

        return exam_dict


class Window3(QWidget, Ui_Global_info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Общая информация')

    def get_global_data(self):

        global_data = {
            'vice_rector': self.viceRectorInfo.toPlainText(),
            'group': self.groupInfo.toPlainText(),
            'direction': self.directionInfo.toPlainText(),
            'qualification': self.qualificationInfo.currentText(),
            'code': self.codeInfo.toPlainText(),
            'form': self.formInfo.currentText(),
            'orientation': self.orientationInfo.toPlainText(),
            'year': self.YearInfo.toPlainText(),
        }

        studing_years_dict = {
            'Бакалавриат': '4 года',
            'Специалитет': '5 лет',
            'Магистратура': '2 года'}

        if 'заочная' in global_data['form']:
            studing_years_dict['Аспирантура'] = '4 года'
        else:
            studing_years_dict['Аспирантура'] = '3 года'

        global_data['studing_years'] = studing_years_dict[global_data['qualification']]

        return global_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.subject_list = None
        self.w1 = Window1()
        self.w2 = Window2()
        self.w3 = Window3()
        self.w1.nextButton.clicked.connect(self.w1.hide)
        self.w1.nextButton.clicked.connect(self.read_excel)
        self.w1.nextButton.clicked.connect(self.w2.show)
        self.w2.nextButton.clicked.connect(self.w2.get_exam_units)
        self.w2.nextButton.clicked.connect(self.w2.hide)
        self.w2.nextButton.clicked.connect(self.w3.show)
        self.w3.nextButton.clicked.connect(self.fill_data)
        self.w3.nextButton.clicked.connect(self.w3.close)
        self.student_dict = None
        self.excel = None
        self.excel_reader = None
        self.subject_list = None
        self.subject_dict = None

    def read_excel(self):
        self.excel = self.w1.excel
        self.excel_reader = ExcelReader(self.excel)
        self.student_dict = self.excel_reader.reader()
        self.subject_list = self.excel_reader.subject_list
        self.subject_dict = self.excel_reader.subject_dict
        self.set_subjects()

    def set_subjects(self):
        # for subject in self.subject_list:
        #     self.w2.examWidgets.append(ExamUnitWidget(subject))
        #     self.w2.verticalLayout.addWidget(self.w2.examWidgets[-1])

        for item in self.subject_dict.items():
            self.w2.blockWidgets.append(BlockWidget(item[0]))
            self.w2.verticalLayout.addWidget(self.w2.blockWidgets[-1])
            for i, subject in enumerate(item[1]):
                widget = ExamUnitWidget(subject)
                widget.examUnit.setPlainText(str(i))
                self.w2.examWidgets.append(widget)
                self.w2.verticalLayout.addWidget(self.w2.examWidgets[-1])

    def fill_data(self):
        exam_units_dict = self.w2.get_exam_units()
        block_exam_units_dict = self.get_block_exam_units(exam_units_dict)
        for k, v in block_exam_units_dict.items():
            exam_units_dict[k] = v

        filler = FillTemplate(
            template_path='word/template',
            student_dict=self.student_dict,
            global_data=self.w3.get_global_data(),
            exam_units=exam_units_dict

        )
        filler.fill_words()

    def get_block_exam_units(self, exam_units_dict):
        block_exam_units_dict = {}
        print(self.subject_dict.items())
        for item in self.subject_dict.items():
            block_exam_units_dict[item[0]] = str(sum([int(exam_units_dict[unit]) for unit in item[1]]))
        print(block_exam_units_dict)

        return block_exam_units_dict

    def fill_exams(self):
        self.w2.get_exam_units()


app = QApplication(sys.argv)

window = MainWindow()
window.w1.show()

app.exec()
print(1)
