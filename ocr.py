from easyocr.easyocr import Reader

# user-network


reader = Reader(['ko'], gpu=False)



result = reader.readtext('D:/format_pc_intro_015@2x.jpg')


print(result[0])
print(result[1])
print(result[2])



