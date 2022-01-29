import random
import string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%&()-=+,.;:/?'  #é possivel trocar por lowercase ou upercase

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))