# NumberSystem

## More consistent number system

## Section 1: Definitions

We define the following operators on the set of digits (any base is fine, we use 10 hereafter):
 - Left t: `ty = -y` where `y` is a single digit. This operator is not applied unless it
 is the leftmost character or preceeded by an `a`.
 - Right t: `xt = 10 * x`
 - Binary a: `xay = x^(-y)`
 - Unary a: `ay = -(y)`.
These are in order of precedence.

We pronounce `a` anti and `t` as tee (like ty in twenty).

The binary `a` is right associative.
A right `t` followed by a digit `ytx` is interpreted as `y * 10 + x`.
Consecutive digits imply summation of the two component numbers.
`t` is usually the right `t`. It is the left `t` it is either the leftmost
character or has an `a` to the right.

We belive the above is enough to define:
 - `x aa y = x ^ y` (we treat the right `a` as unary and the left one as binary).
 - `x ta y = (10 x) ^ -y`
 - `x taa y = (10 x) ^ y`.

## Section 11: Examples

`11 = 2` since the adjacent `1` digits add.

`95a15a15a15a1 = 9.8` since the 4 `5a1`s add to give 4/5 = 8/10.

`1tt2t1aa2a1= 11` (we mean eleven) since the rightmost `a` gives 1/2,
then the `aa` gives `1tt2t1` to the 1/2 (so square root of `1tt2t1`),
and `1tt2t1` is 11 since all the `t`s are right `t`s.

`2aa2a1 = sqrt(2)` since `2a1` is a half so we have the square root of 2.

So now, we note that algebraic real numbers are probably all expressible in this.
By we've yet to use the left `t`...

`t1a2a1 = i` (yes, the imaginary unit), since the left `t` negates the 1 and
we take its square root.

So far, we probably get Q[i], the complex numbers with rational coefficients.
But now:

`2at1a2a1 = 2^i = cos(ln(2)) + i sin(ln(2))` which we're not so sure about...
