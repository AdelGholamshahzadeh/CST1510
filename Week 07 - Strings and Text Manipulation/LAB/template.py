"""
RECORD CHECK  -  my version
===========================

Name  : Adel Gholamshahzadeh
Lane  :  AI
Date  : 11/10/20206


Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""creating a parse_line function to look at the raw lines and retrning dictionary"""
a_dict = {}
def parse_line(raw_line):

    hostname_part, rest = raw_line.strip().split(",",1)

    hostname = hostname_part.strip().lower()

    a_dict["hostname"] = hostname

    for x in rest.strip().split(","):
        key,value = x.split("=")
        a_dict[key.strip().lower()] = float(value.strip())
    return a_dict
"""checking the status of the dictionary"""
def status_of(a_dict):             
        percent = (a_dict["used"]/a_dict["total"]) * 100  
        if percent >= 100:                      
            print("OVER LIMIT")
        elif percent >= 90:
            print("WARNING")
        else:
            print("OK")
            
"""checking the methods"""
a_line = "SRV-02,used=120,total=100"
parse_method = parse_line(a_line)
print(parse_method)
status_of(parse_method)



"""looping through a file"""
with open(r"C:\Users\ACER\Documents\CST1510\Week 07 - Strings and Text Manipulation\LAB\Template_list.txt") as f:
    for line in f:
        parse_method = parse_line(line)
        print(parse_method)
        status_of(parse_method)
    

