# here is the Answer to Ex5
#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

Money=50
usb=6
print(Money//usb,Money%usb)


usb_price = 6
budget = 50

num_usb = budget // usb_price
remaining_money = budget % usb_price

print("Number of USB sticks she can buy:", num_usb)
print("Pounds left:", remaining_money)