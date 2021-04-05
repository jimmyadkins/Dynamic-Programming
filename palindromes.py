#change name to txt file
file = "AliceRawText.txt"

def palindrome(str):
    arr = list(str)
    n = len(arr)
    table = [[0 for x in range(n)] for y in range(n)]

    # Fill in the length = 1 on the table
    best = 1
    i = 0
    while (i < n):
        table[i][i] = 1
        i = i + 1
    print("Length 1 complete.")

    # Fill in the length = 2 on the table
    start = 0
    i = 0
    while i < n - 1:
        if (arr[i] == arr[i + 1]):
            table[i][i + 1] = 1
            start = i
            best = 2
        i = i + 1
    print("Length 2 complete.")

    # Fill in the length >= 3 on the table
    length = 3
    while length <= n:
        i = 0
        while i < (n - length + 1):
            j = i + length - 1

            if (table[i + 1][j - 1] == 1 and
                    arr[i] == arr[j]):
                table[i][j] = 1

                if (length > best):
                    start = i
                    best = length
            i = i + 1
        if length%100 == 0:
            print(f"Length {length} complete.")
        length = length + 1

    result = ""
    i = 0
    while i < best:
        result += arr[i+start]
        i = i + 1
    return best, result

# can paste the string into the test_string variable instead of file
#test_string = "ibidonatacocatonebaylasttuesday"

test_string = open(file).read()
result = palindrome(test_string)
print(f'At length {result[0]}, the longest palindrome is:')
print(result[2])
