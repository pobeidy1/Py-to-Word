# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:09:28 2022

@author: pobe4699
"""

def define_input_outputfile_timestamp(file_Name_str,add_prefix_to_output_file):
    import datetime
    from pathlib import Path
    import os

    time = datetime.datetime.now()
    output_time = time.strftime("%Y%m%d_%H%M_")
    output_file_name = f"{output_time}{add_prefix_to_output_file}"
    
    input_path = Path(__file__).parent /"input"/ f"{file_Name_str}"
    output_path = Path(__file__).parent /"output"/  f"{output_time}{add_prefix_to_output_file}"

    return output_path,input_path