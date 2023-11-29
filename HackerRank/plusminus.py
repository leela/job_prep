def plusminus(arr):
    precision = 6
    no_of_positives = 0
    no_of_negatives = 0
    no_of_zeros = 0

    for number in arr:
        if number > 0:
            no_of_positives += 1
        elif number < 0:
            no_of_negatives += 1
        else:
            no_of_zeros += 1    
    positive_ratio = round(no_of_positives/len(arr), precision)
    negative_ratio = round(no_of_negatives/len(arr), precision)
    zero_ratio = round(no_of_zeros/len(arr), precision)
    print(f"{positive_ratio}\n{negative_ratio}\n{zero_ratio}")
    return positive_ratio, negative_ratio, zero_ratio

def test_plusminus():
    sequences = [
        [0, 0, 0, 0, 0],
        range(2, 10, 3),
        range(-10, 100, 5)
    ]
    for seq in sequences:
        res = plusminus(seq)
        print(seq, res)
        assert sum(res) == 1