"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.interp_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, one = "01", zero = "00"):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.interp_block.__init__(
            self,
            name='Binary Coder',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8],
            interp = len(one)
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.one = one
        self.zero = zero
        self.len = len(one)

    def work(self, input_items, output_items):
        """example: multiply with constant"""

        output_items[0][:] = np.array([np.uint8(self.one[i % self.len]) if input_items[0][i / self.len] == 1 else np.uint8(self.zero[i % self.len]) for i in range(len(output_items[0]))])
        #print(len(input_items[0]))
        return len(output_items[0])
