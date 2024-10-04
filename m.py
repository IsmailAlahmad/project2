# import sys
# from PyQt5 import QtWidgets, QtCore
# from Datamanager import Datamanager
# from Lecturer import Lecturer
# from Grades import Grade
# from assignments import Assignment
# from Student import Student

# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("الواجهة الرئيسية")
#         self.setGeometry(100, 100, 400, 300)

#         layout = QtWidgets.QVBoxLayout()

#         # زر قائمة الطلاب
#         students_button = QtWidgets.QPushButton("قائمة الطلاب")
#         students_button.clicked.connect(self.open_student_list)
#         layout.addWidget(students_button)

#         # زر قائمة المحاضرين
#         lecturers_button = QtWidgets.QPushButton("قائمة المحاضرين")
#         lecturers_button.clicked.connect(self.open_lecturer_list)
#         layout.addWidget(lecturers_button)

#         self.setLayout(layout)

#     def open_student_list(self):
#         try:
#             self.student_list_window = StudentListWindow()
#             self.student_list_window.show()
#         except Exception as e:
#             print(f"Error opening student list: {e}")

#     def open_lecturer_list(self):
#         try:
#             self.lecturer_list_window = LecturerListWindow()
#             self.lecturer_list_window.show()
#         except Exception as e:
#             print(f"Error opening lecturer list: {e}")

# class LecturerListWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("قائمة المحاضرين")
#         self.setGeometry(100, 100, 600, 400)

#         layout = QtWidgets.QVBoxLayout()

#         # حقل البحث
#         self.search_box = QtWidgets.QLineEdit(self)
#         self.search_box.setPlaceholderText("البحث حسب الاسم أو البريد الإلكتروني")
#         layout.addWidget(self.search_box)

#         search_button = QtWidgets.QPushButton("بحث")
#         search_button.clicked.connect(self.search_lecturers)
#         layout.addWidget(search_button)

#         # قائمة المحاضرين
#         self.lecturer_list = QtWidgets.QListWidget(self)
#         layout.addWidget(self.lecturer_list)

#         # زر لإضافة وظيفة جديدة
#         add_assignment_button = QtWidgets.QPushButton("إضافة وظيفة")
#         add_assignment_button.clicked.connect(self.add_assignment)
#         layout.addWidget(add_assignment_button)

#         self.setLayout(layout)
#         self.populate_lecturer_list()  # لملء القائمة عند فتح الواجهة

#     def populate_lecturer_list(self):
#         try:
#             db_manager = Datamanager()
#             all_lecturers = Lecturer.get_all_lecturers(db_manager)  # استرجاع جميع المحاضرين
#             self.lecturer_list.clear()
#             for lecturer in all_lecturers:
#                 item_widget = QtWidgets.QWidget()
#                 item_layout = QtWidgets.QHBoxLayout()

#                 lecturer_label = QtWidgets.QLabel(f"{lecturer.first_name} {lecturer.last_name} - Email: {lecturer.email}")
#                 show_assignments_button = QtWidgets.QPushButton("عرض الوظائف")
#                 show_assignments_button.clicked.connect(lambda _, l=lecturer: self.open_assignments(l))

#                 item_layout.addWidget(lecturer_label)
#                 item_layout.addWidget(show_assignments_button)
#                 item_widget.setLayout(item_layout)

#                 list_item = QtWidgets.QListWidgetItem(self.lecturer_list)
#                 list_item.setSizeHint(item_widget.sizeHint())
#                 self.lecturer_list.addItem(list_item)
#                 self.lecturer_list.setItemWidget(list_item, item_widget)

#             db_manager.close()
#         except Exception as e:
#             print(f"Error populating lecturer list: {e}")

#     def search_lecturers(self):
#         try:
#             search_query = self.search_box.text()
#             db_manager = Datamanager()
#             lecturers = Lecturer.search_lecturers(db_manager, search_query)  # البحث عن المحاضرين
#             self.populate_lecturer_list_with_results(lecturers)
#             db_manager.close()
#         except Exception as e:
#             print(f"Error searching lecturers: {e}")

#     def populate_lecturer_list_with_results(self, lecturers):
#         try:
#             self.lecturer_list.clear()
#             for lecturer in lecturers:
#                 item_widget = QtWidgets.QWidget()
#                 item_layout = QtWidgets.QHBoxLayout()

#                 lecturer_label = QtWidgets.QLabel(f"{lecturer.first_name} {lecturer.last_name} - Email: {lecturer.email}")
#                 show_assignments_button = QtWidgets.QPushButton("عرض الوظائف")
#                 show_assignments_button.clicked.connect(lambda _, l=lecturer: self.open_assignments(l))

#                 item_layout.addWidget(lecturer_label)
#                 item_layout.addWidget(show_assignments_button)
#                 item_widget.setLayout(item_layout)

