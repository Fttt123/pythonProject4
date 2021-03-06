from model import Model

class Controller(Model):
    def controller(self):
        self.pushButton.clicked.connect(lambda: self.add_digit(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.add_digit(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.add_digit(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.add_digit(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.add_digit(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.add_digit(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.add_digit(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.add_digit(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.add_digit(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(self.abs)
        self.pushButton_11.clicked.connect(lambda: self.add_digit(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(self.multiply)
        self.pushButton_13.clicked.connect(self.minus)
        self.pushButton_14.clicked.connect(self.plus)
        self.pushButton_15.clicked.connect(self.get_result)
        self.pushButton_16.clicked.connect(lambda: self.add_digit(self.pushButton_16.text()))
        self.pushButton_17.clicked.connect(self.mod)
        self.pushButton_18.clicked.connect(self.och)
        self.pushButton_19.clicked.connect(lambda: self.M_op(self.pushButton_19.text()))
        self.pushButton_20.clicked.connect(self.ln)
        self.pushButton_21.clicked.connect(self.log)
        self.pushButton_22.clicked.connect(self.st)
        self.pushButton_23.clicked.connect(self.pow)
        self.pushButton_24.clicked.connect(self.add_sqrt)
        self.pushButton_25.clicked.connect(lambda: self.add_digit(self.pushButton_25.text()))
        self.pushButton_26.clicked.connect(lambda: self.add_digit(self.pushButton_26.text()))
        self.pushButton_27.clicked.connect(self.fact)
        self.pushButton_28.clicked.connect(self.delete)
        self.pushButton_29.clicked.connect(self.share)
        self.pushButton_30.clicked.connect(self.add_exp)
        self.pushButton_31.clicked.connect(self.modyl)
        self.pushButton_32.clicked.connect(self.delone)
        self.pushButton_33.clicked.connect(self.kv)
        self.pushButton_35.clicked.connect(self.pi)
        self.pushButton_36.clicked.connect(self.e)
        self.pushButton_37.clicked.connect(lambda: self.M_op(self.pushButton_37.text()))
        self.pushButton_38.clicked.connect(lambda: self.M_op(self.pushButton_38.text()))
        self.pushButton_39.clicked.connect(lambda: self.M_op(self.pushButton_39.text()))
        self.pushButton_40.clicked.connect(lambda: self.M_op(self.pushButton_40.text()))
        self.comboBox.activated.connect(lambda: self.show_combo_text(self.comboBox.currentText()))
        self.comboBox_2.activated.connect(lambda: self.show_combo_text2(self.comboBox_2.currentText()))