def intersection(arrays):
    result = []
    d = {}

    for i in arrays:
        for j in i:
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
            
            if d[j] > 1 and j not in result:
                result.append(j)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append([1,2,3])
    arrays.append([1,4,5,3])
    arrays.append([1,6,7,3])

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
