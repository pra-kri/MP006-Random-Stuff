#from math import sqrt, erf, log, exp
import math

# NOTE: in my functions below, I'll break down the more complex equations
# into smaller chunks and save them as variables a, b, c


def cdf_normal(x):
    """ use the erf() function help build the cumulative dist function """
    return (1.0 + erf(x/ sqrt(2.0))) / 2.0

def d1(S, K, r, sigma, T):
    
    a1 = math.log(S/K) + T*(r + 0.5*sigma**2)
    b1 = sigma * math.sqrt(T)
    c1 = a1/b1
    
    return c1


def d2(S, K, r, sigma, T):
    a2 = math.log(S/K) + T*(r - 0.5*sigma**2)
    b2 = sigma * math.sqrt(T)
    c2 = a2/b2
    
    return c2

def Call(S, K, r, sigma, T):
    """ Call Price """
    a3 = S*cdf_normal(d1(S, K, r, sigma, T))
    b3 = K*math.exp(-r*T)*cdf_normal(d2(S,K,r,sigma,T))
    c3 = a3-b3
    
    return c3

def Put(S, K , r,sigma, T):
    """ Put Price. 
    Using the Call Price function within this, but should probably remove dependency for better code
    """
    temp_call = Call(S, K, r, sigma, T)
    temp_put = K*math.exp(-r*t) - S + temp_call
    
    return temp_put

# TODO: neaten up and make more readable, this is just for practice from reading the Paul Wilmott textbook.