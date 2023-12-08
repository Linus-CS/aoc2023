sum = 0
with open("./input/day1.txt") as file:
    for line in file:
        i = 0
        j = len(line) - 1
        num1 = None
        num2 = None
        seq1 = ""
        seq2 = ""

        while num1 == None or num2 == None:
            if num1 == None:
                if line[i] >= '0' and line[i] <= '9':
                    num1 = line[i]
                else:
                    seq1 += line[i]
                    i += 1

                    if seq1.__contains__("one"):
                        num1 = "1"
                    if seq1.__contains__("two"):
                        num1 = "2"
                    if seq1.__contains__("three"):
                        num1 = "3"
                    if seq1.__contains__("four"):
                        num1 = "4"
                    if seq1.__contains__("five"):
                        num1 = "5"
                    if seq1.__contains__("six"):
                        num1 = "6"
                    if seq1.__contains__("seven"):
                        num1 = "7"
                    if seq1.__contains__("eight"):
                        num1 = "8"
                    if seq1.__contains__("nine"):
                        num1 = "9"

            if num2 == None:
                if line[j] >= '0' and line[j] <= '9':
                    num2 = line[j]
                else:
                    seq2 = line[j] + seq2
                    j -= 1

                    if seq2.__contains__("one"):
                        num2 = "1"
                    if seq2.__contains__("two"):
                        num2 = "2"
                    if seq2.__contains__("three"):
                        num2 = "3"
                    if seq2.__contains__("four"):
                        num2 = "4"
                    if seq2.__contains__("five"):
                        num2 = "5"
                    if seq2.__contains__("six"):
                        num2 = "6"
                    if seq2.__contains__("seven"):
                        num2 = "7"
                    if seq2.__contains__("eight"):
                        num2 = "8"
                    if seq2.__contains__("nine"):
                        num2 = "9"
        print(int(num1 + num2))
        sum += int(num1 + num2)

print(sum)
