def has_negatives(a):

    result = []
    d = {}

    for num in a:

        if abs(num) not in d:
            if num > 0:
                d[abs(num)] = 1
            else:
                d[abs(num)] = 0

        else:
            if num < 0 and d[abs(num)] == 1:
                result.append(abs(num))
            elif num > 0 and d[abs(num)] == 0:
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
