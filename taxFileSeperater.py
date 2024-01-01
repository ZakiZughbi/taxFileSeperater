import os
import pdfplumber

#Change to Working Directory
dir1 = r'C:\Users\mcacc\Desktop\2019 PDF Tax Copy'
os.chdir(dir1)

#Get list of all file Directories
fList=[]
for f in os.listdir():
    fList.append(f)


#If 8879 tax file is the first page on pdf
for f in fList:
    #gets text from pdf
    with pdfplumber.open(f) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()

    #makes in str format
    data = text.split('\n')

    target = data[0]
    print(target)
    if target == '8879':
        #moves files, (basename is the file name)
        os.replace(f, 'C:\\Users\\mcacc\\Desktop\\8879 Files 2\\' +  os.path.basename(f))


#If 8879 tax file isnt the first page on pdf
for f in fList:
    with pdfplumber.open(f) as pdf:
        if len(pdf.pages) >= 4:
            page = pdf.pages[4]
            text = page.extract_text()
        else:
            text = None
    if text != None:
        data = text.split('\n')
        target = data[0]
        print(target)
        if target == '8879':
            os.replace(f, 'C:\\Users]]mcacc]]Desktop\\8879 Files 2\\' +  os.path.basename(f))
