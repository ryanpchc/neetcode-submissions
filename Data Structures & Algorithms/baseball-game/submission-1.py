class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            try:
                op = int(op)
                record.append(op)
            except ValueError:
                if op == "+":
                    last_two_sum = record[-1] + record[-2]
                    record.append(last_two_sum)
                elif op == "D":
                    double_previous_score = 2 * record[-1]
                    record.append(double_previous_score)
                else:
                    record.pop()
        
        record_sum = sum(n for n in record)
        return record_sum