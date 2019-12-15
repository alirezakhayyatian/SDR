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

    def __init__(self,len_packet=107,num_idle=7,sps =12 ):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='remove preamble',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        self.set_output_multiple(sps*len_packet - sps*num_idle)

        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.len_packet = len_packet
        self.num_idle = num_idle
        self.len_data = len_packet - num_idle
        self.sps = sps
    def forecast(self, noutput_items, ninput_items_required):
        ninput_items_required[0] = self.calc_input_size(noutput_items)
        


    def general_work(self, input_items, output_items):
        #lenin = int(len(output_items[0]))
        #num = int(lenin / self.len_data)


        len_out = len(output_items[0])
        lenin = self.calc_input_size(len_out)
        num = int(len_out / (self.len_data * self.sps ))


        tags = self.get_tags_in_window(0, 0, lenin)
        index = np.array([i.offset - self.nitems_read(0) for i in tags])
        len_index = len(index)
        out_temp = []

        #for j in range( len_index - 1 ):
        #    print( (index[j+1]-index[j])*1.0/self.sps )
    
        #print('YYY') 

        num1 =min(len_index-1,num)        
        for j in range( num1 ):
            for i in range( self.len_data *self.sps):
                out_temp.append( input_items[0][ index[j]+i+1] )

        for i in range( num1 * self.len_data * self.sps ):
            output_items[0][i]=out_temp[i]
        #output_items[0][:] = [.5 for i in range(len(output_items[0]))]
        #print(len_index-1)
        #print(num)
        #print(num1)
        #print('rrr')

        self.consume(0,  num1 * self.len_data * self.sps )

        return ( num1 * self.len_data * self.sps )


    def calc_input_size(self, output_size):
        n = int(output_size /(self.sps* self.len_data) )
        return output_size + n * self.sps * self.num_idle
