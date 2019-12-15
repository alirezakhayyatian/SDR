"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.decim_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, decim = 1, begin = 0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.decim_block.__init__(
            self,
            name='Decimator',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32],
            decim = int(decim)
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.decim = decim
        self.begin = begin

    def work(self, input_items, output_items):
        """Decimator"""
        index = [int(self.begin + i * self.decim) for i in range(len(output_items[0]))]
        output_items[0][:] = np.array([input_items[0][i] for i in index])

        return len(output_items[0])

