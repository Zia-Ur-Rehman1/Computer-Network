

print(onlyfiles,'\n')

# import binascii
# import codecs
list_size = []
for i in onlyfiles:
    status = os.stat(join(path, i))
    list_size.append(status.st_size)
print(list_size)
# bin_data = open('test.text', 'rb').read()
# hex_data = codecs.encode(bin_data, "hex_codec")
# # print(len(hex_data))
# filename = 'test.text'
# with open(filename, 'rb') as f:
#     content = f.read()
# print((binascii.hexlify(content)))
def send_chunk_to_space(chunk):
    print(chunk)

CHUNK_SIZE = 100
for i in onlyfiles:
    f = open(join(path,i), 'rb')
    chunk = f.read(CHUNK_SIZE)

    while chunk:

	    send_chunk_to_space(chunk)
	    chunk =f.read(CHUNK_SIZE) #read the next chunk

#     #loop until the chunk is empty (the file is exhausted)
    f.close()
