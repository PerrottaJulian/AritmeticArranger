problems = list()
problems = ["1234 + 101", "25 - 324", "31 + 25", "120 - 3215"]

def aritmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return ("Error: Too many problems.")

    first_line = ""
    second_line = ""
    lines = ""
    result = ""
    for problem in problems:
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if len(first_number) > 4 or len(second_number) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        if operator != "+" and operator != "-":
            return("Error: Operator must be '+' or '-'.")

        lenght = max(len(first_number), len(second_number)) + 2

        first_line += first_number.rjust(lenght) + "    "
        second_line += operator + second_number.rjust(lenght-1) + "    "
        lines += "-"*lenght + "    "

        try:
            first_number = int(first_number)
            second_number = int(second_number)
        except:
            return ("Error: Numbers must only contain digits.")
        
        if solve == True:
            if operator == "+":
                result += str(first_number + second_number).rjust(lenght) + "    "
            else:
                result += str(first_number - second_number).rjust(lenght) + "    "

            arranged_problems = first_line +"\n"+second_line + "\n" + lines + "\n" + result
        else:
            arranged_problems = first_line +"\n"+second_line + "\n" + lines

    return(arranged_problems)
    
print(aritmetic_arranger(problems, True))
        
