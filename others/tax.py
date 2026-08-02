'''
Calculate tax if Salary and Tax Brackets are given as list in the form [ [10000, 0.3],[20000, 0.2], [30000, 0.1], [null, .1]] null being rest of the salary

'''



salary = 70000

brackets = [
    [10000, 0.30],
    [20000, 0.20],
    [30000, 0.10],
    [None, 0.10]
]

print(calculate_tax(salary, brackets))
