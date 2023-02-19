import math

# for i in range(100):
#     ii=10*i

#     print(ii, end=" ")
#     print(ii, end=" ")

#     print(ii+10, end=" ")
#     print(ii, end=" ")

#     print(ii+10, end=" ")
#     print(ii+10, end=" ")

#     print(ii, end=" ")
#     print(ii+10, end=" ")

#     print(ii, end=" ")
#     print(ii, end=" ")




# for i in range(64):
#     ii = 20*i

#     print('0 0', end=" ")
    
#     print(1024-ii, end=" ")
#     print(0, end=" ")

#     print(1024-ii, end=" ")
#     print(1024-ii, end=" ")

#     print(0, end=" ")
#     print(1024-ii, end=" ")

# stp = 64
# for i in range (stp):
#     deg = i  * 2 * math.pi /stp 
#     print (f'{512} {512}' , end=" ")
#     print (f'{512+int(256*math.sin(deg))} {512+int(256*math.cos(deg))}' , end=" ")


for i in range (100000):
    print(f'{i%10} {i%10} ', end='')
    print(f'{0} {0} ', end='')
