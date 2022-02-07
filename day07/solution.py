with open("input.txt", "r") as f:
    input_data = f.read()
    input_data = input_data.split(",")
def solution(data):
    data = [int(x) for x in data]
    values = set(data)
    fMin1 = 9223372036854775807
    fMin2 = 9223372036854775807
    for i in values:
        sum1 = 0
        sum2 = 0
        for j in range(len(data)):
            n = abs(i - data[j])
            sum1 += n
            sum2 += n*(n+1)//2
        if sum1 < fMin1:
            fMin1 = sum1
        if sum2 < fMin2:
            fMin2 = sum2
    return fMin1, fMin2
print(solution(input_data))