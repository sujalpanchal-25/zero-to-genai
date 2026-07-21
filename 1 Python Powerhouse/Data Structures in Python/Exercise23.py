# Exercise 23 
def key_with_max_value(d):
   if not d:
    return "Empty Dictionary"
   
   key = list(d)
    
   max_k = key[0]
   max_v = d[max_k]

   for i in d:
    if d[i] > max_v:
        max_v = d[i]
        max_k = i
    
   return max_k