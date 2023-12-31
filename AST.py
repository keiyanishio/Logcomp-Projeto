from FuncTable import *
from SymbolTable import *

FT = FuncTable()

class Node:
    def __init__(self, value, children):
        self.value = value 
        self.children = children
        

    def evaluate(self, ST):
        pass
    
class BinOp(Node):
    def evaluate(self, ST):
        
        left = self.children[0].evaluate(ST)
        right = self.children[1].evaluate(ST)
        # print(left, right)
        
        
        if self.value == "+":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP +")
            return (left[0] + right[0], "bar")
        
        elif self.value == "-":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP -")
            return (left[0] - right[0], "bar")
        
        elif self.value == "*":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP *")
            return (left[0] * right[0], "bar")
        
        elif self.value == "/":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP /")
            return (left[0] // right[0], "bar")
        
        elif self.value == "&&":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP &&")
            return (int(left[0] and right[0]), "bar")
        
        elif self.value == "||":
            if left[1] != right[1] or left[1] != "bar":
                raise SyntaxError("ERRO BINOP ||")
            return (int(left[0] or right[0]), "bar")
        
        elif self.value == "<":
            return (int(left[0] < right[0]), "bar")
        
        elif self.value == ">":
            return (int(left[0] > right[0]), "bar")
        
        elif self.value == "==":
            if left[1] != right[1]:
                raise SyntaxError("ERRO BINOP ==")
            return (int(left[0] == right[0]), "bar")
        
        elif self.value == ".":
            return (str(left[0]) + str(right[0]), "verse")


class UnOp(Node):
    def evaluate(self, ST):
        if self.value == "+":
            return (self.children[0].evaluate(ST)[0], "bar")
        elif self.value == "!":
            return (not self.children[0].evaluate(ST)[0], "bar")
        else:
            return (-self.children[0].evaluate(ST)[0], "bar")
        
class IntVal(Node):
    def evaluate(self, ST):
        return (int(self.value), "bar")

class NoOp(Node):
    def evaluate(self, ST):
        pass
    
##########################################################################
class Assigment(Node):
    def evaluate(self, ST):
        ST.setter(self.children[0].value, self.children[1].evaluate(ST))
    
    
class Identifier(Node):
    def evaluate(self, ST):
        return ST.getter(self.value)
            
            

class Block(Node):
    def evaluate(self, ST):
        for child in self.children:
            if isinstance(child, ReturnNode):
                return child.evaluate(ST)
            child.evaluate(ST)
            
class Print(Node):
    def evaluate(self, ST):
        print(self.children[0].evaluate(ST)[0])
    
########################################################################
class Scan(Node):
    def evaluate(self, ST):
        return (int(input()), "bar")


class ForLoop(Node):
    def evaluate(self, ST):
        self.children[0].evaluate(ST)
        while self.children[1].evaluate(ST)[0]:
            self.children[3].evaluate(ST)
            self.children[2].evaluate(ST)
            
class IfCond(Node):
    def evaluate(self, ST):
        if self.children[0].evaluate(ST)[0]:
            self.children[1].evaluate(ST)
        elif len(self.children)>2:
            self.children[2].evaluate(ST)
            
########################################################################
class VarDec(Node):
    def evaluate(self, ST):
        if len(self.children) == 1:
            if self.value == "bar":
                ST.create(self.children[0].value, (0, self.value))
            elif self.value == "verse":
                ST.create(self.children[0].value, ("", self.value))
            
        else:
            tipo = self.children[1].evaluate(ST)
            if self.value != tipo[1]:
                raise SyntaxError("Tipo errado")
            ST.create(self.children[0].value, (tipo[0], self.value))
            
            
class StrVal(Node):
    def evaluate(self, ST):
        return (self.value, "verse")
    
########################################################################


    
class ReturnNode(Node):
    def evaluate(self, ST):
        return self.children[0].evaluate(ST)
    
class FuncDec(Node):
    def evaluate(self, ST):
        FT.setter(self.children[0].children[0].value, (self, self.children[0].value))
    
class FuncCall(Node):
    def evaluate(self, ST):
        call = FT.getter(self.value)
        
        if len(call[0].children) != len(self.children)+2:
            raise SyntaxError("Número de argumentos errados")
        
        nst = SymbolTable()
        for i in range(len(self.children)):
            call[0].children[i+1].evaluate(nst)
            nst.setter(call[0].children[i+1].children[0].value, self.children[i].evaluate(ST))
        
        result = call[0].children[-1].evaluate(nst)
        
        if result is not None:
            if call[1] != result[1]:
                raise SyntaxError("Tipo de função errado")
            else:
                return result
    