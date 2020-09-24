import common_utils
from common_utils import Utils

class Tests(object):
    def run_tests():
        Utils.create_and_modify() #Create a brand new ISO and output it to C:\
        Utils.test_jak() #Open a hardcoded Jak ISO and list the contents (TODO: Modify 0COMMON.TXT)
        Utils.list_contents() #Opens any specified ISO and lists the contents 

