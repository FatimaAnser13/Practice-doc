
import sys

if sys.prefix != sys.base_prefix:
    print("Inside a virtual environment")
else:
    print("Using global Python")
