import pycdlib
import sys
import time
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class Utils(object):
    def create_and_modify():
        #Create new ISO file with starting file FOO
        iso = pycdlib.PyCdlib()
        iso.new()
        foostr = b'foo\n'
        iso.add_fp(BytesIO(foostr), len(foostr), '/FOO.;1')

        outiso = BytesIO()
        iso.write_fp(outiso)
        iso.write("C:\\test.iso")
        iso.close()

        #Modify file FOO with data from bazstr
        iso = pycdlib.PyCdlib()
        iso.open_fp(outiso)
        bazstr = b'feelsgoodman\n'
        iso.modify_file_in_place(BytesIO(bazstr), len(bazstr), '/FOO.;1')

        modifiediso = BytesIO()
        iso.write_fp(modifiediso)

        #It works! I think?
        iso.write("C:\\test.iso")
        iso.close()
    def test_jak():
        #Test writing data to a Jak and Daxter ISO file
        iso = pycdlib.PyCdlib()
        isopath = "C:\\jak.iso" #Hardcoded for now
        iso.open(isopath) 

        print("Getting ISO Contents for", isopath)
        for child in iso.list_children(iso_path='/'):
            print(child.file_identifier())

        #Throws an ISO padding exception when attempting to call modify method, disabled for now
        #bazzstr = b''
        #iso.modify_file_in_place(BytesIO(bazzstr), len(bazzstr), b'/TEXT/0COMMON.TXT')

        #outiso = BytesIO()
        #iso.write_fp(outiso)
        #iso.write("C:\\jak.iso")
        iso.close()
    def list_contents():
        #Test command line arguments for a given ISO file. Just lists file contents for now
        iso = pycdlib.PyCdlib()
        isopath = "C:\\jakx.iso"
        sys.argv[1] = isopath #Hardcoded for now
        iso.open(sys.argv[1])


        print("Listing ISO contents for ", isopath)
        for child in iso.list_children(iso_path='/'):
            print(child.file_identifier())

        iso.close()
