# main program
# student budget for college

import module1
import module2
import module3

print("Student College Budget Tracker")
print("------------------------------")

name, course, year = module1.student_details()
pm, sch, job, income_total = module1.get_income()

food, books, travel, mobile, fun, other, expense_total = module2.get_expenses()
other, expense_total = module2.extra_expense(other, expense_total)

bal = module3.calc_balance(income_total, expense_total)
module3.show_report(name, course, year, income_total, expense_total, bal)
module3.suggestions(food, fun, mobile, bal)

ch = input("\nSave this record? yes/no: ")
if ch == "yes" or ch == "Yes":
    module3.save_record(name, course, income_total, expense_total, bal)
else:
    print("Not saved")

print("Thank you")
