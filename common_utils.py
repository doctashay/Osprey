import pycdlib
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



