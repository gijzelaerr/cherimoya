from cherimoya.generators import float_generator, int_generator
from cherimoya.generators import str_generator, complex_generator

DEBUG = False

AARTFAAC_HOST = 'localhost'
AARTFAAC_PORT = 9999

GRAPHITE_HOST = 'localhost'
GRAPHITE_PORT = 2003

"""
FIELD_TYPES = {
    'SIMUL_SINGLE_FLOAT': [float_generator(10, 100)],
    'SIMUL_MULTI_FLOAT': 3 * [float_generator(10, 100)],
    'SIMUL_INT': 3 * [int_generator(0, 100)],
    #'SIMUL_STRING': [str_generator(["LBA0", "LBA1", "HBA_SPLIT"])],
    'SIMUL_COMPLEX': 4 * [complex_generator(-0.5, 0.5)],
}
"""

FIELD_TYPES = {}

for i in range(20):
    FIELD_TYPES['SIMUL_GAIN_%s' % i] = 288 * [complex_generator(-0.5, 0.5)]
    FIELD_TYPES['SIMUL_MAJORRESIDUES_%s' % i] = [float_generator(0, 0001)]
    FIELD_TYPES['SIMUL_MINORRESIDUES_%s' % i] = [float_generator(0, 0001)]

FIELD_TYPES['SIMUL_FLAGGER_50'] = [float_generator(0, 1)]
FIELD_TYPES['SIMUL_FLAGGER_150'] = [float_generator(0, 1)]
FIELD_TYPES['SIMUL_FLAGGER_250'] = [float_generator(0, 1)]
FIELD_TYPES['SIMUL_CHUNKS'] = [float_generator(0, 1)]
FIELD_TYPES['SIMUL_FNORM'] = [float_generator(0, 20)]
FIELD_TYPES['SIMUL_FRINGE_AMPLITUDE'] = [float_generator(0, 00001)]
FIELD_TYPES['SIMUL_FRINGE_PHASE'] = [float_generator(0, 0.2)]
