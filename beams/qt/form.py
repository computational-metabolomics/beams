# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(795, 842)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_general = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_general.setGeometry(QtCore.QRect(20, 8, 761, 151))
        self.groupBox_general.setTitle("")
        self.groupBox_general.setObjectName("groupBox_general")
        self.lineEdit_intensity_matrix = QtWidgets.QLineEdit(self.groupBox_general)
        self.lineEdit_intensity_matrix.setGeometry(QtCore.QRect(120, 60, 161, 20))
        self.lineEdit_intensity_matrix.setText("")
        self.lineEdit_intensity_matrix.setReadOnly(True)
        self.lineEdit_intensity_matrix.setObjectName("lineEdit_intensity_matrix")
        self.lineEdit_peaklist = QtWidgets.QLineEdit(self.groupBox_general)
        self.lineEdit_peaklist.setEnabled(True)
        self.lineEdit_peaklist.setGeometry(QtCore.QRect(120, 30, 161, 20))
        self.lineEdit_peaklist.setText("")
        self.lineEdit_peaklist.setReadOnly(True)
        self.lineEdit_peaklist.setObjectName("lineEdit_peaklist")
        self.pushButton_peaklist = QtWidgets.QPushButton(self.groupBox_general)
        self.pushButton_peaklist.setEnabled(True)
        self.pushButton_peaklist.setGeometry(QtCore.QRect(290, 28, 71, 23))
        self.pushButton_peaklist.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_peaklist.setMaximumSize(QtCore.QSize(81, 16777215))
        self.pushButton_peaklist.setObjectName("pushButton_peaklist")
        self.label_peaklist = QtWidgets.QLabel(self.groupBox_general)
        self.label_peaklist.setEnabled(True)
        self.label_peaklist.setGeometry(QtCore.QRect(12, 30, 81, 16))
        self.label_peaklist.setObjectName("label_peaklist")
        self.label_intensity_matrix = QtWidgets.QLabel(self.groupBox_general)
        self.label_intensity_matrix.setGeometry(QtCore.QRect(12, 60, 111, 16))
        self.label_intensity_matrix.setObjectName("label_intensity_matrix")
        self.comboBox_ion_mode = QtWidgets.QComboBox(self.groupBox_general)
        self.comboBox_ion_mode.setGeometry(QtCore.QRect(540, 30, 111, 22))
        self.comboBox_ion_mode.setObjectName("comboBox_ion_mode")
        self.comboBox_ion_mode.addItem("")
        self.comboBox_ion_mode.addItem("")
        self.label_ion_mode = QtWidgets.QLabel(self.groupBox_general)
        self.label_ion_mode.setGeometry(QtCore.QRect(410, 32, 71, 16))
        self.label_ion_mode.setObjectName("label_ion_mode")
        self.label_ppm_tolerance = QtWidgets.QLabel(self.groupBox_general)
        self.label_ppm_tolerance.setEnabled(True)
        self.label_ppm_tolerance.setGeometry(QtCore.QRect(410, 63, 141, 16))
        self.label_ppm_tolerance.setObjectName("label_ppm_tolerance")
        self.doubleSpinBox_ppm_error = QtWidgets.QDoubleSpinBox(self.groupBox_general)
        self.doubleSpinBox_ppm_error.setGeometry(QtCore.QRect(540, 61, 111, 22))
        self.doubleSpinBox_ppm_error.setMaximum(100000.0)
        self.doubleSpinBox_ppm_error.setProperty("value", 5.0)
        self.doubleSpinBox_ppm_error.setObjectName("doubleSpinBox_ppm_error")
        self.label_data_files = QtWidgets.QLabel(self.groupBox_general)
        self.label_data_files.setEnabled(True)
        self.label_data_files.setGeometry(QtCore.QRect(10, 0, 291, 16))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_data_files.setFont(font)
        self.label_data_files.setObjectName("label_data_files")
        self.lineEdit_default_adduct_library = QtWidgets.QLineEdit(self.groupBox_general)
        self.lineEdit_default_adduct_library.setEnabled(True)
        self.lineEdit_default_adduct_library.setGeometry(QtCore.QRect(540, 92, 111, 20))
        self.lineEdit_default_adduct_library.setReadOnly(True)
        self.lineEdit_default_adduct_library.setObjectName("lineEdit_default_adduct_library")
        self.pushButton_default_adduct_library = QtWidgets.QPushButton(self.groupBox_general)
        self.pushButton_default_adduct_library.setEnabled(True)
        self.pushButton_default_adduct_library.setGeometry(QtCore.QRect(660, 90, 71, 23))
        self.pushButton_default_adduct_library.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_default_adduct_library.setObjectName("pushButton_default_adduct_library")
        self.label_sql_database = QtWidgets.QLabel(self.groupBox_general)
        self.label_sql_database.setEnabled(True)
        self.label_sql_database.setGeometry(QtCore.QRect(12, 92, 121, 16))
        self.label_sql_database.setObjectName("label_sql_database")
        self.lineEdit_sql_database = QtWidgets.QLineEdit(self.groupBox_general)
        self.lineEdit_sql_database.setEnabled(True)
        self.lineEdit_sql_database.setGeometry(QtCore.QRect(120, 92, 161, 20))
        self.lineEdit_sql_database.setText("")
        self.lineEdit_sql_database.setReadOnly(True)
        self.lineEdit_sql_database.setObjectName("lineEdit_sql_database")
        self.pushButton_sql_database = QtWidgets.QPushButton(self.groupBox_general)
        self.pushButton_sql_database.setEnabled(True)
        self.pushButton_sql_database.setGeometry(QtCore.QRect(290, 90, 71, 23))
        self.pushButton_sql_database.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_sql_database.setMaximumSize(QtCore.QSize(81, 16777215))
        self.pushButton_sql_database.setObjectName("pushButton_sql_database")
        self.lineEdit_graph = QtWidgets.QLineEdit(self.groupBox_general)
        self.lineEdit_graph.setEnabled(True)
        self.lineEdit_graph.setGeometry(QtCore.QRect(120, 123, 161, 20))
        self.lineEdit_graph.setText("")
        self.lineEdit_graph.setReadOnly(True)
        self.lineEdit_graph.setObjectName("lineEdit_graph")
        self.pushButton_graph = QtWidgets.QPushButton(self.groupBox_general)
        self.pushButton_graph.setEnabled(True)
        self.pushButton_graph.setGeometry(QtCore.QRect(290, 121, 71, 23))
        self.pushButton_graph.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_graph.setMaximumSize(QtCore.QSize(81, 16777215))
        self.pushButton_graph.setObjectName("pushButton_graph")
        self.label_graph = QtWidgets.QLabel(self.groupBox_general)
        self.label_graph.setEnabled(True)
        self.label_graph.setGeometry(QtCore.QRect(12, 123, 111, 16))
        self.label_graph.setObjectName("label_graph")
        self.pushButton_peak_matrix = QtWidgets.QPushButton(self.groupBox_general)
        self.pushButton_peak_matrix.setEnabled(True)
        self.pushButton_peak_matrix.setGeometry(QtCore.QRect(290, 56, 71, 23))
        self.pushButton_peak_matrix.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_peak_matrix.setMaximumSize(QtCore.QSize(81, 16777215))
        self.pushButton_peak_matrix.setObjectName("pushButton_peak_matrix")
        self.label_default_adduct_library = QtWidgets.QLabel(self.groupBox_general)
        self.label_default_adduct_library.setEnabled(True)
        self.label_default_adduct_library.setGeometry(QtCore.QRect(410, 94, 141, 16))
        self.label_default_adduct_library.setObjectName("label_default_adduct_library")
        self.groupBox_group_features = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_group_features.setGeometry(QtCore.QRect(20, 173, 761, 91))
        self.groupBox_group_features.setTitle("")
        self.groupBox_group_features.setObjectName("groupBox_group_features")
        self.label_max_rt = QtWidgets.QLabel(self.groupBox_group_features)
        self.label_max_rt.setEnabled(True)
        self.label_max_rt.setGeometry(QtCore.QRect(10, 33, 191, 16))
        self.label_max_rt.setObjectName("label_max_rt")
        self.checkBox_group_features = QtWidgets.QCheckBox(self.groupBox_group_features)
        self.checkBox_group_features.setEnabled(True)
        self.checkBox_group_features.setGeometry(QtCore.QRect(10, -1, 231, 17))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_group_features.setFont(font)
        self.checkBox_group_features.setChecked(True)
        self.checkBox_group_features.setObjectName("checkBox_group_features")
        self.doubleSpinBox_max_rt = QtWidgets.QDoubleSpinBox(self.groupBox_group_features)
        self.doubleSpinBox_max_rt.setGeometry(QtCore.QRect(210, 30, 81, 22))
        self.doubleSpinBox_max_rt.setMaximum(9999999.0)
        self.doubleSpinBox_max_rt.setProperty("value", 5.0)
        self.doubleSpinBox_max_rt.setObjectName("doubleSpinBox_max_rt")
        self.comboBox_grouping_method = QtWidgets.QComboBox(self.groupBox_group_features)
        self.comboBox_grouping_method.setGeometry(QtCore.QRect(540, 31, 151, 22))
        self.comboBox_grouping_method.setObjectName("comboBox_grouping_method")
        self.comboBox_grouping_method.addItem("")
        self.comboBox_grouping_method.addItem("")
        self.doubleSpinBox_p_value = QtWidgets.QDoubleSpinBox(self.groupBox_group_features)
        self.doubleSpinBox_p_value.setGeometry(QtCore.QRect(540, 57, 151, 22))
        self.doubleSpinBox_p_value.setDecimals(10)
        self.doubleSpinBox_p_value.setMaximum(1.0)
        self.doubleSpinBox_p_value.setSingleStep(0.01)
        self.doubleSpinBox_p_value.setProperty("value", 0.01)
        self.doubleSpinBox_p_value.setObjectName("doubleSpinBox_p_value")
        self.label_tool_p_value = QtWidgets.QLabel(self.groupBox_group_features)
        self.label_tool_p_value.setEnabled(True)
        self.label_tool_p_value.setGeometry(QtCore.QRect(410, 60, 121, 16))
        self.label_tool_p_value.setObjectName("label_tool_p_value")
        self.label_grouping_method = QtWidgets.QLabel(self.groupBox_group_features)
        self.label_grouping_method.setEnabled(True)
        self.label_grouping_method.setGeometry(QtCore.QRect(410, 33, 121, 16))
        self.label_grouping_method.setObjectName("label_grouping_method")
        self.doubleSpinBox_coefficent = QtWidgets.QDoubleSpinBox(self.groupBox_group_features)
        self.doubleSpinBox_coefficent.setGeometry(QtCore.QRect(210, 57, 81, 22))
        self.doubleSpinBox_coefficent.setMaximum(1.0)
        self.doubleSpinBox_coefficent.setSingleStep(0.1)
        self.doubleSpinBox_coefficent.setProperty("value", 0.7)
        self.doubleSpinBox_coefficent.setObjectName("doubleSpinBox_coefficent")
        self.label_tool_coefficient = QtWidgets.QLabel(self.groupBox_group_features)
        self.label_tool_coefficient.setEnabled(True)
        self.label_tool_coefficient.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.label_tool_coefficient.setObjectName("label_tool_coefficient")
        self.groupBox_annotate_peak_patterns = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_annotate_peak_patterns.setGeometry(QtCore.QRect(20, 273, 761, 101))
        self.groupBox_annotate_peak_patterns.setTitle("")
        self.groupBox_annotate_peak_patterns.setObjectName("groupBox_annotate_peak_patterns")
        self.lineEdit_adduct_library = QtWidgets.QLineEdit(self.groupBox_annotate_peak_patterns)
        self.lineEdit_adduct_library.setEnabled(True)
        self.lineEdit_adduct_library.setGeometry(QtCore.QRect(10, 58, 91, 20))
        self.lineEdit_adduct_library.setReadOnly(True)
        self.lineEdit_adduct_library.setObjectName("lineEdit_adduct_library")
        self.pushButton_adduct_library = QtWidgets.QPushButton(self.groupBox_annotate_peak_patterns)
        self.pushButton_adduct_library.setEnabled(True)
        self.pushButton_adduct_library.setGeometry(QtCore.QRect(110, 56, 71, 23))
        self.pushButton_adduct_library.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_adduct_library.setObjectName("pushButton_adduct_library")
        self.checkBox_annotate_peak_patterns = QtWidgets.QCheckBox(self.groupBox_annotate_peak_patterns)
        self.checkBox_annotate_peak_patterns.setEnabled(True)
        self.checkBox_annotate_peak_patterns.setGeometry(QtCore.QRect(10, -1, 271, 17))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_annotate_peak_patterns.setFont(font)
        self.checkBox_annotate_peak_patterns.setChecked(True)
        self.checkBox_annotate_peak_patterns.setObjectName("checkBox_annotate_peak_patterns")
        self.checkBox_adduct_library = QtWidgets.QCheckBox(self.groupBox_annotate_peak_patterns)
        self.checkBox_adduct_library.setEnabled(True)
        self.checkBox_adduct_library.setGeometry(QtCore.QRect(10, 33, 181, 17))
        self.checkBox_adduct_library.setChecked(True)
        self.checkBox_adduct_library.setObjectName("checkBox_adduct_library")
        self.checkBox_isotopes = QtWidgets.QCheckBox(self.groupBox_annotate_peak_patterns)
        self.checkBox_isotopes.setEnabled(True)
        self.checkBox_isotopes.setGeometry(QtCore.QRect(200, 33, 171, 17))
        self.checkBox_isotopes.setChecked(True)
        self.checkBox_isotopes.setObjectName("checkBox_isotopes")
        self.pushButton_multiple_charged = QtWidgets.QPushButton(self.groupBox_annotate_peak_patterns)
        self.pushButton_multiple_charged.setEnabled(True)
        self.pushButton_multiple_charged.setGeometry(QtCore.QRect(490, 56, 71, 23))
        self.pushButton_multiple_charged.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_multiple_charged.setObjectName("pushButton_multiple_charged")
        self.lineEdit_multiple_charged = QtWidgets.QLineEdit(self.groupBox_annotate_peak_patterns)
        self.lineEdit_multiple_charged.setEnabled(True)
        self.lineEdit_multiple_charged.setGeometry(QtCore.QRect(390, 58, 91, 20))
        self.lineEdit_multiple_charged.setReadOnly(True)
        self.lineEdit_multiple_charged.setObjectName("lineEdit_multiple_charged")
        self.lineEdit_isotopes = QtWidgets.QLineEdit(self.groupBox_annotate_peak_patterns)
        self.lineEdit_isotopes.setEnabled(True)
        self.lineEdit_isotopes.setGeometry(QtCore.QRect(200, 58, 91, 20))
        self.lineEdit_isotopes.setReadOnly(True)
        self.lineEdit_isotopes.setObjectName("lineEdit_isotopes")
        self.pushButton_isotopes = QtWidgets.QPushButton(self.groupBox_annotate_peak_patterns)
        self.pushButton_isotopes.setEnabled(True)
        self.pushButton_isotopes.setGeometry(QtCore.QRect(300, 56, 71, 23))
        self.pushButton_isotopes.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_isotopes.setObjectName("pushButton_isotopes")
        self.checkBox_multiple_charged = QtWidgets.QCheckBox(self.groupBox_annotate_peak_patterns)
        self.checkBox_multiple_charged.setEnabled(True)
        self.checkBox_multiple_charged.setGeometry(QtCore.QRect(390, 33, 171, 17))
        self.checkBox_multiple_charged.setChecked(True)
        self.checkBox_multiple_charged.setObjectName("checkBox_multiple_charged")
        self.checkBox_oligomers = QtWidgets.QCheckBox(self.groupBox_annotate_peak_patterns)
        self.checkBox_oligomers.setEnabled(True)
        self.checkBox_oligomers.setGeometry(QtCore.QRect(580, 33, 171, 17))
        self.checkBox_oligomers.setChecked(True)
        self.checkBox_oligomers.setObjectName("checkBox_oligomers")
        self.spinBox_max_monomer_units = QtWidgets.QSpinBox(self.groupBox_annotate_peak_patterns)
        self.spinBox_max_monomer_units.setGeometry(QtCore.QRect(670, 58, 51, 22))
        self.spinBox_max_monomer_units.setMinimum(2)
        self.spinBox_max_monomer_units.setMaximum(1000000)
        self.spinBox_max_monomer_units.setProperty("value", 2)
        self.spinBox_max_monomer_units.setDisplayIntegerBase(10)
        self.spinBox_max_monomer_units.setObjectName("spinBox_max_monomer_units")
        self.label_max_monomer_units = QtWidgets.QLabel(self.groupBox_annotate_peak_patterns)
        self.label_max_monomer_units.setEnabled(True)
        self.label_max_monomer_units.setGeometry(QtCore.QRect(580, 60, 81, 16))
        self.label_max_monomer_units.setObjectName("label_max_monomer_units")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(640, 764, 71, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(711, 764, 71, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.groupBox_annotate_molecular_formulae = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_annotate_molecular_formulae.setGeometry(QtCore.QRect(20, 383, 761, 101))
        self.groupBox_annotate_molecular_formulae.setTitle("")
        self.groupBox_annotate_molecular_formulae.setObjectName("groupBox_annotate_molecular_formulae")
        self.label_filename_mf = QtWidgets.QLabel(self.groupBox_annotate_molecular_formulae)
        self.label_filename_mf.setEnabled(False)
        self.label_filename_mf.setGeometry(QtCore.QRect(10, 65, 181, 16))
        self.label_filename_mf.setObjectName("label_filename_mf")
        self.lineEdit_filename_mf = QtWidgets.QLineEdit(self.groupBox_annotate_molecular_formulae)
        self.lineEdit_filename_mf.setEnabled(False)
        self.lineEdit_filename_mf.setGeometry(QtCore.QRect(120, 62, 161, 20))
        self.lineEdit_filename_mf.setText("")
        self.lineEdit_filename_mf.setReadOnly(True)
        self.lineEdit_filename_mf.setObjectName("lineEdit_filename_mf")
        self.checkBox_annotate_molecular_formulae = QtWidgets.QCheckBox(self.groupBox_annotate_molecular_formulae)
        self.checkBox_annotate_molecular_formulae.setEnabled(True)
        self.checkBox_annotate_molecular_formulae.setGeometry(QtCore.QRect(10, -1, 281, 17))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_annotate_molecular_formulae.setFont(font)
        self.checkBox_annotate_molecular_formulae.setChecked(True)
        self.checkBox_annotate_molecular_formulae.setObjectName("checkBox_annotate_molecular_formulae")
        self.comboBox_source_mf = QtWidgets.QComboBox(self.groupBox_annotate_molecular_formulae)
        self.comboBox_source_mf.setGeometry(QtCore.QRect(120, 30, 251, 22))
        self.comboBox_source_mf.setObjectName("comboBox_source_mf")
        self.comboBox_source_mf.addItem("")
        self.comboBox_source_mf.addItem("")
        self.label_source_mf = QtWidgets.QLabel(self.groupBox_annotate_molecular_formulae)
        self.label_source_mf.setEnabled(True)
        self.label_source_mf.setGeometry(QtCore.QRect(10, 33, 101, 16))
        self.label_source_mf.setObjectName("label_source_mf")
        self.pushButton_filename_mf = QtWidgets.QPushButton(self.groupBox_annotate_molecular_formulae)
        self.pushButton_filename_mf.setEnabled(False)
        self.pushButton_filename_mf.setGeometry(QtCore.QRect(290, 60, 71, 23))
        self.pushButton_filename_mf.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_filename_mf.setFlat(False)
        self.pushButton_filename_mf.setObjectName("pushButton_filename_mf")
        self.label_max_mz = QtWidgets.QLabel(self.groupBox_annotate_molecular_formulae)
        self.label_max_mz.setEnabled(True)
        self.label_max_mz.setGeometry(QtCore.QRect(410, 32, 121, 16))
        self.label_max_mz.setObjectName("label_max_mz")
        self.spinBox_max_mz = QtWidgets.QSpinBox(self.groupBox_annotate_molecular_formulae)
        self.spinBox_max_mz.setGeometry(QtCore.QRect(540, 28, 111, 22))
        self.spinBox_max_mz.setMaximum(1000000)
        self.spinBox_max_mz.setProperty("value", 500)
        self.spinBox_max_mz.setDisplayIntegerBase(10)
        self.spinBox_max_mz.setObjectName("spinBox_max_mz")
        self.checkBox_heuristic_rules = QtWidgets.QCheckBox(self.groupBox_annotate_molecular_formulae)
        self.checkBox_heuristic_rules.setEnabled(True)
        self.checkBox_heuristic_rules.setGeometry(QtCore.QRect(410, 63, 171, 17))
        self.checkBox_heuristic_rules.setChecked(True)
        self.checkBox_heuristic_rules.setObjectName("checkBox_heuristic_rules")
        self.groupBox_annotate_compounds = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_annotate_compounds.setGeometry(QtCore.QRect(20, 492, 761, 151))
        self.groupBox_annotate_compounds.setTitle("")
        self.groupBox_annotate_compounds.setObjectName("groupBox_annotate_compounds")
        self.checkBox_annotate_compounds = QtWidgets.QCheckBox(self.groupBox_annotate_compounds)
        self.checkBox_annotate_compounds.setEnabled(True)
        self.checkBox_annotate_compounds.setGeometry(QtCore.QRect(10, -2, 351, 17))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_annotate_compounds.setFont(font)
        self.checkBox_annotate_compounds.setChecked(True)
        self.checkBox_annotate_compounds.setObjectName("checkBox_annotate_compounds")
        self.lineEdit_filename_reference = QtWidgets.QLineEdit(self.groupBox_annotate_compounds)
        self.lineEdit_filename_reference.setEnabled(False)
        self.lineEdit_filename_reference.setGeometry(QtCore.QRect(410, 59, 161, 20))
        self.lineEdit_filename_reference.setText("")
        self.lineEdit_filename_reference.setReadOnly(True)
        self.lineEdit_filename_reference.setObjectName("lineEdit_filename_reference")
        self.pushButton_filename_reference = QtWidgets.QPushButton(self.groupBox_annotate_compounds)
        self.pushButton_filename_reference.setEnabled(False)
        self.pushButton_filename_reference.setGeometry(QtCore.QRect(580, 57, 71, 23))
        self.pushButton_filename_reference.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_filename_reference.setObjectName("pushButton_filename_reference")
        self.checkBox_filename_reference = QtWidgets.QCheckBox(self.groupBox_annotate_compounds)
        self.checkBox_filename_reference.setEnabled(True)
        self.checkBox_filename_reference.setGeometry(QtCore.QRect(410, 37, 251, 17))
        self.checkBox_filename_reference.setChecked(False)
        self.checkBox_filename_reference.setObjectName("checkBox_filename_reference")
        self.listWidget_databases = QtWidgets.QListWidget(self.groupBox_annotate_compounds)
        self.listWidget_databases.setGeometry(QtCore.QRect(10, 50, 171, 91))
        self.listWidget_databases.setObjectName("listWidget_databases")
        self.listWidget_categories = QtWidgets.QListWidget(self.groupBox_annotate_compounds)
        self.listWidget_categories.setEnabled(False)
        self.listWidget_categories.setGeometry(QtCore.QRect(200, 50, 171, 91))
        self.listWidget_categories.setObjectName("listWidget_categories")
        self.label_databases = QtWidgets.QLabel(self.groupBox_annotate_compounds)
        self.label_databases.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_databases.setObjectName("label_databases")
        self.label_categories = QtWidgets.QLabel(self.groupBox_annotate_compounds)
        self.label_categories.setEnabled(False)
        self.label_categories.setGeometry(QtCore.QRect(200, 30, 71, 16))
        self.label_categories.setObjectName("label_categories")
        self.groupBox_create_summary = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_create_summary.setGeometry(QtCore.QRect(20, 657, 761, 101))
        self.groupBox_create_summary.setTitle("")
        self.groupBox_create_summary.setObjectName("groupBox_create_summary")
        self.lineEdit_summary_filename = QtWidgets.QLineEdit(self.groupBox_create_summary)
        self.lineEdit_summary_filename.setGeometry(QtCore.QRect(110, 31, 161, 20))
        self.lineEdit_summary_filename.setText("")
        self.lineEdit_summary_filename.setReadOnly(True)
        self.lineEdit_summary_filename.setObjectName("lineEdit_summary_filename")
        self.pushButton_summary_filename = QtWidgets.QPushButton(self.groupBox_create_summary)
        self.pushButton_summary_filename.setGeometry(QtCore.QRect(280, 30, 71, 23))
        self.pushButton_summary_filename.setMinimumSize(QtCore.QSize(63, 23))
        self.pushButton_summary_filename.setObjectName("pushButton_summary_filename")
        self.label_summary_filename = QtWidgets.QLabel(self.groupBox_create_summary)
        self.label_summary_filename.setEnabled(True)
        self.label_summary_filename.setGeometry(QtCore.QRect(12, 33, 111, 16))
        self.label_summary_filename.setObjectName("label_summary_filename")
        self.spinBox_mz_digits = QtWidgets.QSpinBox(self.groupBox_create_summary)
        self.spinBox_mz_digits.setEnabled(False)
        self.spinBox_mz_digits.setGeometry(QtCore.QRect(590, 61, 41, 22))
        self.spinBox_mz_digits.setMaximum(1000000)
        self.spinBox_mz_digits.setProperty("value", 5)
        self.spinBox_mz_digits.setDisplayIntegerBase(10)
        self.spinBox_mz_digits.setObjectName("spinBox_mz_digits")
        self.checkBox_mz_digits = QtWidgets.QCheckBox(self.groupBox_create_summary)
        self.checkBox_mz_digits.setEnabled(True)
        self.checkBox_mz_digits.setGeometry(QtCore.QRect(440, 62, 121, 20))
        self.checkBox_mz_digits.setChecked(False)
        self.checkBox_mz_digits.setObjectName("checkBox_mz_digits")
        self.checkBox_create_summary = QtWidgets.QCheckBox(self.groupBox_create_summary)
        self.checkBox_create_summary.setEnabled(True)
        self.checkBox_create_summary.setGeometry(QtCore.QRect(10, -1, 261, 17))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_create_summary.setFont(font)
        self.checkBox_create_summary.setChecked(True)
        self.checkBox_create_summary.setObjectName("checkBox_create_summary")
        self.comboBox_annotations_format = QtWidgets.QComboBox(self.groupBox_create_summary)
        self.comboBox_annotations_format.setGeometry(QtCore.QRect(460, 30, 281, 22))
        self.comboBox_annotations_format.setObjectName("comboBox_annotations_format")
        self.comboBox_annotations_format.addItem("")
        self.comboBox_annotations_format.addItem("")
        self.comboBox_annotations_format.addItem("")
        self.label_annotations_format = QtWidgets.QLabel(self.groupBox_create_summary)
        self.label_annotations_format.setEnabled(True)
        self.label_annotations_format.setGeometry(QtCore.QRect(372, 33, 111, 16))
        self.label_annotations_format.setObjectName("label_annotations_format")
        self.comboBox_convert_rt = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_convert_rt.setEnabled(False)
        self.comboBox_convert_rt.setGeometry(QtCore.QRect(300, 720, 121, 22))
        self.comboBox_convert_rt.setObjectName("comboBox_convert_rt")
        self.comboBox_convert_rt.addItem("")
        self.comboBox_convert_rt.addItem("")
        self.label_separator = QtWidgets.QLabel(self.centralwidget)
        self.label_separator.setEnabled(True)
        self.label_separator.setGeometry(QtCore.QRect(32, 720, 101, 16))
        self.label_separator.setObjectName("label_separator")
        self.comboBox_separator = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_separator.setGeometry(QtCore.QRect(100, 718, 71, 22))
        self.comboBox_separator.setObjectName("comboBox_separator")
        self.comboBox_separator.addItem("")
        self.comboBox_separator.addItem("")
        self.checkBox_convert_rt = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_convert_rt.setEnabled(True)
        self.checkBox_convert_rt.setGeometry(QtCore.QRect(210, 720, 91, 20))
        self.checkBox_convert_rt.setChecked(False)
        self.checkBox_convert_rt.setObjectName("checkBox_convert_rt")
        self.groupBox_annotate_peak_patterns.raise_()
        self.groupBox_general.raise_()
        self.groupBox_group_features.raise_()
        self.pushButton_start.raise_()
        self.pushButton_cancel.raise_()
        self.groupBox_annotate_molecular_formulae.raise_()
        self.groupBox_annotate_compounds.raise_()
        self.groupBox_create_summary.raise_()
        self.comboBox_convert_rt.raise_()
        self.label_separator.raise_()
        self.comboBox_separator.raise_()
        self.checkBox_convert_rt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_example_data = QtWidgets.QMenu(self.menubar)
        self.menuAdd_example_data.setObjectName("menuAdd_example_data")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExampleData = QtWidgets.QAction(MainWindow)
        self.actionExampleData.setObjectName("actionExampleData")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAdd_example_data.addAction(self.actionExampleData)
        self.menuAdd_example_data.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAdd_example_data.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BEAMS - Birmingham mEtabolite Annotation for Mass Spectrometry"))
        self.pushButton_peaklist.setText(_translate("MainWindow", "Browse..."))
        self.label_peaklist.setText(_translate("MainWindow", "Peaklist:"))
        self.label_intensity_matrix.setText(_translate("MainWindow", "Intensity matrix:"))
        self.comboBox_ion_mode.setItemText(0, _translate("MainWindow", "Positive"))
        self.comboBox_ion_mode.setItemText(1, _translate("MainWindow", "Negative"))
        self.label_ion_mode.setText(_translate("MainWindow", "Ion mode:"))
        self.label_ppm_tolerance.setText(_translate("MainWindow", "Mass tolerance (ppm):"))
        self.label_data_files.setText(_translate("MainWindow", "Data Files & General Settings"))
        self.lineEdit_default_adduct_library.setText(_translate("MainWindow", "Use default"))
        self.pushButton_default_adduct_library.setText(_translate("MainWindow", "Browse..."))
        self.label_sql_database.setText(_translate("MainWindow", "Database:"))
        self.pushButton_sql_database.setText(_translate("MainWindow", "Save as..."))
        self.pushButton_graph.setText(_translate("MainWindow", "Save as..."))
        self.label_graph.setText(_translate("MainWindow", "Graph:"))
        self.pushButton_peak_matrix.setText(_translate("MainWindow", "Browse..."))
        self.label_default_adduct_library.setText(_translate("MainWindow", "Adduct library:"))
        self.label_max_rt.setText(_translate("MainWindow", "Maximum RT difference (sec):"))
        self.checkBox_group_features.setText(_translate("MainWindow", "Group Features"))
        self.comboBox_grouping_method.setItemText(0, _translate("MainWindow", "Pearson correlation"))
        self.comboBox_grouping_method.setItemText(1, _translate("MainWindow", "Spearman-rank correlation"))
        self.label_tool_p_value.setText(_translate("MainWindow", "P-value threshold:"))
        self.label_grouping_method.setText(_translate("MainWindow", "Grouping method:"))
        self.label_tool_coefficient.setText(_translate("MainWindow", "Coefficent threshold:"))
        self.lineEdit_adduct_library.setText(_translate("MainWindow", "Use default"))
        self.pushButton_adduct_library.setText(_translate("MainWindow", "Browse..."))
        self.checkBox_annotate_peak_patterns.setText(_translate("MainWindow", "Annotate Peak Patterns"))
        self.checkBox_adduct_library.setText(_translate("MainWindow", "Adducts"))
        self.checkBox_isotopes.setText(_translate("MainWindow", "Isotopes"))
        self.pushButton_multiple_charged.setText(_translate("MainWindow", "Browse..."))
        self.lineEdit_multiple_charged.setText(_translate("MainWindow", "Use default"))
        self.lineEdit_isotopes.setText(_translate("MainWindow", "Use default"))
        self.pushButton_isotopes.setText(_translate("MainWindow", "Browse..."))
        self.checkBox_multiple_charged.setText(_translate("MainWindow", "Multiple charged ions"))
        self.checkBox_oligomers.setText(_translate("MainWindow", "Oligomers"))
        self.label_max_monomer_units.setText(_translate("MainWindow", "Monomer Units:"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_filename_mf.setText(_translate("MainWindow", "Reference file:"))
        self.checkBox_annotate_molecular_formulae.setText(_translate("MainWindow", "Annotate Molecular Formulae"))
        self.comboBox_source_mf.setItemText(0, _translate("MainWindow", "http://multiomics-int.cs.bham.ac.uk"))
        self.comboBox_source_mf.setItemText(1, _translate("MainWindow", "Tab-delimited text file"))
        self.label_source_mf.setText(_translate("MainWindow", "Source:"))
        self.pushButton_filename_mf.setText(_translate("MainWindow", "Browse..."))
        self.label_max_mz.setText(_translate("MainWindow", "Maximum m/z:"))
        self.checkBox_heuristic_rules.setText(_translate("MainWindow", "Heuristic rules"))
        self.checkBox_annotate_compounds.setText(_translate("MainWindow", "Annotate Compounds / Metabolites"))
        self.pushButton_filename_reference.setText(_translate("MainWindow", "Browse..."))
        self.checkBox_filename_reference.setText(_translate("MainWindow", "Reference file"))
        self.label_databases.setText(_translate("MainWindow", "Databases"))
        self.label_categories.setText(_translate("MainWindow", "Categories"))
        self.pushButton_summary_filename.setText(_translate("MainWindow", "Save as..."))
        self.label_summary_filename.setText(_translate("MainWindow", "Summary:"))
        self.checkBox_mz_digits.setText(_translate("MainWindow", "Number of digits m/z:"))
        self.checkBox_create_summary.setText(_translate("MainWindow", "Create summary"))
        self.comboBox_annotations_format.setItemText(0, _translate("MainWindow", "Multiple rows for each feature"))
        self.comboBox_annotations_format.setItemText(1, _translate("MainWindow", "Single row for each feature and separate columns"))
        self.comboBox_annotations_format.setItemText(2, _translate("MainWindow", "Single row for each feature and merged columns"))
        self.label_annotations_format.setText(_translate("MainWindow", "Annotations:"))
        self.comboBox_convert_rt.setItemText(0, _translate("MainWindow", "Minutes"))
        self.comboBox_convert_rt.setItemText(1, _translate("MainWindow", "Seconds"))
        self.label_separator.setText(_translate("MainWindow", "Separator:"))
        self.comboBox_separator.setItemText(0, _translate("MainWindow", "tab"))
        self.comboBox_separator.setItemText(1, _translate("MainWindow", "comma"))
        self.checkBox_convert_rt.setText(_translate("MainWindow", "Convert RT:"))
        self.menuAdd_example_data.setTitle(_translate("MainWindow", "Help"))
        self.actionExampleData.setText(_translate("MainWindow", "Add example data"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
