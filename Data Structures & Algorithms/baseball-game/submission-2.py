class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            try:
                op = int(op)
                record.append(op)
            except ValueError:
                if op == "+":
                    record.append(record[-1] + record[-2])
                elif op == "D":
                    record.append(2 * record[-1])
                else:
                    record.pop()
        
        record_sum = sum(n for n in record)
        return record_sum