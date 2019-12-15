"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,preamble="1111111",num_packed=207):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='Addind Preamble',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        ''' set size of output'''
        self.set_output_multiple(num_packed)

        self.pre = map(np.uint8,preamble)
        self.num_pre = len(preamble)

        self.num_packed = num_packed
        self.num_data = num_packed - self.num_pre

    def forecast(self, noutput_items, ninput_items_required):
           ninput_items_required[0] = self.len_input_func(noutput_items)


    def general_work(self, input_items, output_items):

        num = int( self.len_input_func( len(output_items[0]) ) / self.num_data )
        #print(num)
        output_items[0][:] = [self.pre[j] if j<self.num_pre else 
        input_items[0][i* self.num_data + ( j - self.num_pre ) ] for i in range(num)
        for j in range(self.num_packed)   ]

        self.consume(0, self.len_input_func( len(output_items[0]) )  )
        return len(output_items[0])

  
    def len_input_func(self, noutput):
        ''' set size of input using size of output ''' 
        n=int(noutput / self.num_packed )
        return (noutput - n * self.num_pre )






