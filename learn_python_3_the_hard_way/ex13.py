from sys import argv
from datetime import date

arquivo, primeiro, segundo = argv
print(
    f"O arquivo é {arquivo}, o primeiro argumento é {primeiro} e o sengundo argumento é {segundo}"
)
ano = int(input("Em que você nasceu? "))
print(f"Você tem {date.today().year - ano}")
