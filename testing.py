import common_utils
from common_utils import Utils

class Tests(object):
    def run_tests():
        print("Testing Creating ISO")
        Utils.write_iso()
        print("ISO Created")
        print("Testing Opening ISO")
        Utils.open_iso()
        print("ISO opened, file contents")
        print("Modifying test ISO file")
        Utils.modify_iso()

