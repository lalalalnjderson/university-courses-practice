def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    testYears = [1992, 1993, 1996, 1900, 2000, 2024, 2100, 2400]
    with open("years.txt", "w") as f:
        for y in testYears:
            f.write(str(y) + "\n")
    
    with open("years.txt", "r") as f:
        for line in f:
            year = int(line.strip())
            if isLeapYear(year):
                print(f"{year} -> leap year")
            else:
                print(f"{year} -> NOT leap year")
    
if __name__ == "__main__":
    main()