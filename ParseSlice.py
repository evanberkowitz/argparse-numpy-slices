#!/usr/bin/env python3

# BSD 3-Clause License
# 
# Copyright (c) 2022, Evan Berkowitz
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse

class ParseSlice(argparse.Action):

    def __call__(self, parser, namespace, values, options_string=None):

        if len(values) == 1 and ':' in values[0]:
            s = slice(*[int(s) if s else None for s in values[0].split(":")])

        else:
            split_commas = [val for d in values for val in d.split(',') if val != '']
            s = [int(''.join([digit for digit in d if digit.isdigit()])) for d in split_commas]

        setattr(namespace, self.dest, s)


if __name__ == '__main__':
    import sys
    import numpy as np

    parser = argparse.ArgumentParser()
    parser.add_argument('--slice', nargs='*', action=ParseSlice)

    x = np.arange(0,10)
    
    default_formats = [
                '--slice 1:6',
                '--slice 1 2 3 4 5',
                '--slice [1 2 3 4 5]',
                '--slice 1,2,3,4,5',
                '--slice [1,2,3 4,5]',
                '--slice :5:1',
                '--slice :5',
                '--slice 5:',
                '--slice ::2',
                '--slice 1::2',
                '--slice :-1:2',
                '--slice=-1:-6:-1', # to get a leading minus sign you need the =
                ]
    longest = max([len(f) for f in default_formats])

    if(len(sys.argv) > 1):
        # Parse user-provided example
        formats = [
                ' '.join(sys.argv[1:])
                ]
        longest = max(longest, max([len(f) for f in formats]))
    else:
        # Give some example input / output pairs
        formats = default_formats


    print(f"The array we are slicing into is\n    {x}\n")
    for a in formats:
        args = parser.parse_args(a.split())
        print(f"{a:{longest+4}} {x[args.slice]}")
