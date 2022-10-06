NICKNAME = "Goshaan4k"
from cmath import sqrt as c_sqrt
import decimal as dec

def solve_quad(b, c):

    d = dec.Decimal(str(b))*dec.Decimal(str(b))-dec.Decimal(str(4*c))
    if d < 0:
        d = c_sqrt(d)
        x1 = (-b - d)/2
        x2 = (-b + d)/2
    else:
        d = d.sqrt()
        x1 = (dec.Decimal(str(-1*b)) - d)/dec.Decimal(2)
        x2 = (dec.Decimal(str(-1*b)) + d)/dec.Decimal(2)
    x1 = complex(x1)
    x2 = complex(x2)
    return(x1, x2)

    raise NotImplementedError()

from numpy.testing import assert_allclose

variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
           ]

for var in variants:
    x1, x2 = solve_quad(**var)
    assert_allclose(x1*x2, var['c'], rtol=1e-15)