#                 list_item = QtWidgets.QListWidgetItem(self.lecturer_list)
#                 list_item.setSizeHint(item_widget.sizeHint())
#                 self.lecturer_list.addItem(list_item)
#                 self.lecturer_list.setItemWidget(list_item, item_widget)
#         except Exception as e:
#             print(f"Error populating lecturer list with results: {e}")

#     def add_assignment(self):
#         try:
#             # هنا يمكنك إضافة نافذة أو وظيفة لإضافة وظيفة جديدة
#             print("إضافة وظيفة جديدة")
#         except Exception as e:
#             print(f"Error adding assignment: {e}")

#     def open_assignments(self, lecturer):
#         try:
#             # فتح واجهة لعرض الوظائف الخاصة بالمحاضر المحدد
#             self.assignments_window = LecturerAssignmentsWindow(lecturer)
#             self.assignments_window.show()
#         except Exception as e:
#             print(f"Error opening assignments window: {e}")

# class LecturerAssignmentsWindow(QtWidgets.QWidget):
#     def __init__(self, lecturer):
#         super().__init__()
#         self.lecturer = lecturer
#         self.setWindowTitle(f"وظائف {lecturer.first_name} {lecturer.last_name}")
#         self.setGeometry(100, 100, 600, 400)

#         layout = QtWidgets.QVBoxLayout()

#         # قائمة الوظائف
#         self.assignment_list = QtWidgets.QListWidget(self)
#         layout.addWidget(self.assignment_list)

#         # زر لعرض الدرجات الخاصة بكل وظيفة
#         self.show_grades_button = QtWidgets.QPushButton("عرض الدرجات")
#         self.show_grades_button.clicked.connect(self.show_grades)
#         layout.addWidget(self.show_grades_button)

#         self.setLayout(layout)
#         self.populate_assignment_list()  # لملء القائمة عند فتح الواجهة

#     def populate_assignment_list(self):
#         try:
#             db_manager = Datamanager()
#             assignments = Assignment.get_assignments_for_lecturer(db_manager, self.lecturer.id)  # استرجاع الوظائف الخاصة بالمحاضر
#             self.assignment_list.clear()
#             for assignment in assignments:
#                 self.assignment_list.addItem(f"وظيفة: {assignment.title}")
#             db_manager.close()
#         except Exception as e:
#             print(f"Error populating assignment list: {e}")

#     def show_grades(self):
#         try:
#             selected_items = self.assignment_list.selectedItems()
#             if selected_items:
#                 for item in selected_items:
#                     assignment_title = item.text()
#                     # هنا يمكنك استخراج assignment_id من العنوان أو أي وسيلة مناسبة
#                     self.grades_window = AssignmentGradesWindow(assignment_title)
#                     self.grades_window.show()
#         except Exception as e:
#             print(f"Error showing grades: {e}")

# class AssignmentGradesWindow(QtWidgets.QWidget):
#     def __init__(self, assignment_title):
#         super().__init__()
#         self.setWindowTitle(f"درجات {assignment_title}")
#         self.setGeometry(100, 100, 600, 400)

#         layout = QtWidgets.QVBoxLayout()

#         # قائمة الدرجات
#         self.grades_list = QtWidgets.QListWidget(self)
#         layout.addWidget(self.grades_list)

#         # زر لتعديل الدرجة
#         self.edit_grade_button = QtWidgets.QPushButton("تعديل الدرجة")
#         self.edit_grade_button.clicked.connect(self.edit_grade)
#         layout.addWidget(self.edit_grade_button)

#         self.setLayout(layout)
#         self.populate_grades_list()  # لملء القائمة عند فتح الواجهة

#     def populate_grades_list(self):
#         try:
#             db_manager = Datamanager()
#             grades = Grade.get_grades_for_assignment(db_manager, self.assignment_title)  # استرجاع الدرجات الخاصة بالوظيفة
#             self.grades_list.clear()
#             for grade in grades:
#                 self.grades_list.addItem(f"الطالب: {grade.student_name} - الدرجة: {grade.score}")
#             db_manager.close()
#         except Exception as e:
#             print(f"Error populating grades list: {e}")

#     def edit_grade(self):
#         try:
#             selected_items = self.grades_list.selectedItems()
#             if selected_items:
#                 for item in selected_items:
#                     student_grade = item.text()
#                     # هنا يمكنك تعديل الدرجة
#                     print(f"تعديل الدرجة: {student_grade}")
#         except Exception as e:
#             print(f"Error editing grade: {e}")

# if __name__ == '__main__':
#     try:
#         app = QtWidgets.QApplication(sys.argv)
#         window = MainWindow()
#         window.show()
#         sys.exit(app.exec_())
#     except Exception as e:
#         print(f"Error in main application: {e}")
