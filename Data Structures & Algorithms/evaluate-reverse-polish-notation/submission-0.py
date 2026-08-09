class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        result = 0

        for c in tokens:

            if c == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif c == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)

            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif c == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            
            else:
                #number
                stack.append(int(c))

        return stack.pop()
