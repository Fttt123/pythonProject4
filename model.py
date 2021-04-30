import random
from view import Ui_MainWindow
import math
import skobki

class Model(Ui_MainWindow):
    result = ""
    _sqrt = ""
    _exp = ""
    delet = ""
    M_str = ''
    M = ''

    def add_digit(self, digit: str):
        self.result += digit
        self.plainTextEdit.setPlainText(self.result)

    def add_operator(self, operator: str):
        self.result += operator
        self.plainTextEdit.setPlainText(self.result)

    def plus(self):
        if self.result == '':
            self.result += '0+'
            self.plainTextEdit.setPlainText(str(self.result))
        else:
            self.result += '+'
            self.plainTextEdit.setPlainText(str(self.result))

    def minus(self):
        if self.result == '':
            self.result += '0-'
            self.plainTextEdit.setPlainText(str(self.result))
        else:
            self.result += '-'
            self.plainTextEdit.setPlainText(str(self.result))

    def share(self):
        try:
            if self.result == '':
                self.result += '0/'
                self.plainTextEdit.setPlainText(str(self.result))
            else:
                self.result += '/'
                self.plainTextEdit.setPlainText(str(self.result))
        except ZeroDivisionError:
                self.plainTextEdit.setPlainText(str('На 0 делить нельзя'))

    def multiply(self):
        if self.result == '':
            self.result += '0*'
            self.plainTextEdit.setPlainText(str(self.result))
        else:
            self.result += '*'
            self.plainTextEdit.setPlainText(str(self.result))


    def add_sqrt(self):
        self.result += 'math.sqrt('
        self.plainTextEdit.setPlainText(str(self.result))

    def delone(self):
        self.result += '1/'
        self.plainTextEdit.setPlainText(str(self.result))

    def abs(self):
        if self.result == '':
            self.plainTextEdit.setPlainText(str('Ничего не ввидено'))
        else:
            if self.result < 0:
                self.result = abs(self.result)
            elif self.result > 0:
                self.result = -abs(self.result)
            self.plainTextEdit.setPlainText(str(self.result))

    def M_op(self, operator: str):
        if operator == 'MS':
            self.M_str = str(eval(self.result))
        elif operator == 'MR' and self.M_str != '':
            self.result += self.M_str
            self.plainTextEdit.setPlainText(self.result)

        elif operator == 'MC':
            self.M_str = ''

        elif operator == 'M+' and self.M_str != '':
            self.M_str = str(int(self.result) + int(self.M_str))

        elif operator == 'M-' and self.M_str != '':
            self.M_str = str(int(self.result) - int(self.M_str))


    def modyl(self):
        self.result += 'abs('
        self.plainTextEdit.setPlainText(str(self.result))

    def e(self):
        self.result += '2.7182818284590452536'
        self.plainTextEdit.setPlainText(str(self.result))

    def add_exp(self):
        if self.result == '':
            self.result += '0'
            self.plainTextEdit.setPlainText(str(self.result))
        elif self.result == '0':
            self.result += ''
        else:
            self.result += '* 10**'
            self.plainTextEdit.setPlainText(str(self.result))

    def pow(self):
        if self.result == '':
            self.result += "0**"
            self.plainTextEdit.setPlainText(str(self.result))
        elif self.result == '0**':
            self.result += ''
        else:
            self.result += '**'
            self.plainTextEdit.setPlainText(self.result)

    def kv(self):
        if self.result == '':
            self.result += '0**2'
            self.plainTextEdit.setPlainText(str(self.result))
        else:
            self.result += '**2'
            self.plainTextEdit.setPlainText(str(self.result))

    def mod(self):
        if self.result == '':
            self.result += '0%'
            self.plainTextEdit.setPlainText(str(self.result))
        elif self.result == '0%':
            self.result += ''
        else:
            self.result += '%'
            self.plainTextEdit.setPlainText(str(self.result))

    def st(self):
        self.result += '10**'
        self.plainTextEdit.setPlainText(str(self.result))

    def pi(self):
        self.result += '3.141592653589793238'
        self.plainTextEdit.setPlainText(str(self.result))

    def delete(self):
        self.plainTextEdit.clear()
        self.result = ""
        self.plainTextEdit.setPlainText(self.result)

    def log(self):
        if self.result =='':
            self.result += 'math.log10('
            self.plainTextEdit.setPlainText(str(self.result))

    def ln(self):
        self.result += 'math.log('
        self.plainTextEdit.setPlainText(str(self.result))

    def fact(self):
        self.result += 'math.factorial('
        self.plainTextEdit.setPlainText(str(self.result))

    def och(self):
        self.delet = self.result
        self.result = ''
        for i in range(len(self.delet)):
            if i != len(self.delet) - 1:
                self.result += self.delet[i]
        self.plainTextEdit.setPlainText(self.result)

    def show_combo_text(self, operator: str):
        if operator == "sin":
            self.result += 'math.sin('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "cos":
            self.result += 'math.cos('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "tan":
            self.result += 'math.tan('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "sec":
            self.result += '1/math.cos('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "csc":
            self.result += '1/math.sin('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "cot":
            self.result = float(self.plainTextEdit.toPlainText())
            self.result = math.cos(self.result)/math.sin(self.result)
            self.plainTextEdit.setPlainText(str(self.result))

    def show_combo_text2(self, operator: str):
        if operator == "|x|":
            self.result += 'abs('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "floor()":
            self.result += 'math.floor('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "ciel()":
            self.result += 'math.ceil('
            self.plainTextEdit.setPlainText(str(self.result))
        if operator == "Rand":
            self.result = random.random()
            self.plainTextEdit.setPlainText(str(self.result))

    def get_result(self):
        if self.result == 'math.log10(0)':
            self.result += ''
            self.plainTextEdit.setPlainText(str('Неверный ввод'))
        elif self.result == 'math.log10(':
            self.result += ''
        elif self.result == 'math.log(0)':
            self.result += ''
            self.plainTextEdit.setPlainText(str('Неверный ввод'))
        elif self.result == 'math.log(':
            self.result += ''
        elif self.result == 'math.sqrt(':
            self.plainTextEdit.setPlainText(str('0'))
        elif self.result == 'math.factorial(':
            self.result += ''
        elif self.result == '0**':
            self.result += ''
        elif self.result == '10**':
            self.plainTextEdit.setPlainText(str('1'))
        elif self.result == '1/':
            self.result += ''
        elif self.result == '0%':
            self.result += ''
        else:
            try:
                self.plainTextEdit.setPlainText(str(eval(self.result)))
            except ZeroDivisionError:
                self.plainTextEdit.setPlainText(str('На 0 делить нельзя'))
            else:
                if self.result != '' and skobki.ic(self.result):
                    self.result = str(float(eval(self.result)))
                else:
                    self.result = ' '
                self.plainTextEdit.setPlainText(self.result)