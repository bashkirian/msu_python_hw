def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    assert (b == 0)
    if a >= 0:
        return a
    else:
        return (-a)
        
def extEucl(m, n):
    a = m; b = n
    u1 = 1; v1 = 0
    u2 = 0; v2 = 1
    while b != 0:
        q = a // b; r = a%b
        (a, b) = (b, r)
        (u1, u2) = (u2, u1 - q*u2)
        (v1, v2) = (v2, v1 - q*v2)
    if a >= 0:
        return (a, u1, v1)
    else:
        return (-a, -u1, -v1)
        
def invmod(x, m):
    (d, u, v) = extEucl(x, m)
    if d != 1:
        raise ValueError("element is not invertible modulo m")
    return u
    
def powmod(a, n, m):
    if n < 0:
        raise ValueError("Negative exponent")
    # Invariant: a^n * p = const
    p = 1
    while n > 0:
        if n%2 == 0:
            n //= 2; a = (a*a)%m
        else:
            n -= 1; p = (p*a)%m
    return p
