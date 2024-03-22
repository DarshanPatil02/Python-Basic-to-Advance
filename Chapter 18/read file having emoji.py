# Here we are going to read txt file having emoji
with open("H:/Python/Chapter 18/Love story.txt", 'r', encoding='utf-8') as rf:
    print(rf.encoding)
    data = rf.read()
    print(data)
