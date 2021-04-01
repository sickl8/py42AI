from time import time
from time import sleep


def ft_progress(listy):
    list_len = len(listy)
    first_call = time()
    for j in listy:
        i = j + 1
        now = time()
        elapsed = now - first_call
        ETA = elapsed * list_len / i
        hours = ETA // 3600
        minutes = (ETA - (3600 * hours)) // 60
        seconds = ETA - (3600 * hours) - (60 * minutes)
        print('ETA: ', end='')
        if hours:
            print('{:.0f}'.format(hours) + 'h ', end='')
        if minutes:
            print('{:.0f}'.format(minutes) + 'm ', end='')
        print('{:.2f}'.format(seconds) + 's ', end='')
        print('[' + str(int(i * 100 / list_len)).rjust(3, ' ') + '%]', end='')
        print('[' + '>'.rjust(int((i / list_len) * 24), '=').ljust(24, ' ') +
              '] ', end='')
        print(str(i) + '/' + str(list_len) + ' | ', end='')
        print('elapsed time ', end='')
        hours = elapsed // 3600
        minutes = (elapsed - (3600 * hours)) // 60
        seconds = elapsed - (3600 * hours) - (60 * minutes)
        if hours:
            print('{:.0f}'.format(hours) + 'h ', end='')
        if minutes:
            print('{:.0f}'.format(minutes) + 'm ', end='')
        print('{:.2f}'.format(seconds) + 's', end='\r')
        yield i
    return


listy = range(10000)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.001)
print()
print(ret)
