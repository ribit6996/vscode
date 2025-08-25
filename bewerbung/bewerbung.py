import os
import time
import docx

datum = time.strftime('%d.%m')
Name = 'Oleksandr Gajdrik'
d = docx.Document

f = d("C:/Users/gaj99/Downloads/Motivationsschreiben.docx")

for para in f.paragraphs:
    for run in para.runs:
        if 'name' in run.text:
            run.text = run.text.replace('name', Name)

f.save("C:/Users/gaj99/Downloads/Motivationsschreiben1.docx")