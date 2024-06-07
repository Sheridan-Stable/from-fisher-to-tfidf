import math
import scipy.stats as stats

def tf_icf(Nij, N, Ni):
    return Nij * math.log(N/Ni)

def tf_idf(Nij, D, Bi):
    return Nij * math.log(D/Bi)

def fisher(Nij, Ni, Nj, N, return_table=False): #H
    """Not used"""
    contingency_table = [[0, 0], [0, 0]]
    contingency_table[0][0] = Nij
    contingency_table[0][1] = Ni -Nij
    contingency_table[1][0] = Nj -Nij
    contingency_table[1][1] = N - Ni - (Nj -Nij)
    try:
        if return_table:
            return stats.fisher_exact(contingency_table, alternative='greater')[1], contingency_table
        return stats.fisher_exact(contingency_table, alternative='greater')[1]
    except:
        print("Error: Check the values again.")
        print(contingency_table)

def H(Nij, Ni, Nj, N):
    return stats.hypergeom.sf(Nij-1, N, Ni, Nj)


def hypergeom_pmf(Nij, Ni, Nj, N): #h
    return math.comb(Ni,Nij) * math.comb(N - Ni, Nj -Nij) / math.comb(N, Nj)


def LogH(Nij, Ni, Nj, N):
    return -math.log(H(Nij, Ni, Nj, N))


def binmomial(Nij, Nj, Pi): #b
    return (math.comb(Nj,Nij)*Pi**Nij)*(1-Pi)**(Nj-Nij)
    

def compute_Qij(Nij, Ni, Nj, N):
    Pi = Ni/N
    return H(Nij+1, Ni, Nj, N)/binmomial(Nij, Nj, Pi)



def eq8(Nij, Ni, Nj, N):
    tficf = tf_icf(Nij, N, Ni)
    Pij = Nij/Nj
    Pi = Ni/N
    Qij = compute_Qij(Nij, Ni, Nj, N)
    return tficf +Nij*math.log(Pij) + (Nj -Nij)*(Pi - Pij) - Qij

def eq11( r, Ni, Nj, N, Bi, D):
    """
   Nij = r
    nil = rBil; l != j
    """
    tfidf = tf_idf(r, D, Bi)
    Pi = Ni/N
    Pij = r/Nj
    return tfidf - r*(1-Bi/D)*(1-Pij) - compute_Qij(r, Ni, Nj, N)


def temp( r, Ni, Nj, N, Bi, D):
    """
   Nij = r
    nil = rBil; l != j
    """
    tfidf = tf_idf(r, D, Bi)
    Pi = Ni/N
    return tfidf - r*( (Bi/D) * (1-Pi) - 1 + r/D ) - compute_Qij(r, Ni, Nj, N)
    

def display_stats(Nij, Ni, Nj, N, Bi, D):
    Pi = Ni/N
    Pij = Nij/Nj
    
    print(f'Nij={Nij}\tNi={Ni}\tNj={Nj}\tN={N}\t\nBi={Bi}\tD={D}\tPi={Pi}\tPij={Pij}\n\nEq3: {LogH(Nij, Ni, Nj, N):.4f}\nEq8: {eq8(Nij, Ni, Nj, N):.4f}\nEq11: {eq11(Nij, Ni, Nj, N, Bi, D):.4f}\nEq12: {tf_idf(Nij, D, Bi):.4f}\n{"-"*13}\n')
