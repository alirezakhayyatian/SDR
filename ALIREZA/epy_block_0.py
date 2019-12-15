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

    def __init__(self, sps=8, carier=2000 , samp_rate=32000):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.interp_block.__init__(
            self,
            name='fsk_mod_alireza',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32],
            interp = int(sps)
            
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.sps = sps
        self.T = float(sps)/float(samp_rate)
        self.sep_freq = float(samp_rate /(sps) )

        self.first = [np.cos(2 * np.pi * (float(carier)) * float(i) / float(samp_rate) ) for i in range(sps) ]
               
        self.second = [np.cos(2 * np.pi * (float(carier) + self.sep_freq ) * float(i) /float(samp_rate)) for i in range(sps) ]
    
    def work(self, input_items, output_items):

        output_items[0][:] =[self.first[j] if input_items[0][i] == 0 else self.second[j]
        for i in range( len(input_items[0])) for j in range(self.sps) ]

        return len(output_items[0])







