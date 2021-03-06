from cmath import exp
from cmath import pi

def fft_recursive(T):
    A = [x.conjugate() for x in T]
    n=len(A)
    if n==1:
        return(A)
    wn=exp(2*pi*1j/n)
    w=1
    A0=[A[2*k] for k in range(0,n//2)]
    A1=[A[2*k+1] for k in range(0,n//2)]
    Y0=fft_recursive(A0)
    Y1=fft_recursive(A1)
    Y=[0 for i in range(n)]
    for k in range(0,n//2):
        Y[k]=Y0[k]+w*Y1[k]
        Y[k+n//2]=Y0[k]-w*Y1[k]
        w=w*wn
    return(Y)
    

def fft_inverse(B):
    n=len(B)
    return([fft_recursive(B)[i]/n for i in range(len(B))]) 
