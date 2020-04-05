def trans_code(code):
    j = 0
    while j < len(code):
        if code[j] == ']':
            i = j  #i记录左括号，j记录右括号
            k = 0  #k记录‘|’
            while code[i] != '[':
                if code[i] == '|':
                    k = i
                i -= 1
            temp_code = code[k + 1:j] * int(code[i + 1:k])
            code = code.replace(code[i:j+1], temp_code)
            j = i
        j += 1
    return code
            
if __name__=='__main__':
    #code = 'HG[3|B[2|CA]]F'
    #code = 'BHCJSBCSCW[100|DASKDNKJWDNWCNQWCNOQCNQWOICNWQOINCWQOICNQWOIXWOISWIODAOWPQWDMQKOQZCDWF]WQJDWQUINCQQW[99|SDWQJCIQIUWCNQUCNWQIDNWQUIFNSALQP]DQOJOIXZALPPQQAAX'
    code = input()
    print(trans_code(code))
