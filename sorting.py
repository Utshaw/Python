
li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li) # returns a new sorted list

print('Sorted List: ', s_li )
print('Original List: ', li )

li.sort() # sort() sorts the list in place and returns None
print('Original List: ', li )

r_list = sorted(li, reverse=True)
print('Reverse Sorted List ', r_list)

dict = {'roll': 1505105, 'name': 'Utshaw'}

print(sorted(dict)) # returns a list of sorted key's


