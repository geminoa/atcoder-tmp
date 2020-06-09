s = input().strip()
l = ['dreameraser','dreamerase','dreamer','eraser','dream','erase']
idx = 0
while idx < len(l):
   if s.startswith(l[idx]):
       s = s[len(l[idx]):]
       idx = 0
       continue
   idx += 1
if len(s) == 0: print('YES')
else: print('NO')
