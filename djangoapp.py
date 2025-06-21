import sys
sys.path.insert(0, './HelloWorld')
from HelloWorld import wsgi


app = wsgi.application