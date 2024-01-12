import sys
import pickle
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, \
    QDoubleSpinBox, QComboBox


def load_model(file_path):
    with open(file_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(0, 0, 831, 509)
        self.setWindowTitle("MainWindow")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.exit_btn = QPushButton("EXIT", central_widget)
        self.exit_btn.setGeometry(630, 410, 191, 51)

        self.title_labl = QLabel("ENGINEERING MANAGEMENT PROJECT", central_widget)
        self.title_labl.setGeometry(160, 0, 501, 51)
        font = self.title_labl.font()
        font.setPointSize(22)
        self.title_labl.setFont(font)

        self.horizontalLayoutWidget = QWidget(central_widget)
        self.horizontalLayoutWidget.setGeometry(20, 301, 651, 41)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)

        self.model1 = QRadioButton("Linear Regression", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model1)

        self.model2 = QRadioButton("Random Forest", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model2)

        self.model3 = QRadioButton("Support Vector", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model3)

        self.model4 = QRadioButton("Decision Tree", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model4)

        self.model5 = QRadioButton("Gradient Boosting", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model5)

        self.model6 = QRadioButton("Lasso Regression", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model6)

        self.selectmodel_labl = QLabel("Select Model", central_widget)
        self.selectmodel_labl.setGeometry(20, 274, 131, 20)
        font = self.selectmodel_labl.font()
        font.setPointSize(12)
        self.selectmodel_labl.setFont(font)

        self.user_details_labl = QLabel("User Details", central_widget)
        self.user_details_labl.setGeometry(20, 50, 131, 20)
        font = self.user_details_labl.font()
        font.setPointSize(12)
        self.user_details_labl.setFont(font)

        self.prediction_labl = QLabel("Prediction", central_widget)
        self.prediction_labl.setGeometry(20, 370, 131, 20)
        font = self.prediction_labl.font()
        font.setPointSize(12)
        self.prediction_labl.setFont(font)

        self.pred_accuracy_labl = QLabel("Accuracy", central_widget)
        self.pred_accuracy_labl.setGeometry(20, 399, 81, 21)

        self.pred_sgpa_labl = QLabel("SGPA of 5th Semester", central_widget)
        self.pred_sgpa_labl.setGeometry(220, 400, 131, 20)

        self.pred_cgpa_labl = QLabel("CGPA of 5th Semester", central_widget)
        self.pred_cgpa_labl.setGeometry(420, 400, 131, 20)

        self.pred_sgpa = QLabel("IDK", central_widget)
        self.pred_sgpa.setGeometry(220, 420, 61, 21)

        self.pred_cgpa = QLabel("IDK", central_widget)
        self.pred_cgpa.setGeometry(420, 420, 61, 21)

        self.pred_accuracy = QLabel("IDK", central_widget)
        self.pred_accuracy.setGeometry(20, 420, 61, 21)

        self.predict_btn = QPushButton("PREDICT", central_widget)
        self.predict_btn.setGeometry(680, 300, 141, 41)
        self.predict_btn.clicked.connect(self.predict)

        self.widget = QWidget(central_widget)
        self.widget.setGeometry(20, 80, 791, 181)
        font = self.widget.font()
        font.setPointSize(10)
        self.widget.setFont(font)

        self.label = QLabel("Gender", self.widget)
        self.label.setGeometry(50, 20, 101, 21)

        self.label_2 = QLabel("Availing any Scholarship?", self.widget)
        self.label_2.setGeometry(50, 60, 181, 21)

        self.label_3 = QLabel("Matric Percentage", self.widget)
        self.label_3.setGeometry(50, 100, 181, 21)

        self.label_4 = QLabel("Intermediate Percentage", self.widget)
        self.label_4.setGeometry(50, 140, 181, 21)

        self.label_5 = QLabel("SGPA in first semester", self.widget)
        self.label_5.setGeometry(470, 20, 181, 21)

        self.label_6 = QLabel("SGPA in second semester", self.widget)
        self.label_6.setGeometry(470, 60, 181, 21)

        self.label_7 = QLabel("SGPA in third semester", self.widget)
        self.label_7.setGeometry(470, 100, 181, 21)

        self.label_8 = QLabel("SGPA in fourth semester", self.widget)
        self.label_8.setGeometry(470, 140, 181, 21)

        self.sel_matric = QDoubleSpinBox(self.widget)
        self.sel_matric.setGeometry(240, 100, 71, 22)
        self.sel_matric.setMaximum(100.0)
        self.sel_matric.setSingleStep(1.0)
        self.sel_matric.setValue(0.0)

        self.sel_inter = QDoubleSpinBox(self.widget)
        self.sel_inter.setGeometry(240, 140, 71, 22)
        self.sel_inter.setMaximum(100.0)

        self.sel_gpa1 = QDoubleSpinBox(self.widget)
        self.sel_gpa1.setGeometry(660, 20, 71, 22)
        self.sel_gpa1.setMaximum(4.0)
        self.sel_gpa1.setSingleStep(0.2)
        self.sel_gpa1.setValue(1.0)

        self.sel_gpa2 = QDoubleSpinBox(self.widget)
        self.sel_gpa2.setGeometry(660, 60, 71, 22)
        self.sel_gpa2.setMaximum(4.0)
        self.sel_gpa2.setSingleStep(0.2)
        self.sel_gpa2.setValue(1.0)

        self.sel_gpa3 = QDoubleSpinBox(self.widget)
        self.sel_gpa3.setGeometry(660, 100, 71, 22)
        self.sel_gpa3.setMaximum(4.0)
        self.sel_gpa3.setSingleStep(0.2)
        self.sel_gpa3.setValue(1.0)

        self.sel_gpa4 = QDoubleSpinBox(self.widget)
        self.sel_gpa4.setGeometry(660, 140, 71, 22)
        self.sel_gpa4.setMaximum(4.0)
        self.sel_gpa4.setSingleStep(0.2)
        self.sel_gpa4.setValue(1.0)

        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(240, 60, 151, 22)

        self.sel_scholarship = QHBoxLayout(self.horizontalLayoutWidget_2)

        self.yes_btn = QRadioButton("YES", self.horizontalLayoutWidget_2)
        self.sel_scholarship.addWidget(self.yes_btn)

        self.no_btn = QRadioButton("NO", self.horizontalLayoutWidget_2)
        self.sel_scholarship.addWidget(self.no_btn)

        self.horizontalLayoutWidget_3 = QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(240, 20, 151, 22)

        self.sel_scholarship_2 = QHBoxLayout(self.horizontalLayoutWidget_3)

        self.yes_btn_2 = QRadioButton("MALE", self.horizontalLayoutWidget_3)
        self.sel_scholarship_2.addWidget(self.yes_btn_2)

        self.no_btn_2 = QRadioButton("FEMALE", self.horizontalLayoutWidget_3)
        self.sel_scholarship_2.addWidget(self.no_btn_2)

        self.interest_label = QLabel("Interest in Program", self.widget)
        self.interest_label.setGeometry(470, 180, 181, 21)

        self.interest_combobox = QComboBox(self.widget)
        self.interest_combobox.setGeometry(660, 180, 71, 22)
        self.interest_combobox.addItems(["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])

    def predict(self):
        selected_model = None
        if self.model1.isChecked():
            selected_model = load_model('linear_regression_model.pkl')
        elif self.model2.isChecked():
            selected_model = load_model('random_forest_model.pkl')
        elif self.model3.isChecked():
            if self.model3_sgpa.isChecked():
                selected_model = load_model('support_vector_model_sgpa.pkl')
            elif self.model3_cgpa.isChecked():
                selected_model = load_model('support_vector_model_cgpa.pkl')
        elif self.model4.isChecked():
            selected_model = load_model('decision_tree_model.pkl')
        elif self.model5.isChecked():
            if self.model5_sgpa.isChecked():
                selected_model = load_model('gradient_boosting_model_sgpa.pkl')
            elif self.model5_cgpa.isChecked():
                selected_model = load_model('gradient_boosting_model_cgpa.pkl')
        elif self.model6.isChecked():
            selected_model = load_model('lasso_regression_model.pkl')

        if selected_model is not None:
            input_values = [
                int(self.no_btn_2.isChecked()),  # Gender
                int(self.yes_btn.isChecked()),  # Availing any scholarship
                self.sel_matric.value(),
                self.sel_inter.value(),
                self.sel_gpa1.value(),
                self.sel_gpa2.value(),
                self.sel_gpa3.value(),
                self.sel_gpa4.value(),
                self.interest_combobox.currentIndex()  # Selected index of the interest level
            ]

            mapping = {
                "Strongly Disagree": 0,
                "Disagree": 1,
                "Neutral": 2,
                "Agree": 3,
                "Strongly Agree": 4
            }

            # Map the interest level index to the desired values
            interest_level = [
                "Strongly Disagree",
                "Disagree",
                "Neutral",
                "Agree",
                "Strongly Agree"
            ][input_values[-1]]

            input_values[-1] = mapping[interest_level]

            input_df = pd.DataFrame([input_values], columns=[
                'Gender', 'Availing any scholarship', 'Matric percentage',
                'Intermediate percentage', 'SGPA in BS First semester',
                'SGPA in BS Second semester', 'SGPA in BS Third semester',
                'SGPA in BS Fourth semester', 'Interest Level'
            ])

            predictions = selected_model.predict(input_df)

            pred_sgpa_value = predictions[0]
            pred_cgpa_value = predictions[1]

            self.pred_sgpa.setText(f'{pred_sgpa_value:.2f}')
            self.pred_cgpa.setText(f'{pred_cgpa_value:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
