
x = 10        
y = 3.14
z = 2 + 3j     
print(f"int: {x}, float: {y}, complex: {z}")


s = "Python"              
l = [1, 2, 3, 4]           
t = (10, 20, 30)           
print(f"str: {s}, list: {l}, tuple: {t}")


s1 = {1, 2, 3, 4}          
fs = frozenset([5, 6, 7])  
print(f"set: {s1}, frozenset: {fs}")


d = {"name": "Alice", "age": 25}  
print(f"dict: {d}")


b1 = True
b2 = False
print(f"bool: {b1}, {b2}")


by = b"hello"              
ba = bytearray([1, 2, 3])    
mv = memoryview(by)         
print(f"bytes: {by}, bytearray: {ba}, memoryview: {list(mv)}")


n = None
print(f"NoneType: {n}")


print(f"Type of x: {type(x)}")   
print(f"Type of s: {type(s)}")   
print(f"Type of fs: {type(fs)}") 


l[0] = 42
print(f"Modified list: {l}")  


try:
    t[0] = 42
except TypeError as e:
    print(f"Error: {e}")  
