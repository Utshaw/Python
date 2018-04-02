



try:
    f = open('test.txt', 'r') # open the file in read mode default is read mode ; read+write = r+; read = r; append = a

    print(f.name) # file name

    f.close() # close the file when done with it

except FileNotFoundError:
    print('File not found...')


# using context-manager (recommended way)


for i in range(50):
    print('-', end='')
print()



# context manager closes file even if exception or not closing of file happens
with open('test.txt', 'r') as f:
    f_contents = f.read() # read entire content into the memory
    print(f_contents)

print(f.closed) # file is closed after with block so can't read anything


for i in range(50):
    print('-', end='')
print()





with open('test.txt', 'r') as f:
    f_contents = f.readlines() # reads all of the lines in file and make a list out of that
    for content in f_contents:
        print(content)


for i in range(50):
    print('-', end='')
print()




with open('test.txt', 'r') as f:
    f_contents = f.readline() # read line by line





for i in range(50):
    print('-', end='')
print()


# Efficient way
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
    print()



for i in range(50):
    print('-', end='')
print()

# putting size to read certain number of characters
with open('test.txt', 'r') as f:


    f.seek(10) # move the file 'pointer' after 10 characters
    size_to_read = 100

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

    print()

for i in range(50):
    print('-', end='')
print()




# write Mode

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# reading writing in binary mode for other file types (i.e image)

with open('sample.jpg', 'rb') as rf:
    with open('sample_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)