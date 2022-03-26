# 1. Open the phone_book.py file and copy/paste the following code:
import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row)
        # print(type(row)) #[2] What is the type of the row variable line 7 in the print(row) statement?
        line_count += 1

# [3] Try updating the code of phone_book.py to ignore the header (first line) and only print last name + phone number.

# with open('data/phone_book.csv', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     line_count = 0
#     for row in csv_reader: #Skip first element
#         if line_count > 0:
#             first_name = row[0]
#             phone_number = row[2]
#             print(f"{first_name}: {phone_number}")

#         line_count += 1
