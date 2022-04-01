# argparse-numpy-slices

Sometimes we need to parse slices to extract subarrays.

This utility helps a user of python's [argparse](https://docs.python.org/3/library/argparse.html) parse a variety of formats for expressing which indices to take.

You can default to include everything or nothing by default, via
```
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--slice-that-defaults-to-everything', nargs='*', action=ParseSlice, default=Everything)
    parser.add_argument('--slice-that-defaults-to-nothing',    nargs='*', action=ParseSlice, default=Nothing)
```

If the user passes an argument with a colon, such as `2::2` they will receive a `slice` object.

If the user passes just a list of values, perhaps surrounded by `[square brackets]`, perhaps `comma,separated`, they will get a single list of integers with those values.

Both possibilities can be used as indices for numpy arrays, while traditional python lists and tuples can only accept `slice` objects.

`ParseSlice.py` can be copied/pasted into your project, as long as you follow the BSD 3-Clause License.

You can evaluate `python3 ParseSlice.py` or just `./ParseSlice`.  If you pass no arguments you will see some understood formats and their results for `np.arange(0,10)`.  If you pass a `--slice` argument the result will be your slice specification evaluated for that same numpy array.
