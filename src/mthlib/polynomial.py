from itertools import zip_longest

class Polynomial:
    
    def __init__(self, *coeffs):
        """ input: coeffs are in the form a_n, ...a_1, a_0 
        """
        self.coeffs = list(coeffs) 

    def __str__(self):
        res = ""
        degree = len(self.coeffs) - 1
        res += str(self.coeffs[0]) + "x^" + str(degree)
        for i in range(1, len(self.coeffs)-1):
            coeff = self.coeffs[i]
            if coeff < 0:
                res += " - " +  str(-coeff) + "x^" + str(degree - i)
            else:
                res += " + " +  str(coeff) + "x^" + str(degree - i)
                
        if self.coeffs[-1] < 0:
            res += " - " + str(-self.coeffs[-1])
        else:
            res += " + " + str(self.coeffs[-1])

        return res

     
    def __repr__(self):
        
        return "Polynomial" + str(self.coeffs)
            
    def __call__(self, x):    
        res = 0
        for coeff in self.coeffs:
            res = res * x + coeff
        return res 
    
    def degree(self):
        return len(self.coeffs)   
            
    def __add__(self, other):
        c1 = self.coeffs[::-1]
        c2 = other.coeffs[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    
    def __sub__(self, other):
        c1 = self.coeffs[::-1]
        c2 = other.coeffs[::-1]
        
        res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    
    
    