d = {' ': 1, 'a': 2, 'b': 3}

if ' ' in d.keys():
    d['space'] = d.pop(' ')
print(d)