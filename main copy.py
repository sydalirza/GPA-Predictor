import sys
import pickle
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, \
    QDoubleSpinBox, QComboBox


def load_model(file_path):
    with open(file_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


import sys
import pickle
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout, \
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

        main_layout = QVBoxLayout(central_widget)

        self.exit_btn = QPushButton("EXIT", central_widget)
        main_layout.addWidget(self.exit_btn)

        self.title_labl = QLabel("ENGINEERING MANAGEMENT PROJECT", central_widget)
        main_layout.addWidget(self.title_labl)

        self.add_model_selection_section(main_layout)

        self.add_user_details_section(main_layout)

        self.add_prediction_section(main_layout)

        self.predict_btn = QPushButton("PREDICT", central_widget)
        main_layout.addWidget(self.predict_btn)
        self.predict_btn.clicked.connect(self.predict)

    def add_model_selection_section(self, main_layout):
        self.selectmodel_labl = QLabel("Select Model", self)
        main_layout.addWidget(self.selectmodel_labl)

        self.horizontalLayoutWidget = QWidget()
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)

        self.model1 = QRadioButton("Linear Regression", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model1)

        self.model2 = QRadioButton("Random Forest", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model2)

        self.model3 = QRadioButton("Support Vector Regressor", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model3)

        self.model4 = QRadioButton("Decision Tree", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model4)

        self.model5 = QRadioButton("Gradient Boosting", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model5)

        self.model6 = QRadioButton("Lasso Regression", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.model6)

        main_layout.addWidget(self.horizontalLayoutWidget)


    def add_user_details_section(self, main_layout):
        self.user_details_labl = QLabel("User Details", self)
        main_layout.addWidget(self.user_details_labl)

        self.widget = QWidget(self)
        main_layout.addWidget(self.widget)

        user_details_layout = QVBoxLayout(self.widget)

        self.label_gender = QLabel("Gender", self)
        user_details_layout.addWidget(self.label_gender)

        self.horizontalLayoutWidget_3 = QWidget(self)
        self.sel_scholarship_2 = QHBoxLayout(self.horizontalLayoutWidget_3)

        self.yes_btn_2 = QRadioButton("MALE", self.horizontalLayoutWidget_3)
        self.sel_scholarship_2.addWidget(self.yes_btn_2)

        self.no_btn_2 = QRadioButton("FEMALE", self.horizontalLayoutWidget_3)
        self.sel_scholarship_2.addWidget(self.no_btn_2)

        user_details_layout.addWidget(self.horizontalLayoutWidget_3)

        self.label_scholarship = QLabel("Availing any Scholarship?", self)
        self.horizontalLayoutWidget_4 = QWidget(self)
        self.sel_scholarship = QHBoxLayout(self.horizontalLayoutWidget_4)

        self.yes_btn = QRadioButton("YES", self.horizontalLayoutWidget_4)
        self.sel_scholarship.addWidget(self.yes_btn)

        self.no_btn = QRadioButton("NO", self.horizontalLayoutWidget_4)
        self.sel_scholarship.addWidget(self.no_btn)

        user_details_layout.addWidget(self.label_scholarship)
        user_details_layout.addWidget(self.horizontalLayoutWidget_4)

        self.label_matric = QLabel("Matric Percentage", self)
        self.sel_matric = QDoubleSpinBox(self)
        # Configure QDoubleSpinBox properties as needed
        user_details_layout.addWidget(self.label_matric)
        user_details_layout.addWidget(self.sel_matric)

        self.label_inter = QLabel("Intermediate Percentage", self)
        self.sel_inter = QDoubleSpinBox(self)
        # Configure QDoubleSpinBox properties as needed
        user_details_layout.addWidget(self.label_inter)
        user_details_layout.addWidget(self.sel_inter)

        # Add more user details fields as needed

        self.label_interest = QLabel("Interest in Program", self)
        self.interest_combobox = QComboBox(self)
        self.interest_combobox.addItems(["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
        user_details_layout.addWidget(self.label_interest)
        user_details_layout.addWidget(self.interest_combobox)


    def add_prediction_section(self, main_layout):
        self.prediction_labl = QLabel("Prediction", self)
        main_layout.addWidget(self.prediction_labl)

        self.pred_accuracy_labl = QLabel("Accuracy", self)
        self.pred_sgpa_labl = QLabel("SGPA of 5th Semester", self)
        self.pred_cgpa_labl = QLabel("CGPA of 5th Semester", self)

        self.pred_accuracy = QLabel("IDK", self)
        self.pred_sgpa = QLabel("IDK", self)
        self.pred_cgpa = QLabel("IDK", self)

        main_layout.addWidget(self.pred_accuracy_labl)
        main_layout.addWidget(self.pred_sgpa_labl)
        main_layout.addWidget(self.pred_cgpa_labl)
        main_layout.addWidget(self.pred_accuracy)
        main_layout.addWidget(self.pred_sgpa)
        main_layout.addWidget(self.pred_cgpa)

    def predict(self):
        selected_model = None
        if self.model1.isChecked():
            selected_model = load_model('linear_regression_model.pkl')
        # Add similar conditions for other models

        if selected_model is not None:
            input_values = [
                int(self.no_btn_2.isChecked()),  # Gender
                # Add other user details values here
            ]

            mapping = {
                "Strongly Disagree": 0,
                "Disagree": 1,
                "Neutral": 2,
                "Agree": 3,
                "Strongly Agree": 4
            }

            interest_level = [
                "Strongly Disagree",
                "Disagree",
                "Neutral",
                "Agree",
                "Strongly Agree"
            ][self.interest_combobox.currentIndex()]

            input_values.append(mapping[interest_level])

            input_df = pd.DataFrame([input_values], columns=[
                'Gender',  # Add other column names here
                'Interest Level'
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
