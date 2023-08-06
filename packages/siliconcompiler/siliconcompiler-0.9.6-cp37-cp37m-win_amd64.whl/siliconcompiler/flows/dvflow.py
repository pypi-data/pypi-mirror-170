import os
import re
import siliconcompiler

############################################################################
# DOCS
############################################################################

def make_docs():
    '''
    A configurable constrained random stimulus DV flow.

    The verification pipeline includes the followins teps:

    * **import**: Sources are collected and packaged for compilation
    * **compile**: RTL sources are compiled into object form (once)
    * **testgen**: A random seed is used to generate a unique test
    * **refsim**: A golden trace of test is generated using a reference sim.
    * **sim**: Compiled RTL is exercised using generated test
    * **compare**: The outputs of the sim and refsim are compared
    * **signoff**: Parallel verification pipelines are merged and checked

    The dvflow can be parametrized using a single 'np' flowarg parameter.
    Setting 'np' > 1 results in multiple independent verificaiton
    pipelines to be launched.

    '''

    chip = siliconcompiler.Chip('<topmodule>')
    chip.set('option', 'flow', 'dvflow')
    setup(chip)

    return chip

#############################################################################
# Flowgraph Setup
#############################################################################
def setup(chip, flow='dflow'):
    '''
    Setup function for 'dvflow'
    '''

    # Definting a flow
    flow = 'dvflow'

    # A simple linear flow
    flowpipe = ['import',
                'compile',
                'testgen',
                'refsim',
                'sim',
                'compare',
                'signoff']

    tools = {
        'import': 'verilator',
        'compile': 'verilator',
        'testgen': 'verilator',
        'refsim': 'verilator',
        'sim': 'verilator',
        'compare': 'verilator',
        'signoff': 'verify'
    }


    # Parallelism
    if 'np' in chip.getkeys('arg', 'flow'):
        np = int(chip.get('arg', 'flow', 'np')[0])
    else:
        np = 1

    # Setting mode as 'sim'
    chip.set('option', 'mode', 'sim')

    # Flow setup
    for step in flowpipe:
        #start
        if step == 'import':
            chip.set('flowgraph', flow, step, '0', 'tool', tools[step])
        #serial
        elif step == 'compile':
            chip.set('flowgraph', flow, step, '0', 'tool', tools[step])
            chip.set('flowgraph', flow, step, '0', 'input', ('import', '0'))
        #fork
        elif step == 'testgen':
            for index in range(np):
                chip.set('flowgraph', flow, step, str(index), 'tool', tools[step])
                chip.set('flowgraph', flow, step, str(index), 'input', ('compile', '0'))
        #join
        elif step == 'signoff':
            chip.set('flowgraph', flow, step, '0', 'tool', tools[step])
            for index in range(np):
                chip.add('flowgraph', flow, step, '0', 'input', (prevstep, str(index)))
        else:
            for index in range(np):
                chip.set('flowgraph', flow, step, str(index), 'tool', tools[step])
                chip.set('flowgraph', flow, step, str(index), 'input', (prevstep, str(index)))

        prevstep = step

##################################################
if __name__ == "__main__":
    chip = make_docs()
    chip.write_flowgraph("dvflow.png")
