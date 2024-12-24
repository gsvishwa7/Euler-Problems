prev_x = 1
new_x = 2
current_x = 2
sum = 0
while current_x <= 4000000:
    if current_x%2 == 0:
        sum = sum + current_x
    new_x = current_x + prev_x
    prev_x = current_x
    current_x = new_x
print(sum)

