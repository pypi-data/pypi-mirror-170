import os
import importlib
import re
import shutil
import sys
import siliconcompiler


####################################################################
# Make Docs
####################################################################

def make_docs():
    '''
    Vivado is an FPGA programming tool suite from Xilinx used to
    program Xilinx devices.

    Documentation: https://www.xilinx.com/products/design-tools/vivado.html

    '''

    chip = siliconcompiler.Chip('<design>')
    chip.set('arg','step', 'compile')
    chip.set('arg','index', '<index>')
    setup(chip)
    return chip


################################
# Setup Tool (pre executable)
################################

def setup(chip, mode='batch'):
    '''
    '''

    # default tool settings, note, not additive!
    tool = 'vivado'
    vendor = 'xilinx'
    refdir = 'tools/'+tool
    script = 'compile.tcl'
    step = chip.get('arg','step')
    index = chip.get('arg','index')

    clobber = True

    if mode == 'batch':
        clobber = True
        script = '/compile.tcl'
        option = "-mode batch -source"

    # General settings
    chip.set('tool', tool, 'exe', tool, clobber=clobber)
    chip.set('tool', tool, 'vendor', vendor, clobber=clobber)
    chip.set('tool', tool, 'vswitch', '-version', clobber=clobber)
    chip.set('tool', tool, 'version', '0', clobber=clobber)
    chip.set('tool', tool, 'refdir', step, index, refdir, clobber=clobber)
    chip.set('tool', tool, 'script', step, index, script, clobber=clobber)
    chip.set('tool', tool, 'threads', step, index, os.cpu_count(), clobber=clobber)
    chip.set('tool', tool, 'option', step, index, option, clobber=clobber)
