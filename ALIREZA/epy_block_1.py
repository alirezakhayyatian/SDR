"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, len_packet=107,samp_per_sym =12,num_idle=7):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='Detect Preamble',   # will show up in GRC
            in_sig=[np.float32,np.float32],
            out_sig=[np.float32]
        )

        self.set_output_multiple( samp_per_sym * len_packet )


        self.len_packet = len_packet
        self.samp_per_sym = samp_per_sym
        self.num_idle = num_idle
        self.key = pmt.intern("start")
        self.value = pmt.intern("100")
        self.value1 = pmt.intern("999")

        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def forecast(self, noutput_items, ninput_items_required):
        ninput_items_required[0] = noutput_items + self.len_packet * self.samp_per_sym
        ninput_items_required[1] = noutput_items + self.len_packet * self.samp_per_sym



    def general_work(self, input_items, output_items):
        lenin = int(len(output_items[0]))
        index =[]
        temp = []
        for i in range( lenin -1 ):               
            if( input_items[1][i] >0.98 ):
                if( (input_items[1][i] >= input_items[1][i-1]) and (input_items[1][i] > input_items[1][i+1] ) ):
                    if  ( (len(index) !=0 ) and ( (i-index[-1]) < self.samp_per_sym * self.num_idle) ):
                        index.remove( index[-1] )
                        index.append( i )
                    else:
                        index.append(i)
                    
           
        for i in index:
            self.add_item_tag(0, self.nitems_written(0) + i, self.key, self.value)

        
        output_items[0][:]=[ input_items[0][i] for i in range( lenin ) ]

        self.consume(0, lenin)
        self.consume(1, lenin)

        return lenin

        
        

    '''
        for k in range(len(index)):

            if(k==0):
                self.add_item_tag(0, self.nitems_written(0) + index[k], self.key, self.value)
            else:
                aa=index[k]-index[k-1]
                if( int(aa/(self.samp_per_sym)) == self.len_packet ):
                    self.add_item_tag(0, self.nitems_written(0) + index[k], self.key, self.value)
                else:
                    index.remove( index[k] )
                    #self.add_item_tag(0, self.nitems_written(0) + index[k], self.key, self.value)
                    #self.add_item_tag(0, self.nitems_written(0) + i, self.key, self.value1)
'''
