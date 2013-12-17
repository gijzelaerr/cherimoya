from cherimoya.generators import float_generator, int_generator
from cherimoya.generators import str_generator, complex_generator

AARTFAAC_HOST = 'localhost'
AARTFAAC_PORT = 9999

GRAPHITE_HOST = 'localhost'
GRAPHITE_PORT = 2003

FIELD_TYPES = {
    'SIMUL_SINGLE_FLOAT': [float_generator(10, 100)],
    'SIMUL_MULTI_FLOAT': 3 * [float_generator(10, 100)],
    'SIMUL_INT': 3 * [int_generator(0, 100)],
    'SIMUL_STRING': [str_generator(["LBA0", "LBA1", "HBA_SPLIT"])],
    'SIMUL_COMPLEX': 4 * [complex_generator(-0.5, 0.5)],
}

for i in range(200):
    FIELD_TYPES['SIMUL_GAIN_%s' % i] = 4 * [complex_generator(-0.5, 0.5)]
