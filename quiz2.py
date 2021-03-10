input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    for i in input:
        a = input.count(i)
        print(a)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
