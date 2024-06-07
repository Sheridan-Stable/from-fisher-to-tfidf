from utils import *

#Thm1 small
print(f"Thm 1; n=1000\n{'-'*13}")
n=1000
ni=150
bi=4
nj=100
nij=25
d=20
display_stats(nij, ni, nj, n, bi, d)
#######
#Thm1 large
print(f"Thm 1; n=10000\n{'-'*13}")
n=10000
ni=200
bi=20
nj=75
nij=15
d=75
display_stats(nij, ni, nj, n, bi, d)
#######
#Cor1 small
print(f"Cor 1; n=1000\n{'-'*13}")
n=1000
ni=100
bi=10
nj=25
nij=10
d=40
display_stats(nij, ni, nj, n, bi, d)
#######
#Cor1 large
print(f"Cor 1; n=10000\n{'-'*13}")
n=10000
ni=200
bi=8
nj=100
nij=25
d=100
display_stats(nij, ni, nj, n, bi, d)
#######
#Cor2 small
print(f"Cor 2; n=1000\n{'-'*13}")
n=1000
ni=160
bi=8
nj=20
nij=20
d=50
display_stats(nij, ni,nj,n,bi,d)
#######
#Cor2 large
print(f"Cor 2; n=10000\n{'-'*13}")
n=10000
ni=1200
bi=15
nj=80
nij=80
d=125
display_stats(nij, ni, nj, n, bi, d)



