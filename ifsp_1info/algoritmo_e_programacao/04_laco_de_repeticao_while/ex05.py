canal9 = 0
canal12 = 0
canal23 = 0
canal40 = 0
outros = 0 
pessoas = 0
canal = None

while canal != 0:
    canal = int(input("Qual seu canal foi favorito? "))
    if canal != 0: 
        pessoas += 1

    if canal == 9:
        canal9 += 1
    elif canal == 12:
        canal12 += 1
    elif canal == 23:
        canal23 += 1
    elif canal == 40:
        canal40 += 1
    elif canal != 0:
        outros += 1 

print(f"{canal9 * (100 /pessoas)}% das pessoas assistem o canal \n{canal12 * (100 / pessoas)}% das pessoas assistem o canal 12\n{canal23 * (100 / pessoas)}% das pessoas assistem o canal 23\n{canal40 * (100 / pessoas)}% das pessoas assistem o canal 40\n{outros * (100 / pessoas)}% das pessoas assistem outro canal")