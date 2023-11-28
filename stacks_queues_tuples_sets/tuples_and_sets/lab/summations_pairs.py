class SummationPairs:

    def __init__(self, current_numbers, current_target):
        self.current_numbers = current_numbers
        self.current_target = current_target
        self.summation_pairs = self.find_summations_pairs()

    def find_summations_pairs(self):
        summations_pairs = set()
        current_numbers = self.current_numbers.copy()
        for first_number in self.current_numbers:

            current_numbers.remove(first_number)
            for second_number in current_numbers:
                if first_number + second_number == self.current_target:
                    summations_pairs.add(f"{first_number} + {second_number} = {self.current_target}")

        return summations_pairs

    def __repr__(self):
        return "\n".join(self.summation_pairs)

numbers = list(map(int, (input().split())))
target = int(input())

print(SummationPairs(numbers, target))