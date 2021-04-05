from ai42.progressbar import ft_progress
from time import sleep


rng = range(1000)
var = 0
for elem in ft_progress(rng):
    var += elem
    sleep(0.01)

print(var)
print(var)
