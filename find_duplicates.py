def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Test
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
print("Duplicates:", find_duplicates(nums))