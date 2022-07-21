import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from sm import mengecek_
    mengecek_()
elif bit == '32bit':
    from sm import mengeck_
    mengeck_()
