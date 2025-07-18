# time module

print("Hello World")

import time

# initial1 = time.time()
# i = 0
# while(i<45):
#     if i < 10:
#         print(f"{i} . Where to go")
#         i+=1
#         continue
#     print(f"{i}. Where to go")
#     i +=1
# print("Time required for while loop:",time.time() - initial1)
#
# print()
#
# initial2 = time.time()
# for i in range(45):
#     if i < 10:
#         print(f"{i}  . It's Hitesh")
#     else:
#         print(i,".","It's Hitesh")
# print("Time required for for loop:",time.time() - initial2)

# for i in range(20):
#     print("Its Hitesh Haridas Gawande")
#     time.sleep(1)

# local_time_test = time.asctime(time.localtime(time.time()))
# print(local_time_test)
# print(time.asctime())
# print(time.ctime())

local_time = time.localtime()
print(local_time)
print(time.strftime("%d-%m-%y %H:%M:%S",local_time))

start = time.perf_counter()
for i in range(1000000):
    pass
end = time.perf_counter()
print(f"Time required to run for loop {end - start:.4f}")
