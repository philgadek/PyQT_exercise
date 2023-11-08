from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QPushButton, QFileDialog
from PyQt6.QtWidgets import QLabel, QGridLayout, QLineEdit, QPlainTextEdit
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction, QPixmap, QIntValidator


class Window(QMainWindow):
    #Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('AC, FG, MP')
        
        self.createMenu()
        self.createTabs()
          
    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)
        
        # Task 1
        self.fileMenu = self.menu.addMenu("Task1")
        # Przycisk otwierający zdjęcie
        self.actionOpen1 = QAction('Open', self)
        self.actionOpen1.setShortcut('Ctrl+O')
        self.actionOpen1.triggered.connect(self.openPNG)
        self.fileMenu.addAction(self.actionOpen1)
        
        # Task 2
        self.fileMenu = self.menu.addMenu("Task2")
        # Clear
        self.actionClear2 = QAction('Clear', self)
        self.actionClear2.setShortcut('Ctrl+R')
        self.actionClear2.triggered.connect(self.note_clear)
        self.fileMenu.addAction(self.actionClear2)
        # Open
        self.actionOpen2 = QAction('Open', self)
        self.actionOpen2.setShortcut('Ctrl+O')
        self.actionOpen2.triggered.connect(self.note_open)
        self.fileMenu.addAction(self.actionOpen2)
        # Save
        self.actionSave2 = QAction('Save', self)
        self.actionSave2.setShortcut('Ctrl+S')
        self.actionSave2.triggered.connect(self.note_save)
        self.fileMenu.addAction(self.actionSave2)
        # Save as
        self.actionSaveas2 = QAction('Save as', self)
        self.actionSaveas2.setShortcut('Ctrl+D')
        self.actionSaveas2.triggered.connect(self.note_saveas)
        self.fileMenu.addAction(self.actionSaveas2)
        
        # Task 3
        self.fileMenu = self.menu.addMenu("Task3")
        # Clear fields
        self.actionClear3 = QAction('Clear', self)
        self.actionClear3.setShortcut('Ctrl+R')
        self.actionClear3.triggered.connect(self.fields_clear)
        self.fileMenu.addAction(self.actionClear3)

    
    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()
        
        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        
        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Task 1")
        self.tabs.addTab(self.tab_2, "Task 2")        
        self.tabs.addTab(self.tab_3, "Task 3")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)
        
        # Tab 1
        self.tab_1.image = QLabel(self.tab_1)
        self.refresh1()
        
        # Tab 2
        self.tab_2.notepad = QPlainTextEdit(self.tab_2)
        self.refresh2()
        
        # Tab 3
        self.tab_3.lineEditA = QLineEdit(self.tab_3)
        self.tab_3.lineEditA.move(25, 10)
        self.tab_3.lineEditA.setPlaceholderText("Enter any character")
        self.tab_3.lineEditA.textChanged.connect(self.text_update)

        self.tab_3.lineEditB = QLineEdit(self.tab_3)
        self.tab_3.lineEditB.move(25, 60)
        self.tab_3.lineEditB.setPlaceholderText("Enter any character")
        self.tab_3.lineEditB.textChanged.connect(self.text_update)

        self.tab_3.lineEditC = QLineEdit(self.tab_3)
        self.tab_3.lineEditC.move(25, 110)
        self.tab_3.lineEditC.setPlaceholderText("Enter numeric character")
        self.tab_3.lineEditC.setValidator(QIntValidator(1,2147483647,self))
        self.tab_3.lineEditC.textChanged.connect(self.text_update)

        self.tab_3.lineEditABC = QPlainTextEdit(self.tab_3)
        self.tab_3.lineEditABC.move(25, 160)
        self.tab_3.lineEditABC.setPlaceholderText("Value of A + B + C")
        self.tab_3.lineEditABC.setReadOnly(True)
        
        self.refresh3()
        self.setCentralWidget(self.tabs)


    # Refreshing
    def refresh1(self):
        self.tab_1.image.resize(self.size())
        
    def refresh2(self):
        self.tab_2.notepad.resize(self.width() - 50, self.height() - 100)
        
    def refresh3(self):
        self.tab_3.lineEditA.setFixedWidth(self.width() - 50)
        self.tab_3.lineEditB.setFixedWidth(self.width() - 50)
        self.tab_3.lineEditC.setFixedWidth(self.width() - 50)
        self.tab_3.lineEditABC.setFixedWidth(self.width() - 50)  
        
          
    # Task 1    
    def openPNG(self):
        fileName, _ = QFileDialog.getOpenFileName(self.tab_1, "Wybierz plik obrazu",  "Początkowa nazwa pliku", "PNG (*.png)")
        
        if fileName:
            pixmap = QPixmap(fileName)
            self.tab_1.image.resize(self.size())
            self.tab_1.image.setPixmap(pixmap.scaled(pixmap.width(),pixmap.height()))

    # Task 2
    def note_clear(self):
        self.tabs.setCurrentIndex(1)
        self.tab_2.notepad.clear()
        
    def note_open(self):
        self.tabs.setCurrentIndex(1) 
        fileName2, _ = QFileDialog.getOpenFileName(self.tab_2, "Wybierz plik tekstowy", "", "TXT (*.txt)")
        title = fileName2 + ".txt"
        if title:
            with open(title, 'r') as f: 
                print(title)
                self.tab_2.notepad.resize(self.size())
                self.note_clear()
                self.tab_2.notepad.insertPlainText(title)
            
    def note_save(self):
        self.tabs.setCurrentIndex(1)
        text_to_save = self.tab_2.notepad.toPlainText()
        title = text_to_save + ".txt"
        if title:
            with open(title, 'w') as f:
                f.write(text_to_save)
        else:
            self.note_saveas()
   
    def note_saveas(self):
        self.tabs.setCurrentIndex(1) 
        fileName, _ = QFileDialog.getSaveFileName(self.tab_2, "Wybierz plik tekstowy",  "", "TXT (*.txt)")
        text_to_read2 = self.tab_2.notepad.toPlainText()
        if fileName:
            with open(fileName, 'r') as f: 
                self.tab_2.notepad.resize(self.size())
                self.note_clear()
                self.tab_2.notepad.insertPlainText(text_to_read2)   
    
    # Task 3    
    def text_update(self):
        sum = ""
        sum = self.tab_3.lineEditA.text() + " " + self.tab_3.lineEditB.text() + " " + self.tab_3.lineEditC.text()
        self.tab_3.lineEditABC.clear()
        self.tab_3.lineEditABC.insertPlainText(sum)

    
    def fields_clear(self):
        self.tabs.setCurrentIndex(2)
        self.tab_3.lineEditA.clear()
        self.tab_3.lineEditB.clear()
        self.tab_3.lineEditC.clear()
        
    


# Uruchomienie okna
# if __name__ == '__Apppp__':
app = QApplication([])
win = Window()
win.setGeometry(100,100,640,480)
win.show()
app.exec()