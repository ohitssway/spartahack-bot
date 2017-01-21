class Calculator:
    def __init__(self):
        self.expr = ""
        self.pos = 0
    def eval_infix_sum(self,expr, pos):
       expr = self.eval_infix_factor(expr, pos)    #returns the expression after it evaluates all the expressions in between parentheses.
       expr = self.eval_infix_product(expr,pos)    #returns the expression after all multiplication and division operators
       try:  ans = int(expr[pos])
       except:  ans = 0
       for i in range(pos + 1, len(expr)):
          if expr[i] == "+":
             ans += expr[i+1]     #if the element is a "+" then the number after it is just added to the total sum (ans)
          elif expr[i] == "-":
             ans -= expr[i+1]     #if the element is a "-" then the number after it is just subtracted to the total sum (ans)
          elif type(expr[i]) != int:
             break
       return ans, pos
    
    def eval_infix_product(self,expr, pos):
       while '*' in expr or '/' in expr or '%' in expr:
          try:  mul = expr.index("*")
          except:  mul = len(expr) + 1
          try: div = expr.index("/")
          except: div = len(expr) + 1
          try: mod = expr.index("%")
          except: mod = len(expr) + 1
          
          if mul < div and mul < mod:
             ans = expr[mul-1] * expr[mul+1]
             expr = expr[0:mul-1] + [ans] + expr[mul+2:]      #replaces the "a * b" terms with the actual product a*b
          elif div < mul and div < mod:
             ans = expr[div-1]//expr[div+1]
             expr = expr[0:div-1] + [ans] + expr[div+2:]      #replaces the "a // b" terms with the actual quotient a//b
          elif mod < div and mod < mul:
             ans = expr[mod-1]%expr[mod+1]
             expr = expr[0:mod-1] + [ans] + expr[mod+2:]      #replaces the "a % b" terms with the actual value of a % b
       return expr
    
    def eval_infix_factor(self,expr, pos):
       while '(' in expr:
          openingPI = len(expr) - 1 - expr[::-1].index('(')     #find the index of the last instance of "("
          tempExpr = expr[openingPI + 1:]     #creates a temporary array of the expression's elements after that last "("
          closingPI = len(expr[:openingPI + 1]) + tempExpr.index(')')    #finds the first instance of ")" in tempExpr since that will be the closing parentheses
          factorAns, discard = self.eval_infix_sum(expr[openingPI+1:closingPI], pos)
          expr = expr[0:openingPI] + [factorAns] + expr[closingPI+1:]
       return expr
    
    def eval_infix_list(self,expr):
       for i in range(len(expr)):
          try:  expr[i] = int(expr[i])     #replaces the list element with the integer type of the element (i.e. "5" become 5)
          except:  pass
       ans, discard = self.eval_infix_sum( expr, 0 )     # start subscript at 0, then forget it
       return ans
       
    def eval_infix(self,expr):
       # evaluate an expression represented as a single space-separated string
       return self.eval_infix_list(expr.split() + [';'])    # make a list, and append semicolon