import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sally/Desktop/thesis/digi_twins/install/twin_control'
