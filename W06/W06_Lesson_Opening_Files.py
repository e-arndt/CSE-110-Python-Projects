# Author: Eric Arndt
# Class: CSE 110 W06 Lesson Opening Files


path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\PCB 103\\CSE 110\\CSE 110 Code Projects\\W06\\books.txt"
print()
with open(path, "r") as bom_books:
    for read in bom_books:
        book = read.strip()
        print(book)
        
print()