import testing
import time
from testing import Tests

import pycdlib
import sys
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

Tests.run_tests()
