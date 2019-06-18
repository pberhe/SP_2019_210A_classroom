#!/usr/bin/env python

print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

def formatting(t):
    f = "the {:d} numbers are: ".format(len(t))
    f += ", ".join(['{:d}'] * len(t))
    return f.format(*t)

print(formatting((4, 6, 10)))
print(formatting((4, 6, 10, 12, 15)))

integers = (24, 38, 47, 9)
integers_str = str(integers)[1:-1]
print("the first {:d} numbers are: {}".format(len(integers), integers_str))

print(('{:<5}'*len(integers)).format(*integers))

