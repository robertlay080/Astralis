
#### main.py

```python
#!/usr/bin/env python3
import random

phenomena = [
    "A massive supernova explosion in a distant galaxy.",
    "A rogue planet drifting through interstellar space.",
    "A neutron star with an unusually powerful magnetic field.",
    "An exoplanet covered entirely in liquid metal oceans.",
    "A black hole that distorts time near its event horizon."
]

def get_random_phenomenon():
    return random.choice(phenomena)

def main():
    print("Welcome to Astralis Astronomical Phenomena!")
    print("Here's a random space phenomenon:")
    print(get_random_phenomenon())

if __name__ == "__main__":
    main()
