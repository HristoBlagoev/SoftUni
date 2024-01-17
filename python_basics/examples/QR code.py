import address as address
import pyqrcode
import png
from pyqrcode import QRcode

adress = 'https://www.youtube.com/watch?v=29HZ8Ec_2PE'
url = pyqrcode.create(address)
url.png('Music.png', scale = 8)

