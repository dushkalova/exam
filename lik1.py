# exam
import re
def readfile():
    f = ''
    f = open('lik.txt', 'r', encoding='utf-8')
    inf = f.read()
    f.close
    return inf

def find_1(inf):
    result = ''
    forma = re.compile('([А-Я]\. [А-Я][а-я]*? )')
    spisok = forma.findall(inf)
    result = ', '.join(spisok)
    return result

def main():
    inf = ''

    inf = readfile()
    result = find_1(inf)
    print(result)
    
if __name__ == "__main__":
    main()
