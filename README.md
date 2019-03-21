# MyKatas
A storage place for some coding Katas I wrote. Good coding practice. 

# Notes
These were tested and working with Python 2.7.15

(default, Nov 28 2018, 22:38:08) 

[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux2

# Roman Numerals and back again
Fun exercise. Used recursion to break the numbers into individual symbols, or take one symbol and add it to the total.

Future enhancements might include some input validation and performance improvements for large numbers. But hopefully you aren't using Roman numerals for numbers over several thousand.

Usage:

```import numberal```

Return an Arabic number:

```numberal.toNum(<Valid Roman Numeral>)```

Return a Roman numeral:

```numberal.toRN(<Positive Integer>) ```

# FizzBuzz
My interpretation of the "FizzBuzz" game. Not something I had heard of before, but I like the concept.

Future enhancements would be doing some input validation for the function calls, and maybe adding a way to remove a defined number and word combination.

Usage:

```import FizzBuzz```

Create a game object:

```fb = FizzBuzz.FBgame()```

Return the result of a play:

```fb.play(<positive integer>) ```

Setup your own phrases:

```fb.setup(divisor = <positive integer>, word = <string>) ```
