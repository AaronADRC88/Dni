__author__ = 'aferreiradominguez'
letrasT=('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')
print("introduce num DNI")
dni= input()
p = int(dni) % 23;
for i in letrasT:
    print(letrasT[p])
    break

