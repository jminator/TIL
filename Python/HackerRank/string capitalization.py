
def cap_name(name):
    lst = name.split(' ')
    n_lst = []
    for name in lst:
        n_lst.append(name.capitalize())
    
    full_name = ' '.join(n_lst)
    return full_name

if __name__ == '__main__':
    name = input()
    result = cap_name(name)
    print(result)
