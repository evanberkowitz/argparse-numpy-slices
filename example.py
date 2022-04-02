#!/usr/bin/env python

import argparse
import ParseSlice
import numpy as np

parser = argparse.ArgumentParser()

# Explicit approach
parser.add_argument('--default-to-everything', nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Everything)
parser.add_argument('--default-to-nothing',    nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Nothing   )
# With sugar
parser.add_argument('--star-star-everything', **ParseSlice.SliceEverything)
parser.add_argument('--star-star-nothing',    **ParseSlice.SliceNothing)
parser.add_argument('--star-star-default',    **ParseSlice.SliceWithDefault([2, 3, 5, 7]))
parser.add_argument('--star-star-evens',      **ParseSlice.SliceWithDefault(slice(0,None,2)))

args = parser.parse_args()

x = np.arange(10)

print(f"       numpy array is: {x}")
print(f"Default to everything: {x[args.default_to_everything]}")
print(f"Default to    nothing: {x[args.default_to_nothing]}")
print(f"Star star  everything: {x[args.star_star_everything]}")
print(f"Star star     nothing: {x[args.star_star_nothing]}")
print(f"Star star     default: {x[args.star_star_default]}")
print(f"Star star       evens: {x[args.star_star_evens]}")
