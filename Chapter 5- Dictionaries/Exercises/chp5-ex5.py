burger = {
    'species':'dog',
    'owner':'jack',
    'name':'burger',
}
fany = {
    'name':'fany',
    'species':'cat',
    'owner':'james',
}

pets = [burger,fany]
for pet in pets:
    print(pet['name'].title()+' is a '+pet['species']+', and it belongs to '+
        pet['owner'].title()+'.')