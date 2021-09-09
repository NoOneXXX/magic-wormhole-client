from PyQt5.QtCore import pyqtSignal, QObject

"""
signal collection class 
I will adding many comment in this class and other class
but never write any chinese word ,this is not for expression emotion the real reason is not writing chinese word in my 
gnome system ,There is not suitable inputting here so choose english to do all comment 
"""


class signal_(QObject):
    """this is for get code setting below , never delete it or change """
    set_code_signal = pyqtSignal(str)
    close_rec_dialog = pyqtSignal()
    close_send_dialog = pyqtSignal()
    start_receive_file = pyqtSignal()

    render_send_percent_number = pyqtSignal(str)
    render_rec_percent_number = pyqtSignal(str)

    send_file_name_and_size = pyqtSignal(str)
    rec_file_name_and_size = pyqtSignal(str)

    close_inner_dialog_event = pyqtSignal(int)
    about_notify_to_user = pyqtSignal(int)

    three_seconds_countdown_then_close_dialog = pyqtSignal(int)

    open_hint_dialog_finished_transfer_file = pyqtSignal(str)





