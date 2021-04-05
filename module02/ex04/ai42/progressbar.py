from time import time
from time import sleep


def ft_progress(listy):
    list_len = len(listy)
    first_call = time()
    for i in range(0, list_len + 1):
        now = time()
        elapsed = now - first_call
        ETA = 0
        if i:
            ETA = elapsed * list_len / i
        hours = ETA // 3600
        minutes = (ETA - (3600 * hours)) // 60
        seconds = ETA - (3600 * hours) - (60 * minutes)
        print('ETA: ', end='')
        if i and hours:
            print('{:.0f}'.format(hours) + 'h ', end='')
        if i and minutes:
            print('{:.0f}'.format(minutes) + 'm ', end='')
        if i:
            print('{:.2f}'.format(seconds) + 's ', end='')
        print('[' + str(int(i * 100 / list_len)).rjust(3, ' ') + '%]', end='')
        print('[' + '>'.rjust(int((i / list_len) * 24), '=').ljust(24, ' ') +
              '] ', end='')
        print(str(int(i)).rjust(len(str(list_len)), ' ') +
              '/' + str(list_len) + ' | ', end='')
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
