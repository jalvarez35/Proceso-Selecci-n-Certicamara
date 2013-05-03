import unittest

def karatsuba(x,y):
    if x<0 or y<0:
        return "Error"
    
    xx=str(x) 
    yy=str(y)
    if len(xx)!= len(yy):
        return "Error"
    
    m=len(xx)
    if m not in [1,2,4,8,16,32,64,128,256,512,1024,2048]:
        return "Error"
    
    n=m/2
    if n==0:
        return x*y
    a=int(xx[:n])
    b=int(xx[n:])
    c=int(yy[:n]) 
    d=int(yy[n:])
    z0=karatsuba(a,c)
    z1=karatsuba(a,d)
    z2=karatsuba(b,c)
    z3=karatsuba(b,d)
    resultado=(10**m)*z0 + (10**n)*(z1+z2)+ z3
    return resultado

class KaratsubaTest (unittest.TestCase):

    def test_Karatsuba(self):
        self.assertEqual(12345633*56789066, karatsuba(12345633, 56789066))

    def test_negative(self):
        self.assertEqual("Error", karatsuba(-1,-1))

    def test_longitud1(self):
        self.assertEqual(2*3, karatsuba(2, 3))

    def test_longitud_no_potencia_de_2(self):
        self.assertEqual("Error", karatsuba(123456,456789))

    def test_longitud_diferente(self):
        self.assertEqual("Error", karatsuba(1234,56789098))
        
if __name__ == '__main__':
    unittest.main()
