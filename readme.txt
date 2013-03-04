\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\                                               \\\
\\\       \\\\\   \\   \\   \\\\   \\     \\      \\\
\\\      \\   \\  \\   \\  \\  \\  \\\   \\\      \\\
\\\      \\       \\\\\\\  \\  \\  \\\\ \\\\      \\\
\\\      \\   \\  \\   \\  \\  \\  \\  \  \\      \\\
\\\       \\\\\   \\   \\   \\\\   \\     \\      \\\
\\\                                               \\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


This repository computes the Bott-Samelson classes of the equivariant
cobordism ring of the flag manifold G/B for type A (i.e. G = GL(n)). 

Note we are denoting the polynomials by its dual class, so there is a
reversion of indices. 

Basically up to now we are able to make SAGE do formal manipulations in the
symbolic ring to give us certain simplified expressions, and have not incorporated
some properties of the cobordism ring, such as f(x)=f(y) for f in C[X]^W. 
This suffices in certain cases, however.

The most complete version of code up to date is in "Tangent Law in Type A3.py"

(Monday, March 4th, 2013) As of now, the correct version of the code is the one
in "reuse". The one given above has been corrected but not tested. The correct output
is the only one that's 3MB. All others are incorrect. This is due to faulty code
in Demazure.

Now that the corrected code is tested, yes  it is correct but much slower than our reuse
code, so YAY! Basically it took more than 1 hour and SAGE shut it down.