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

    def __init__(self,one='01',zero='00'):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.decim_block.__init__(
            self,
            name='Binary Decoder',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32],
            decim = len(one)
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).


    def work(self, input_items, output_items):
        """example: multiply with constant"""
        '''out =[]
        for i in range( len(input_items[0])-1 ):
            if( input_items[0][i] == input_items[0][i+1] ):
                out.append( 1 )
            else:
                out.append( 0 )
            i+=1
        output_items[0] = out'''
        #print(len(input_items[0]))
        output_items[0][:] = [0 if (input_items[0][2*i] ==input_items[0][2*i+1]) else 1   for i in range( int(len(input_items[0])/2) ) ]
        return len(output_items[0])






