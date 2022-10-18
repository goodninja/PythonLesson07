path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson07/catalog.txt'
output_path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson07/output.txt'
catalog = ""

def read_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read().split('\n')
    return catalog

def write_file(str1, str2):
    with open(path,'r+',encoding='utf-8') as file:
        length = len(file.readlines())
        file.write(f'{length+1};{str1};{str2}\n')

def export_file(array):
    with open(output_path,'w',encoding='utf-8') as file:
        count = 1
        for i in range(len(array)):
            file.write(f'{count}.{array[i][1]}, телефон {array[i][2]}\n')
            count+=1