from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class AddTeacherDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("إضافة معلم")
        self.setGeometry(200, 200, 300, 200)

        self.name_label = QLabel("الاسم:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("البريد الإلكتروني:")
        self.email_input = QLineEdit()

        self.add_button = QPushButton("إضافة")
        self.add_button.clicked.connect(self.add_teacher)

        self.cancel_button = QPushButton("إلغاء")
        self.cancel_button.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        # تصميم الأزرار
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)

    def add_teacher(self):
        name = self.name_input.text()
        email = self.email_input.text()
        if name and email:  # تحقق من عدم كون الحقول فارغة
            self.parent().add_teacher_row(name, email)  # إضافة المعلم إلى الجدول
            self.accept()
