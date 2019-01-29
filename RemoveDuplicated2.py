def remove_duplicates(numbers):
  numbers.sort()
  new_number = []
  for num in numbers:
    if num not in new_number:
      new_number.append(num)
  return new_number

print remove_duplicates([1, 1, 2, 2])
print remove_duplicates([2, 1, 3, 2, 3, 3])
print remove_duplicates([4, 1, 4, 2, 3, 3, 2, 4])
