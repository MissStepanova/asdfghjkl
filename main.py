n_ps = input("Введи пороль")
ps = input("Повтори пожалуйта пороль")
def ask_password(ps_f, n_ps_f):
    run = True
    while run:
        if ps_f == n_ps_f:
            print("Пророль верный")
            run = False
        else:
            print("Пророль не верный")
            run = False
ask_password(ps, n_ps)