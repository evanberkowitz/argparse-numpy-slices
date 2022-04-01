# argparse-numpy-slices

Sometimes we need to parse slices to extract subarrays.

This utility helps a user of python's [argparse](https://docs.python.org/3/library/argparse.html) parse a variety of formats for expressing which indices to take.

As shown in `example.py` you can default to include everything or nothing by default, via
```python
import argparse
import ParseSlice
parser = argparse.ArgumentParser()
# Explicit approach
parser.add_argument('--default-to-everything', nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Everything)
parser.add_argument('--default-to-nothing',    nargs='*', action=ParseSlice.ParseSlice, default=ParseSlice.Nothing   )
# With sugar
parser.add_argument('--star-star-everything', **ParseSlice.SliceEverything)
parser.add_argument('--star-star-nothing',    **ParseSlice.SliceNothing)
parser.add_argument('--star-star-default',    **ParseSlice.SliceWithDefault([2, 3, 5, 7]))
```
When adding an argument that should be parsed as a slice, it is crucial `nargs='*'` and the slicing happens via the [`action`](https://docs.python.org/3/library/argparse.html#action) option.  Only then can the parsing happen to the whole slice specification as one object, rather than piece-by-piece.

To make specifying `nargs`, `action` and a `default` simple, the simple syntactic sugar `**SliceEverything`, `**SliceNothing` and `**SliceWithDefault(your_default)` are provided that can be used with `**kwarg` unpacking, as shown.  *Using this sugar is the _strongly_ suggested approach!*

If the user passes an argument with a colon, such as `2::2` they will receive a `slice` object.

If the user passes just a list of values, perhaps surrounded by `[square brackets]`, perhaps `comma,separated`, they will get a single list of integers with those values.

Both possibilities can be used as indices for numpy arrays, while traditional python lists and tuples can only accept `slice` objects.

`ParseSlice.py` can be copied/pasted into your project, as long as you follow the BSD 3-Clause License.

You can evaluate `python3 ParseSlice.py` or just `./ParseSlice`.  If you pass no arguments you will see some understood formats and their results for `np.arange(0,10)`.  If you pass a `--slice` argument the result will be your slice specification evaluated for that same numpy array.
