def differing_bits(bin1, bin2):
    #assert both binary strings are of equal length
    assert len(bin1) == len(bin2), "Binary strings must be of equal length"

    #count differing bits
    differing_count = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
    return differing_count

bin1 = "11010111"
bin2 = "11100101"
result = differing_bits(bin1, bin2)
print(f"Number of differing bits: {result}")
