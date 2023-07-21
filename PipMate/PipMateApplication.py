import sys
from PyQt6.QtWidgets import QApplication, QMainWindow ,QToolTip
from PipMate import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.btn_calculate)
        
        self.ui.comboBox.currentTextChanged.connect(self.combo_changed)
        
    def combo_changed(self, currentText):
        if currentText == "EURUSD":
            print("Fiber")
        elif currentText == "GBPUSD":
            print("Cable")
        elif currentText == "USDCHF":
            print("Swissie") 
    
    def input_account_balance(self):
        acc_balance = self.ui.AccountBalance.text()
        print("Acc balance: ", acc_balance)
        return acc_balance
    
    # Calculate the amount at risk
    def amount_at_risk(self):
        self.ui.AmountAtRisk.clear()
        account_balance = int(self.input_account_balance())
        risk_percentage = float(self.ui.RiskPercentage.text()) * 0.01
        risk = str(account_balance * risk_percentage)
        self.ui.AmountAtRisk.insert(f"${risk}")
        return risk
    
    # Filles the result field
    def results_field(self):
        amount_at_risk_ = float(self.amount_at_risk())
        stop_loss = float(self.ui.StopLoss.text())
        standard_size = amount_at_risk_ / 0.0001 / stop_loss
        
        standard_size = int(standard_size)
        units_size = str(standard_size)
        
        self.ui.PositionSize.clear()
        self.ui.PositionSize.insert(units_size)
        
        standard_lots_size = standard_size / 100000
        standard_lots_size = str(standard_lots_size)
        
        self.ui.StandardLots.clear()
        self.ui.StandardLots.insert(standard_lots_size)
    
    def btn_calculate(self):
        if self.ui.AccountBalance.text() == "":
            print("error: empty Account Balance")
        if self.ui.StopLoss.text() == "" :
            print("error: empty Stop Loss")
        if self.ui.RiskPercentage.text() == "":
            print("error: empty Risk Percentage")
        else:
            self.results_field()
            
app = QApplication(sys.argv)
window = Main()
window.show()
app.exec()
