"""
定义逻辑门，类的继承
"""

# 超类
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    

# BinaryGate类
class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        # return int(input("Enter Pin A input for gate " + \
        #                  self.getLabel() + "-->"))

        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getName() + "-->") 
        else:
            return self.pinA.getFrom().getOutput()


    def getPinB(self):
        return int(input("Enter Pin B input for gate " + \
                         self.getLabel() + "-->"))


# UnaryGate类
class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None
    
    def getPin(self):
        return int(input("Enter Pin input for gate " + \
                         self.getLabel() + "-->"))


# AndGate类
class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

# OrGate类
class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


# NorGate类
class NotGate(UnaryGate):
    
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        a = self.getPin()

        if a == 1:
            return 0
        else:
            return 1


# test
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
print(g1.getOutput())
print(g2.getOutput())
print(g3.getOutput())
print(g4.getOutput())



