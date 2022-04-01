#!/usr/bin/env python

import argparse
import ParseSlice
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('--default-to-everything', nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Everything)
parser.add_argument('--default-to-nothing',    nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Nothing   )

args = parser.parse_args()

x = np.arange(10)

print(f"       numpy array is: {x}")
print(f"Default to everything: {x[args.default_to_everything]}")
print(f"Default to    nothing: {x[args.default_to_nothing]}")
