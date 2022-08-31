i='helloWoRLd hOw Are yOu'
def swap_case(s):
    for i in s:
        if i == i.upper():
            i=i.lower()
        else:
            i = i.upper()
    return i
print(swap_case(s))