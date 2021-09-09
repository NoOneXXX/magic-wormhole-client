import sys
from pathlib import Path
from os.path import expanduser
import os


class source_file:
    def __init__(self, file_path):
        file_path = Path(file_path).resolve()
        assert file_path.exists()

        self.name = file_path.name
        self.full_path = file_path
        self.final_bytes = None
        self.transfer_bytes = None
        self.file_object = None

    def open(self):
        self.file_object = open(self.full_path, "rb")
        self.file_object.seek(0, 2)
        self.final_bytes = self.file_object.tell()
        self.transfer_bytes = self.final_bytes
        self.file_object.seek(0, 0)


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

"""
get default path
"""
def get_defaul_path():
    default_dir = ''
    if get_platform() == 'windows':
        default_dir = expanduser("~\Desktop")
    else:
        default_dir = expanduser("~/Desktop")
    return default_dir

def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
