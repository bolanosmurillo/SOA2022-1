f = open("pylint.log", "r")
report = 0
for line in f:
    if "/10" in line:
        report = line
        break
f.close()
init = report.index("at ")
end = report.index("/")

grade = report[init:end]
space = grade.index(" ")
grade = grade[space+1:end]
grade = float(grade)
print(grade)
