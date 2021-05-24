'''
@author: oluiscabral
'''
import platform


def get_sys_sep():
    sep = '/'
    if platform.system().upper() == 'WIN32':
        sep = '\\'
    return sep


class PlatformInfo:
    PLATFORM = platform.system().upper()
    PATH_SEPARATOR = get_sys_sep()
