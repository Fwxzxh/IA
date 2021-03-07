from itertools import*

def f(n):
    s=range(n);l=len
    for r in permutations(product(s,s)):
        if all([l({x[0]for x in r[i*n:-~i*n]})*l({x[1]for x in r[i*n:-~i*n]})*l({r[j*n+i][0]for j in s})*l({r[j*n+i][1]for j in s})==n**4for i in s]):return r

if __name__ == "__main__":
    print(f(3))
