# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:00:47 2022

@author: pobe4699
"""


from docxtpl import DocxTemplate

from utls.context2 import * 
from makeTimeStamped_outputFile import define_input_outputfile_timestamp
import os

#change this one
file_Name_str = "test_Abstract_01.docx"
add_prefix_to_output_file = "generated_doc.docx"


print(25*("--"),end=" \n")
print("Lets do this!"+20*("--"),end=" \n")

output_path,input_path = define_input_outputfile_timestamp(file_Name_str,add_prefix_to_output_file)
print("The input path is :",input_path , end=" \n")

doc = DocxTemplate(input_path)
print("Your template is recieved...", end=" \n")

doc.render(context)
print("I am rendering the outcome document...", end=" \n")

doc.save(output_path)        
print("Good Job, WellDone!"+20*("--"))
print(25*("--"),end=" \n")

