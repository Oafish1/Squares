# Squares: A Counter-Based Random Number Generator

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Oafish1/Squares/Build%20and%20Test?label=tests&style=plastic)

This library is an implementation of [arXiv:2004.06278](https://arxiv.org/abs/2004.06278) adapted for any number of bits.  Keep in mind that the original implementation was designed for 64 bit numbers while this implementation uses a default of 32.

The generation algorithm is **NOT MY WORK**.  For the paper on which this utility is based, please look [here](https://arxiv.org/abs/2004.06278).

### Usage

The package can be installed with
```bash
pip install squares-rng
```

After installing, the generator can be used with
```bash
from squares import squares

rng = squares()
next(rng) # Returns 32-bit uint
```

The generator can be seeded
```bash
rng = squares(seed=42)
next(rng) # 4161798144
```

If you are struggling to decide on a seed to use for reproducible testing, one can be generated from the computer's internal clock
```bash
from squares import get_suitable_seed

seed = get_suitable_seed()
```

This function is used in the case that no seed is provided to the generator.

`get_suitable_seed` has no bit restrictions.  If a seed containing too many bits is passed to the generator, it will be truncated and a warning will be shown.

For small seeds, the `safety` parameter should be left as `True`
```bash
rng = squares(seed=42, safety=False)
next(rng) # 0
next(rng) # 115605504
```

`safety` is a proprietary method to allow for smaller keys, iterating the generator until the seed has a non-zero maximal bit.  Due to the nature of the algorithm, smaller keys would otherwise result in much smaller numbers for the first few iterations.  With `safety=True`, keep in mind that the first generation will take longer than subsequent calls.

The maximal bits of the generated number can also be set
```bash
rng = squares(seed=84, bits=64)
next(rng) # 9267630197371305984
```

The default is `bits=32` for maximal python compatibility.  Keep in mind that this does not automatically influence the internal calculation except where necessary.  Some internal calculations may involve more than the specified number of bits if python allows it.  However, the generated integer will not exceed the requested bits.

Lastly, a truncation utility is included
```bash
from squares import truncate

truncate(6798039809, 32) # 2503072513
```

The truncation utility defaults to truncating the higher bits, but can be configured to preserve them instead
```bash
truncate(698320, 16, right_shift=True) # 43645
```

# Original Paper

[Widynski, *arXiv:2004.06278*](https://arxiv.org/abs/2004.06278)
