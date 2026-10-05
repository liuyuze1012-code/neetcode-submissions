class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in operations:
            if op == "+":
                result.append(result[-1] + result[-2]) 
            elif op == "C":
                result.pop()                           

            elif op == "D":
                result.append(result[-1] * 2)        

            else:
                result.append(int(op))

        total = 0
        for num in result:
            total += num
        return total
            


        