#Write a map function that adds plus 5 to each item in the list.

lst1=[10, 20, 30, 40, 50, 60]
def addfive(items):
    return items + 5
lst2=list(map(addfive, lst1))

print(lst2)