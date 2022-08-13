class Python:
    def _init_(self):
        pass
    def Addition(self,a,b):
        return a+b
    def Sub_a_from_b(self,a,b):
        return a-b
    def sub_b_from_a(self,a,b):
        return b-a
    def Multiplication(self,a,b):
        return a*b
    def Divide_a_from_b(self,a,b):
        return a/b
    def Divide_b_from_a(self,a,b):
        return b/a
    def NOTA(self,a):
        return ~a
    def NOTB(self,b):
        return ~b
    def rem_a_from_b(self,a,b):
        return a%b
    def rem_b_from_a(self,a,b):
        return b%a
    def OR(self,a,b):
        return a|b
    def AND(self,a,b):
        return a&b
    def XOR(self,a,b):
        return a^b
    def power(self,a,b):
        return a**b
    def factorial(self,a):
        if(a<=1):
            return 1
        else:
            return a*self.factorial(a-1)
    def fibonacci(self,a):
        
        if n in [0,1]:
            return n
        else:
            return self.fibonacci(a-1)+self.fibonacci(a-2)

p=Python()
print(p.Addition(7,8))
print(p.factorial(9))
