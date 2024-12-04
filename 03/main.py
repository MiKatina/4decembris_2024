a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]# saraksts ar cipariem 

num = int(input("Choose a number: ")) # aprēķināšana ar veseliem skaitliem, izvēlās ciparu 

new_list = []

for i in a:
    if i < num:
        new_list.append(i) # pievieno 

print(new_list)