#You are keeping the scores for a baseball game with strange rules. At the beginning of the game,
#  you start with an empty record
def calPoints(ops):
    record = []
    for op in ops:
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(2 * record[-1])
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
    return sum(record)

# Example usage
print(calPoints(["5", "2", "C", "D", "+"]))  # Output: 30
