from cherimoya.generators import float_generator, complex_generator

DEBUG = False

AARTFAAC_HOST = 'localhost'
AARTFAAC_PORT = 9999

GRAPHITE_HOST = 'localhost'
GRAPHITE_PORT = 2003

FIELD_TYPES = {}

num = 28
min_ = 5.47897e+07
max_ = 5.48721e+07
for i in [x * ((max_ - min_)/num) + min_ for x in range(num)]:
    FIELD_TYPES['GAINS_%s' % i] = 288 * [complex_generator(0, 2.)]
    FIELD_TYPES['MAJORRESIDUES_%s' % i] = [float_generator(0.00010016,
                                                           9.9978e-06)]
    FIELD_TYPES['MINORRESIDUES_%s' % i] = [float_generator(1.0001e-07,
                                                           9.9935e-07)]

FIELD_TYPES['FLAGGER_13'] = [float_generator(0.015312, 0.015909)]
FIELD_TYPES['FLAGGER_20'] = [float_generator(0.015312, 0.015909)]
FIELD_TYPES['FLAGGER_250'] = [float_generator(0.0036337, 0.0040518)]
FIELD_TYPES['CHUNKS'] = [float_generator(0.27618, 0.28096)]
FIELD_TYPES['FNORM'] = [float_generator(15.952, 57.914)]
FIELD_TYPES['FRINGE_AMPLITUDE'] = [float_generator(0.00071085, 0.015806)]
FIELD_TYPES['FRINGE_PHASE'] = [float_generator(-3.1305, 3.1305)]



