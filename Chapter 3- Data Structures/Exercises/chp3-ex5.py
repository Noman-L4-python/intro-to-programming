invite = ["Dr Israr Ahmed","Sohaib","Ibrahim"]
print("You are Invited to dinner at my house this Evening,", invite[0])
print("You are Invited to dinner at my house this Evening,", invite[1])
print("You are Invited to dinner at my house this Evening,", invite[2])

out_guest = invite.pop(2)
print(out_guest, "couldn't make the dinner!")


new_guest = "Khabib"
invite.insert(1,new_guest)

print("You are Invited to dinner at my house this Evening,", invite[0])
print("You are Invited to dinner at my house this Evening,", invite[1])
print("You are Invited to dinner at my house this Evening,", invite[2])