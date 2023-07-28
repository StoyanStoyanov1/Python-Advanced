def positive_vs_negative(numbers):
    positive = []
    negative = []

    for num in numbers:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)

    if sum(positive) > abs(sum(negative)):
        return f"{sum(negative)}\n{sum(positive)}\nThe positives are stronger than the negatives"
    else:
        return f"{sum(negative)}\n{sum(positive)}\nThe negatives are stronger than the positives"


numbers = list(map(int, input().split()))
print(positive_vs_negative(numbers))
