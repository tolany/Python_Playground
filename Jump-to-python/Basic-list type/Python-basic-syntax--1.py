#Basic Syntax 

#1-1 if statement 
a = 3 
if a > 1:
    print("a is greater than 1")

#1-2 for statement 
for b in [1,2,3]:
    print(b)

#1-3 while statement 
i = 0
while i < 3:
    i = i + 1 
    print(i)

#1-4 function 
def sum(c,d):
    return c + d  
print(sum(3,4))

#1-5 String (1) 
Astring = "Hello world"
Bstring = 'Hello World'
Cstring = """Hello World"""
Dstring = '''Hello World'''

#1-6 String (2)
Head = 'Hello'
Middle = ' '
Tail = 'World'
FullSentence = Head + Middle + Tail 
print(Head)
print(Middle)
print(Tail)
print(FullSentence)

#1-7 Indexing 
H = Head[0]
e = Head[1]
Worl = Tail[0:3]
World = Tail[:4]
print(H)
print(e)
print(Worl)
print(World)

hello = FullSentence[:4]
print(hello.lower())

#1-8 String Formating
print("I'm %d years old" %25)
print("I'm eating %s" %"Bread")

ages = 25
print("I'm %d" %ages)

#1-8 Function about String 
sample = "1-8 String Formating"
print(sample.count('S'))

print(sample.find('Str'))

print(sample.upper())

print(sample.lower())

sample2 = "   String Formating   "
print(sample2.lstrip())
print(sample2.rstrip())
print(sample2.strip())
#print(((sample2.strip).join(';')).split(';'))

#1-9 list type 

sample_list = [1,2,3,4,5]

print(sample_list[2])

#1-10 list function 

sample_list.append(6)
sample_list.append([7,8])
sample_list.append(9)
sample_list.append([10, 11])
print(sample_list)

sample_list.reverse()
print(sample_list)

sample_list.insert(2, [3,4,5])
sample_list.remove(3)
sample_list.remove(4)
sample_list.remove(5)
print(sample_list)



