def calculate(data, findall):
    # data = {"a": 1, "b": 2, "c": 3}
    matches = findall(r"([abc])([+-])?=([abc])?([+-]?\d*)?")
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        if s == '+':
            data[v1] = data[v1] + data.get(v2, 0) + int(n or 0)
        elif s == '-':
            data[v1] = data[v1] - data.get(v2, 0) + int(n or 0)
        elif s == '':
            data[v1] = data.get(v2, 0) + int(n or 0)
        else:
            raise Exception('Такой операции не предусмотрено!')
    return data
