from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMenuBar, QAction, QStatusBar, QMessageBox, QInputDialog, QMainWindow
from src.bot import Query, Reply

class MyHealthCareBot(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.query = Query()
	
	def initUI(self):
		self.setWindowTitle('AI-Powered HealthCare Chatbot')
		self.setGeometry(100, 100, 600, 400)
		
		# Create widgets
		self.label = QLabel('Enter patient description:')
		self.submit_button = QPushButton('Submit')
		self.output_label = QLabel()
		self.output_label.setWordWrap(True)
		self.input_text = QLineEdit()
		
		# Create menu bar
		menu_bar = self.menuBar()
		options_menu = menu_bar.addMenu('Options')

		# Create actions for menu bar
		set_age_action = QAction('Set Age', self)
		set_age_action.triggered.connect(self.show_set_age_dialog)
		options_menu.addAction(set_age_action)

		set_gender_action = QAction('Set Gender', self)
		set_gender_action.triggered.connect(self.show_set_gender_dialog)
		options_menu.addAction(set_gender_action)
		# Create status bar
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

		# Create layout
		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.input_text)
		layout.addWidget(self.submit_button)
		layout.addWidget(self.output_label)

		# Create central widget
		central_widget = QWidget()
		central_widget.setLayout(layout)
		# Set central widget
		self.setCentralWidget(central_widget)

		# Set layout for the window
		self.setLayout(layout)
		
		# Connect button click event to slot
		self.submit_button.clicked.connect(self.process_input)

	def show_set_age_dialog(self):
		age, ok = QInputDialog.getInt(self, 'Set Age', 'Enter age:', 0, 0, 150)
		if ok:
			self.query.set_param("age", str(age))
			self.status_bar.showMessage('Age set to: {}'.format(age))

	def show_set_gender_dialog(self):
		gender, ok = QInputDialog.getText(self, 'Set Gender', 'Enter gender (e.g. male, female):')
		if ok:
			self.query.set_param("gender", gender)
			self.status_bar.showMessage('Gender set to: {}'.format(gender))

	def process_input(self):
		# Get user input from the input_text QLineEdit
		user_input = self.input_text.text()

		# update query message
		self.query.set_message(user_input)

		# chatbot's logic goes here
		bot_output = Reply(self.query.create_message()).send(True)

		# Update the output_label QLabel with the bot's output
		self.output_label.setText(bot_output)
