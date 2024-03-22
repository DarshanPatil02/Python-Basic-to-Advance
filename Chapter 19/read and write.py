# Write a data in file salary_output.txt from reading file salary.txt where salary of person>100000

from csv import DictReader,DictWriter
with open('H:\Python\Chapter 19\salary.txt','r') as rf:
    with open('H:\Python\Chapter 19\salary_output.txt','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['f_name','lname','salary'])
        csv_writer.writeheader()
        for row in csv_reader:
            f_name,lname,salary = row['first_name'],row['last_name'],int(row['salary'])
            if salary>=100000:
                csv_writer.writerow({
                    'f_name':f_name,'lname':lname,'salary':salary
                })
        


