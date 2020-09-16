import pycdlib
import sys
import time
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class Utils(object):
    def write_iso():
        print("Creating basic ISO")
        #Create new PyCdLib object
        iso = pycdlib.PyCdlib()
        iso.new()

        #Add file to ISO with data passed from foostr.
        foostr = b'foo\n'
        iso.add_fp(BytesIO(foostr), len(foostr), '/FOO.;1') 

        #Create new directory inside the ISO file
        iso.add_directory('/TEST')

        #Add file to new directory /TEST/ with data passed from foostr
        iso.add_fp(BytesIO(foostr), len(foostr), '/TEST/FOO.;1') 

        #Master the ISO file and output to build directory
        iso.write('new.iso') 

        #Close PyCdLib object
        iso.close()
    def open_iso():
        iso = pycdlib.PyCdlib()
        iso.open("C:\iso.iso") #Hardcoded for now

        for child in iso.list_children(iso_path='/'):
            print(child.file_identifier())

        iso.close()
    def modify_iso():
        iso = pycdlib.PyCdlib()
        iso.new()
        foostr = b'foo\n'
        iso.add_fp(BytesIO(foostr), len(foostr), '/FOO.;1')
        outiso = BytesIO()
        iso.write_fp(outiso)
        iso.close()

        iso.open_fp(outiso)

        bazstr = b'bazzzzzz\n'
        iso.modify_file_in_place(BytesIO(bazstr), len(bazstr), '/FOO.;1')

        modifiediso = BytesIO()
        iso.write_fp(modifiediso)
        iso.close()
