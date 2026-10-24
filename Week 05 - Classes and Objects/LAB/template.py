"""
RECORD CHECK  -  my version
===========================

Name  : Adel Gholamshahzadeh
Lane  :  AI
Date  : 24/10/2020

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.


# your class goes here
class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """This method showcases the status of the record"""
        percent = (self.value / self.limit) * 100
        percent_overlimit  = ""
        if percent >= 100:
            percent_overlimit  = "OVER LIMIT"
            print("OVER LIMIT")
        elif percent >= 90:
            print("WARNING")
        else:
            print("OK")
        if percent_overlimit == "OVER LIMIT":
            Record.over_limit_count += 1
        return self.over_limit_count

# ==================================================================== RECORDS
# 2. Create your records.


records = []   # replace with your code
record1 = Record("rec1", 40, 100)
record2 = Record("rec2", 200, 100)
#record1_status = record1.status()
#record2_status = record2.status()
records.append(record1) 
records.append(record2)   


# ==================================================================== OUTPUT


for record in records:
    print()
    print("=" * 34)
    print()
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f" Label: {record.label} | Value: {record.value} | Limit:  {record.limit}")
    print(f"Status:  {record.status()}")
    print("=" * 34)


# ==========================================================================

