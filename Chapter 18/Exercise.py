# Problem 1
# Read salary.txt 
# And return output as Darshan's salary is 100000

with open("H:/Python/Chapter 18/salary.txt",'r') as rf:
    with open("H:/Python/Chapter 18/Exercise.txt",'w') as wf:
        wf.write("Output of 1st Problem \n \n")
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}'s Salary is {salary}")


# Problem 2
# Read Index.html
# and Return links in html file
    
with open("H:/Python/Chapter 18/index.html",'r') as rf:
    with open("H:/Python/Chapter 18/Exercise.txt",'a') as wf:
        wf.write("\n \n Output of 2nd Problem \n \n")
        for line in rf.readlines():
            if "<a href" in line:
                pos = line.find("<a href")
                first_quote = line.find('\"', pos)
                second_quote = line.find('\"',first_quote+1)
                url = line[first_quote+1:second_quote]
                wf.write(f"{url}\n")

# Better solution for line having 2 links

with open("H:/Python/Chapter 18/index.html",'r') as rf:
    with open("H:/Python/Chapter 18/Exercise.txt",'a') as wf:
        wf.write("\n Ouput of 2nd problem with better solution i.e., it can find two links in one line \n \n")
        page = rf.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = page.find('\"', pos)
                second_quote = page.find('\"',first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(f"{url}\n")
                page = page[second_quote:]


