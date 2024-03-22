# To write in csv file we can use writer and DictWriter in csv module
# Write csv file by writer


from csv import writer
with open('Chapter 19/written_csv_file.csv','w',newline='') as wf:
    csv_writer = writer(wf)
    # We can write with two methods writerow, writerows
    # writerow
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Darshan','INDIA'])
    csv_writer.writerow(['Ajay','INDIA'])
    csv_writer.writerow(['Sumit','INDIA'])

with open('Chapter 19/written_csv_file.csv','a',newline='') as wf:
    csv_writer = writer(wf)
    # We can write with two methods writerow, writerows
    #writerows
    csv_writer.writerows([['John','UK'],['Tom','UK'],['Kane','UK']])


from csv import DictWriter
with open("H:\Python\Chapter 19\written_csv_file.csv","a",newline='') as f:
    f.write("\n \n")
    csv_writer = DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    # We can write with two methods writerow, writerows
    csv_writer.writerow({'first_name':'Darshan','last_name':"Patil",'age':21})
    # Writerows
    csv_writer.writerows([
        {'first_name':'Rohit','last_name':"Sharma",'age':42},
        {'first_name':'Surya','last_name':'Yadav','age':38},
        {'first_name':'Deepak','last_name':'Chahar','age':25}
        ])