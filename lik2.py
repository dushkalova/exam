import re
def readfile():
    f = ''
    f = open('lik.txt', 'r', encoding='utf-8')
    inf = f.read()
    f.close
    return inf

def find_1(inf):
    result = ''
    forma = re.compile('[а-я] ([А-Я]\. [А-Я][а-я].+?)[\]\[ \.\:\,\;»]')
    spisok = forma.findall(inf)        
    result1 = ', '.join(spisok)
    return result1

def find_2(inf):
    result = ''
    forma = re.compile('([А-Я]\. [А-Я]\. [А-Я][а-я].+?)[\]\[ \.\:\,\;»]')
    spisok = forma.findall(inf)
    result2 = ', '.join(spisok)
    return result2

def find_3(inf):
    result = ''
    forma = re.compile('([А-Я][а-я]+? [А-Я][а-я].+?)[\]|\[|\.\: \,\;»]')
    spisok = forma.findall(inf)
    result3 = ', '.join(spisok)
    return result3

def main():
    inf = ''
    inf = readfile()
    result1 = find_1(inf)
    result2 = find_2(inf)
    result3 = find_3(inf)
    print(result1+'\n'+result2+'\n'+result3)
    
if __name__ == "__main__":
    main()
