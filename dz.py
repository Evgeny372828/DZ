Timur = input().lower()
Ruslan = input().lower()
if Timur == Ruslan:
    print("ничья")
elif Timur == "камень" and Ruslan == "ножницы" or Timur == "ножницы" and Ruslan == "бумага" or Ruslan == "бумага" and Ruslan == "камень":
    print("Победил Тимур")
else:
    print("Победил Руслан")