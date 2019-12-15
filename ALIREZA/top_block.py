#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Dec 16 01:31:00 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from block__power import block__power  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import epy_block_0
import epy_block_0_1
import epy_block_1
import epy_block_2
import epy_block_2_1
import epy_block_3
import epy_block_4
import epy_block_5
import numpy as np
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 600e3
        self.deltaF = deltaF = samp_rate/(sps)
        self.carrier = carrier = deltaF
        self.num_idle = num_idle = 8
        self.len_data = len_data = 124
        self.e2 = e2 = sum([np.power(np.cos(2 * np.pi * (float(carrier) + deltaF) * float(i) / float(samp_rate)), 2) for i in range(sps)])
        self.e1 = e1 = sum([np.power(np.cos(2 * np.pi * float(carrier) * float(i) / float(samp_rate)), 2) for i in range(sps)])

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(True)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 3, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	5000, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 0, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [3, 0, 3, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.interp_fir_filter_xxx_1_0 = filter.interp_fir_filter_fff(1, ([np.cos(2 * np.pi  * (float(carrier)+ deltaF) * float(i) /float(samp_rate) )/e2  for i in range(sps)]))
        self.interp_fir_filter_xxx_1_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_1 = filter.interp_fir_filter_fff(1, ([np.cos(2 * np.pi  * float(carrier) * float(i) /float(samp_rate))/e1 for i in range(sps)]))
        self.interp_fir_filter_xxx_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(1, ([1.0 / float(num_idle * (sps-1)) for i in range(num_idle*(sps-1)) ]))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_5 = epy_block_5.blk(one='01', zero='00')
        self.epy_block_4 = epy_block_4.blk(len_packet=len_data + num_idle, num_idle=num_idle, sps=sps)
        self.epy_block_3 = epy_block_3.blk(in0=0, in1=1)
        self.epy_block_2_1 = epy_block_2_1.blk(decim=sps, begin=sps-1)
        self.epy_block_2 = epy_block_2.blk(preamble=''.join( ['1' for i in range(num_idle)] ), num_packed=len_data + num_idle)
        self.epy_block_1 = epy_block_1.blk(len_packet=len_data + num_idle, samp_per_sym=sps, num_idle=num_idle)
        self.epy_block_0_1 = epy_block_0_1.blk(one='01', zero='00')
        self.epy_block_0 = epy_block_0.blk(sps=sps, carier=carrier, samp_rate=samp_rate)
        self.blocks_vector_source_x_0 = blocks.vector_source_b(list( ord(i) for i in 'Alireza KH...'), True, 1, [])
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'E:\\my.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.block__power_0_0 = block__power(
            num_taps=sps-1,
        )
        self.block__power_0 = block__power(
            num_taps=sps-1,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.block__power_0, 0), (self.epy_block_3, 0))
        self.connect((self.block__power_0_0, 0), (self.epy_block_3, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.epy_block_0, 0), (self.interp_fir_filter_xxx_1, 0))
        self.connect((self.epy_block_0, 0), (self.interp_fir_filter_xxx_1_0, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.epy_block_0_1, 0), (self.epy_block_2, 0))
        self.connect((self.epy_block_1, 0), (self.epy_block_4, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_time_sink_x_1_0, 2))
        self.connect((self.epy_block_2, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.epy_block_2_1, 0), (self.epy_block_5, 0))
        self.connect((self.epy_block_3, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_3, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.epy_block_3, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.epy_block_4, 0), (self.epy_block_2_1, 0))
        self.connect((self.epy_block_5, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.epy_block_5, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.epy_block_1, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.block__power_0, 0))
        self.connect((self.interp_fir_filter_xxx_1_0, 0), (self.block__power_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_e2(sum([np.power(np.cos(2 * np.pi * (float(self.carrier) + self.deltaF) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_e1(sum([np.power(np.cos(2 * np.pi * float(self.carrier) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_deltaF(self.samp_rate/(self.sps))
        self.interp_fir_filter_xxx_1_0.set_taps(([np.cos(2 * np.pi  * (float(self.carrier)+ self.deltaF) * float(i) /float(self.samp_rate) )/self.e2  for i in range(self.sps)]))
        self.interp_fir_filter_xxx_1.set_taps(([np.cos(2 * np.pi  * float(self.carrier) * float(i) /float(self.samp_rate))/self.e1 for i in range(self.sps)]))
        self.interp_fir_filter_xxx_0.set_taps(([1.0 / float(self.num_idle * (self.sps-1)) for i in range(self.num_idle*(self.sps-1)) ]))
        self.epy_block_4.sps = self.sps
        self.epy_block_2_1.begin = self.sps-1
        self.epy_block_2_1.decim = self.sps
        self.epy_block_1.samp_per_sym = self.sps
        self.epy_block_0.sps = self.sps
        self.block__power_0_0.set_num_taps(self.sps-1)
        self.block__power_0.set_num_taps(self.sps-1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_e2(sum([np.power(np.cos(2 * np.pi * (float(self.carrier) + self.deltaF) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_e1(sum([np.power(np.cos(2 * np.pi * float(self.carrier) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_deltaF(self.samp_rate/(self.sps))
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.interp_fir_filter_xxx_1_0.set_taps(([np.cos(2 * np.pi  * (float(self.carrier)+ self.deltaF) * float(i) /float(self.samp_rate) )/self.e2  for i in range(self.sps)]))
        self.interp_fir_filter_xxx_1.set_taps(([np.cos(2 * np.pi  * float(self.carrier) * float(i) /float(self.samp_rate))/self.e1 for i in range(self.sps)]))

    def get_deltaF(self):
        return self.deltaF

    def set_deltaF(self, deltaF):
        self.deltaF = deltaF
        self.set_e2(sum([np.power(np.cos(2 * np.pi * (float(self.carrier) + self.deltaF) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_carrier(self.deltaF)
        self.interp_fir_filter_xxx_1_0.set_taps(([np.cos(2 * np.pi  * (float(self.carrier)+ self.deltaF) * float(i) /float(self.samp_rate) )/self.e2  for i in range(self.sps)]))

    def get_carrier(self):
        return self.carrier

    def set_carrier(self, carrier):
        self.carrier = carrier
        self.set_e2(sum([np.power(np.cos(2 * np.pi * (float(self.carrier) + self.deltaF) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.set_e1(sum([np.power(np.cos(2 * np.pi * float(self.carrier) * float(i) / float(self.samp_rate)), 2) for i in range(self.sps)]))
        self.interp_fir_filter_xxx_1_0.set_taps(([np.cos(2 * np.pi  * (float(self.carrier)+ self.deltaF) * float(i) /float(self.samp_rate) )/self.e2  for i in range(self.sps)]))
        self.interp_fir_filter_xxx_1.set_taps(([np.cos(2 * np.pi  * float(self.carrier) * float(i) /float(self.samp_rate))/self.e1 for i in range(self.sps)]))

    def get_num_idle(self):
        return self.num_idle

    def set_num_idle(self, num_idle):
        self.num_idle = num_idle
        self.interp_fir_filter_xxx_0.set_taps(([1.0 / float(self.num_idle * (self.sps-1)) for i in range(self.num_idle*(self.sps-1)) ]))
        self.epy_block_4.len_packet = self.len_data + self.num_idle
        self.epy_block_4.num_idle = self.num_idle
        self.epy_block_2.num_packed = self.len_data + self.num_idle
        self.epy_block_1.len_packet = self.len_data + self.num_idle
        self.epy_block_1.num_idle = self.num_idle

    def get_len_data(self):
        return self.len_data

    def set_len_data(self, len_data):
        self.len_data = len_data
        self.epy_block_4.len_packet = self.len_data + self.num_idle
        self.epy_block_2.num_packed = self.len_data + self.num_idle
        self.epy_block_1.len_packet = self.len_data + self.num_idle

    def get_e2(self):
        return self.e2

    def set_e2(self, e2):
        self.e2 = e2
        self.interp_fir_filter_xxx_1_0.set_taps(([np.cos(2 * np.pi  * (float(self.carrier)+ self.deltaF) * float(i) /float(self.samp_rate) )/self.e2  for i in range(self.sps)]))

    def get_e1(self):
        return self.e1

    def set_e1(self, e1):
        self.e1 = e1
        self.interp_fir_filter_xxx_1.set_taps(([np.cos(2 * np.pi  * float(self.carrier) * float(i) /float(self.samp_rate))/self.e1 for i in range(self.sps)]))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
