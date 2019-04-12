#! /usr/bin/env python3

#1
def sleep_in(weekday, vacation):
  if vacation or not weekday:
    return True
  if not vacation and weekday:
    return False

sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)

#2
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False

monkey_trouble(True, True)
monkey_trouble(False, False)
monkey_trouble(True, False)

#3
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

sum_double(1,2)
sum_double(3,2)
sum_double(2,2)

#4
def diff21(n):
  if n <= 21:
    return abs(n - 21)
  else:
    return abs(n - 21) * 2

diff21(19)
diff21(10)
diff21(21)

#5
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False

parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False,6)

#6
def makes10(a, b):
  if a + b is 10:
    return True
  elif a is 10 or b is 10:
    return True
  else:
    return False

makes10(9,10)
makes10(9,9)
makes10(1,9)

#7
def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10

def pos_neg(a, b, negative):
  if not negative:
    return ((a >= 0 and b < 0) or (a < 0 and b >= 0))
  else:
    return a < 0 and b < 0

pos_neg(1,-1, False)
pos_neg(-1,1, False)
pos_neg(-4,-5, True)

#8
def not_string(str):
  if str.split()[0] is 'not':
    return str
  else:
    return "not {}".format(str)

not_string("candy")
not_string("x")
not_string("not bad")

#9
def missing_char(str, n):
  if len(str) > 0 and n <= len(str)-1:
    return str.replace(str[n],'',1)
  else:
    return str

missing_char("kitten", 1)
missing_char("kitten", 0)
missing_char("kitten", 4)

#10
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

front_back('code')
front_back('a')
front_back('ab')

#11
def front3(str):
  return str[0:3] * 3

#12
def string_times(str, n):
  if n >= 0:
    return str * n
  else:
    return str

#13
def front_times(str, n):
  if n >= 0:
    return str[0:3] * n
  else:
    return str

#14
def string_bits(str):
  new_str = ''
  for i in range(0, len(str), 2):
      new_str += str[i]

  return new_str

#15
def string_splosion(str):
  created = ''
  for i in range(0, len(str) + 1):
    created += str[0:i]

  return created

#16
def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count += 1

  return count

#17
def array_front9(nums):
  if len(nums) < 4:
    return 9 in nums
  else:
    return 9 in nums[:4]
