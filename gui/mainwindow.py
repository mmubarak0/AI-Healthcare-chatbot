from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyHealthCareBot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI-Powered HealthCare Chatbot')
        self.setGeometry(100, 100, 400, 200)

        # Create widgets
        self.label = QLabel('Enter patient description:')
        self.input_text = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.output_label = QLabel()

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.output_label)

        # Set layout for the window
        self.setLayout(layout)

        # Connect button click event to slot
        self.submit_button.clicked.connect(self.process_input)

    def process_input(self):
        # Get user input from the input_text QLineEdit
        user_input = self.input_text.text()

        # chatbot's logic goes here
        bot_output = f"Bot Output: {user_input}"

        # Update the output_label QLabel with the bot's output
        self.output_label.setText(bot_output)
