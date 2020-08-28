import os
import csv
from pdfminer.high_level import extract_text
import pandas as pd



pdf_names = []
text_list = []

directory = '/home/ayu/Desktop/profile/resume'


for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdf_names.append(filename)


for pdf in pdf_names:
    text = extract_text(pdf)
    text_list.append(text)


dict = {'text':text_list}  
     
df = pd.DataFrame(dict) 
   
df.to_csv('record.csv') 



