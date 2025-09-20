import numpy as np
from random import choice

class FileWriting:
    def __init__(self):
        self.file_int = int()
        self.lr = 271
        self.ur = 363
        self.curr = int()
    def main(self):
        for i in range(self.lr, self.ur+1):
            self.curr = i
            self.open()
            #if i > 275:
                #break
    def open(self):
        fl = "Chapter_Generator/chapter" + str(self.curr) + ".html"
        with open(fl, "w") as file:
            self.Write(file)
        print(f'File {self.curr} complete.')
    def Write(self, file):
        file.write("<?xml version='1.0' encoding='utf-8'?>\n")
        file.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
        file.write("<head>\n")
        file.write("<title>"+"Chapter "+str(self.curr)+"</title>\n")
        file.write("</head>\n\n")
        file.write("<body>\n\n")
        file.write("</body>\n")
        file.write("</html>")

FW = FileWriting()

FW.main()