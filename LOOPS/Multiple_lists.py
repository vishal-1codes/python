#zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
#zip can handle three or more lists as well!
#Here we comapire two list and if element is greater then another element it return greter element.
#max also help us.
#zip help to comapire elements in two or three list at a time
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  print(max(a,b))
  