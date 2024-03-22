
stdform = input('Enter a number in scientific notation: ')
#test
stdform = stdform.strip()
correct = True
x= -1
dot = -1
caret = -1
for i in range(len(stdform)):
  c = stdform[i]
  if c=='x':
    if x!=-1:
      correct = False
    x  = i
  elif c=='.':
    if dot!=-1:
      correct = False
    dot = i
  elif c=='^':
    if caret!=-1:
      correct = False
    caret = i

if x==-1 or dot==-1 or caret==-1:
  correct= False
if correct:
  s = 0
  e = dot
  if stdform[s:s+1]=='-':
    s = 1
  if not stdform[s:e].isdigit():
    correct = False
  if not stdform[e+1:x].isdigit():
    correct = False
  if stdform[x+1:caret] != "10":
    correct = False
  s = caret + 1
  if stdform[s:s+1] == '-':
    s = s+1
  if not stdform[s:].isdigit():
    correct = False
if correct:
  base = stdform[:x]
  power = stdform[caret+1:]
  print("This number in E notation is " + base + 'E' + power + '.')
else:
  print("Error converting to scientific E notation.")
