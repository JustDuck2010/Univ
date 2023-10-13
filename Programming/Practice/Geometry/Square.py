def sq_sq(a):
    return(a**2)
def sq_rec(a,b):
    return(a*b)
def sq_tr(b,h):
    return(b*h/2)
def main():
    print(sq_sq(5))
    print(sq_rec(5,2))
    print(sq_tr(5,10))

if __name__ == '__main__':
    main()