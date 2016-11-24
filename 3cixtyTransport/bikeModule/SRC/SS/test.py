def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

import validators
def validateUrl(url):
    if not validators.url(url):
        return 1
    else:
        return 0


'''
def checkEqual(iterator):
  try:
     iterator = iter(iterator)
     first = next(iterator)

     if all(first == rest for rest in iterator):
         return 0
     else:
         return 1

'''

def checkEqual(lst):
   if lst[1:] == lst[:-1]:
       return 0
   else:
       return 1


iterator = ["a","a","b","c","d","e"], ["a","a","b","c","d","e"], ["a","a","b","c","d","e"]
iteratorX = ["a","a","b","c","d","e"], ["a","a","b","c","d","x"], ["a","a","b","c","d","j"]

print checkEqual(iterator)
print checkEqual(iteratorX)



test = u"51.521661"

urlTest = 'https://api-neon.tfl.gov.'


print validateUrl(urlTest)

print is_number(test)
print test.isalnum()

print test.isnumeric()
