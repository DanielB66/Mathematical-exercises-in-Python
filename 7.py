n = int(input("Enter a number: "))  # קבלת המספר מהמשתמש
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")  # מדפיס את המספר num
        num += 1
        if num > n:  # בדיקה אם המספר num עבר את המספר שהמשתמש הכניס
            break
    print()  # מעבר לשורה חדשה לכל שורה
    if num > n:  # בדיקה נוספת לסיום הלולאה החיצונית במקרה של break בלולאה הפנימית
        break
