def minmax(arr):
    sorted_array = sorted(arr)
    min = sum(sorted_array[:4])
    max = sum(sorted_array[-4:])
    print(f"{min} {max}")
    return min, max

def test_minmax():
    seq = [1, 2, 3, 4, 5]
    assert minmax(seq) == (10, 14)