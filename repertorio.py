# -*- coding: utf-8 -*-

class Vetor(object):
    #==========================================================================
    # Construtor e métodos de representação
    #========================================================================== 
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def __repr__(self):
        return 'Vetor(%r, %r, %r)' % tuple(self)
        
    def __str__(self):
        return 'Vetor(%s, %s, %s)' % tuple(self)
    
    #==========================================================================
    # Funções especiais
    #==========================================================================    
    def __abs__(self):
        return self.quadnorma()**0.5
        
    def __nonzero__(self):
        return any(self)

    #==========================================================================
    # Operações aritméticas
    #==========================================================================
    def __pos__(self):
        return Vetor(self.x, self.y, self.z)
        
    def __neg__(self):
        return Vetor(-self.x, -self.y, -self.z)
        
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y, self.z + outro.z)
        
    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y, self.z - outro.z)
        
    def __mul__(self, outro):
        try:
            self.escalar(outro)
        except AttributeError:
            return Vetor(self.x * outro, self.y * outro, self.z * outro)
            
    def __pow__(self, k):
        if k <= 0:
            raise ValueError('Exponenciação de vetores somente definida para expoentes inteiros positivos')
        else:
            v = Vetor(self.x, self.y, self.z)
            for i in range(k):
                v = v * self
            return v
            
    __rmul__ = __mul__
            
    def __div__(self, k):
        return Vetor(self.x / k, self.y / k, self.z / k)
        
    def __iadd__(self, outro):
        self.x += outro.x
        self.y += outro.y
        self.z += outro.z
        return self
        
    def __isub__(self, outro):
        self.x -= outro.x
        self.y -= outro.y
        self.z -= outro.z
        return self
        
    def __imul__(self, k):
        self.x *= k
        self.y *= k
        self.z *= k
        return self
        
    def __idiv__(self, k):
        self.x /= k
        self.y /= k
        self.z /= k
        return self

    #==========================================================================
    # Operações lógicas
    #==========================================================================
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y and self.z == outro.z
        
    def __ne__(self, outro):
        return not self == outro

    #==========================================================================
    # Acesso a elementos
    #==========================================================================
    def __getitem__(self, i):
        if i in [0, -3]:
            return self.x
        elif i in [1, -2]:
            return self.y
        elif i in [2, -1]:
            return self.z
        else:
            raise ValueError('Índice fora dos limites')
            
    def __setitem__(self, i, value):
        if i in [0, -3]:
            self.x = float(value)
        elif i in [1, -2]:
            self.y = float(value)
        elif i in [2, -1]:
            self.z = float(value)
        else:
            raise ValueError('Índice fora dos limites')

    #==========================================================================
    # Protocolos
    #==========================================================================
    def __iter__(self):
        return iter([self.x, self.y, self.z])
        
    def __len__(self):
        return 3
        
    def __reversed__(self):
        return Vetor(self.z, self.y, self.x)
        
    def escalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z
    
    def projetar(self, outro):
        if outro==Vetor(0,0):
            return 0
        else:
            return (self.escalar(outro)/outro.escalar(outro))*outro
        
    #==========================================================================
    # Protocolos
    #==========================================================================
    norma = __abs__        
        
    def normalizado(self):
        """Retorna uma cópia de módulo unitário deste vetor"""
        return self / abs(self)
        
    def normalizar(self):
        """Altera as componentes deste vetor para tornar o módulo unitário"""
        self /= abs(self)
        
    def quadnorma(self):
        """Calcula o quadrado do módulo (norma euclideana)"""
        return self.x**2 + self.y**2 + self.z**2
        
    def vetorial(self, outro):
        """Calcula e retorna o produto vetorial self x outro"""
        return Vetor(
            self.y * outro.z - outro.y * self.z,
            self.z * outro.x - outro.z * self.x,
            self.x * outro.y - outro.x * self.y,
        )
