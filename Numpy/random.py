import numpy as np

rng = np.random.default_rng(seed = 1)

print(rng.integers(low= 1, high = 101, size=(3, 2)))