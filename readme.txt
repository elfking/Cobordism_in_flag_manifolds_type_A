This repository computes the Bott-Samelson classes of the equivariant
cobordism ring of the flag manifold G/B for type A (i.e. G = GL(n)). 

Note we are denoting the polynomials by its dual class, so there is a
reversion of indices. 

Basically up to now we are able to make SAGE do formal manipulations in the
symbolic ring to give us certain simplified expressions, and have not incorporated
some properties of the cobordism ring, such as f(x)=f(y) for f in C[X]^W. 
This suffices in certain cases, however.

The most complete version of code up to date is in "Tangent Law in Type A3.py"
