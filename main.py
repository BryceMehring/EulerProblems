import sys
from source.common import common

if len(sys.argv) > 1:
    execfile('source/' + sys.argv[1] + '/main.py')
