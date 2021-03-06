from cPickle import load


import Gui.MainWindow as mw_gui
from dialog_load_data_intel import Ui_Data_Dialog_interaction
from dialog_import_model_intel import Ui_Import_Model_Interaction
from dialog_specifications_intel import Ui_Specifications_Interaction
import cv2
import os
from PySide import QtCore, QtGui
from Utils import variables as vars
from main_right_panel_widget_intel import ImageWidget
from main_left_panel_widget_intel import LayersWidget
from Gui.main_right_panel_widget import Ui_main_right_panel_widget
from Gui.MainWindow import Ui_MainWindow
from Image.scan import Scan
from Image.layers import Layers
from Gui.main_left_panel_widget import Ui_main_left_panel_widget

@QtCore.Slot()
def signals_and_slots_checkboxes():
    for i in range(len(global_vars.layers_checkboxes)):
        global_vars.layers_checkboxes[i].toggled.connect(Img_Layer.generate_all_layers)


if __name__ == "__main__":
    import sys

    global_vars = vars.Variables()

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mw_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    img_widget = ImageWidget(MainWindow, global_vars)
    img_layer_widget = LayersWidget(MainWindow, global_vars)

    ui.splitter_right_layout.addWidget(img_widget)
    ui.splitter_left_layout.addWidget(img_layer_widget)


    Ui_dit = Ui_Data_Dialog_interaction(global_vars)
    Ui_idm = Ui_Import_Model_Interaction(global_vars)
    Ui_ds = Ui_Specifications_Interaction(global_vars)

    Img_Scanner = Scan(global_vars)
    Img_Layer = Layers(global_vars)


    #CONNECTS

    # tab actions:
    ui.actionData_Import.triggered.connect(Ui_dit.open_dialog)
    ui.actionImport_Model.triggered.connect(Ui_idm.open_dialog)
    ui.actionSpecifications.triggered.connect(Ui_ds.open_dialog)
    ui.actionRunModel.triggered.connect(Img_Scanner.scan_img)


    # user interface updates:
    Ui_dit.update_img.connect(img_widget.update_image)
    Ui_idm.update_model_data.connect(Ui_ds.update_specs)
    Img_Scanner.update_layers_list.connect(img_layer_widget.add_classes_checkboxes)
    Img_Scanner.update_layers_list.connect(signals_and_slots_checkboxes)


    sys.exit(app.exec_())
