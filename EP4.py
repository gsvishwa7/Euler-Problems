#Find the largest palindrome made from the product of two 3-digit numbers.

#product = 0
curr_product = 0

# x = 999
# y = 999
# curr_product = x*y #999*999
# while str(curr_product)[::-1] != str(curr_product):
#     look_ahead_1 = (x-1)*y #998*999 997*999
#     look_ahead_2 = x*(y-1) #999*998 998*998


for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        product = x*y
        if product < curr_product:
            break
        if str(product)[::-1] == str(product):
            print(x,y, x*y)
            curr_product = product
            break

print(curr_product)    