def arithmetic_arranger(problems, show_answers=False):
    top = []
    bottom = []
    dash = []
    answers = []
    
    if len(problems) > 5:
        print('Error: Too many problems. The limit is five')
        return
    
    for string in problems:
        split_string = string.split()
        
        if not split_string[0].isdigit() or not split_string[2].isdigit():
            print('Error: Numbers must only contain digits.')
            return
        
        if len(split_string[0]) > 4 or len(split_string[2]) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
        
        if split_string[1] not in ['+', '-']:
            print("Error: Operator must be '+' or '-'.")
            return
        
        max_length = max(len(split_string[0]), len(split_string[2]))
        top.append(split_string[0].rjust(max_length + 2))
        bottom.append(split_string[1] + split_string[2].rjust(max_length + 1))
        dash.append('-' * (max_length + 2))
        
        if show_answers:
            if split_string[1] == '+':
                answer = int(split_string[0]) + int(split_string[2])
            else:
                answer = int(split_string[0]) - int(split_string[2])
            answers.append(str(answer).rjust(max_length + 2))

    top_line = "  ".join(top)
    bottom_line = "  ".join(bottom)
    dash_line = "  ".join(dash)
    answers_line = "  ".join(answers)
    
    print(top_line, '\n')
    print(bottom_line, '\n')
    print(dash_line, '\n')
    if show_answers:
        print(answers_line)

arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
