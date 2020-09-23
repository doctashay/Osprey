import testing
import time
from testing import Tests

import pycdlib
import sys
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
iso = pycdlib.PyCdlib()
iso.open_fp('C:\\new.iso')

bazstr = b'bazzzzzz\n'
iso.modify_file_in_place(BytesIO(bazstr), len(bazstr), '/FOO.;1')
modifiediso = BytesIO()
iso.write_fp(modifiediso)
iso.close()