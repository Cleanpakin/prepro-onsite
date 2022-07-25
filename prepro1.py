'''prepro1'''
def main():
    '''prepro ez'''
    grade = float(input())
    grade2 = 4.00 - grade
    if grade < 1.00:
        print("I'm so sad.")
    elif grade >= 2.00:
        print("I'm so happy.")
    else:
        print("%.2f" %grade2)
main()
