import os
import sys

if __name__ == '__main__':
    os.system(f"pyrcc5 ../src/my_qrc.qrc -o my_qrc_rc.py")

    ui_file_path_list = [
        "ui_admin_widget",
        "ui_chat_room",
        "ui_dashboard",
        "ui_employee_finder",
        "ui_login_widget",
        "ui_medical_widget",

    ]
    for ui_file in ui_file_path_list:
        os.system(f'python  -m PyQt5.uic.pyuic --import-from=Client.ui -x {ui_file}.ui -o compiled_{ui_file}.py')
