def penultimate(string):
    string = string.split()
    return string[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")