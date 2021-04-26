from nrzi import NRZI
from hdb3 import HDB3
from manchester import Manchester
from multilevel import Multilevel

bits = Manchester("10110010")
bits.encode()
print("Bits:", bits.get_bits())
print("Code:", bits.get_code())

bits.plot()