# # nof_plates = 5
# a=[]
# b=[]
# c=[]
# # results = [a,b,c]
# for i in range(nof_plates, 0, -1):
#     a.append(i)
# # d = a
# # options = [c, b]

# # move n-1 disc from a via c to b
# # move biggest disc from a to c
# # move rest from b via a to c
# def HanoiTowers(start, via, target, n):
#     if c == d:
#         return
#     if len(c) == 0 and len(b) == 0:
#         target.append(start.pop(-1))
#         move(via,start)
#         print('part1')
#         move(via,target)
#         print(results)
#         move(target,start)
#         print(results)
#         move(start,via)
#         print(results)
#         move(target,via)
#         print(results)
#         move(target,start)
#         print(results)
#         return HanoiTowers(a,c,b,nof_plates)
#     elif len(a) > 1:
#         print('part2')
#         move(via,start)
#         print(results)
#         move(via,target)
#         print(results)
#         move(start,target)
#         print(results)
#         move(start,via)
#         print(results)
#         move(via,target)
#         print(results)
#         move(target,start)
#         print(results)
#         move(via,start)
#         print(results)
#         move(via,target)
#         print(results)
#         return HanoiTowers(a,c,b,nof_plates)
#     elif len(start) == 1:
#         print('part3')
#         target.append(start.pop(-1))
#         print(results)
#         return HanoiTowers(c,a,b,nof_plates)
#     elif n in target:
#         if len(start) == 3 or len(via) == 3:
#             print('part5')
#             move(target,start)
#             print(results)
#             move(via,start)
#             print(results)
#             move(via,target)
#             print(results)
#             move(target,start)
#             print(results)
#             move(start,via)
#             print(results)
#             move(target,via)
#             print(results)
#             move(target,start)
#             print(results)
#         else:
#             print('part4')
#             move(via,start)
#             print(results)
#             move(target,start)
#             print(results)
#             move(target,via)
#             print(results)
#             move(via,start)
#             print(results)
#             move(start,target)
#             print(results)
#             move(via,target)
#             print(results)
#             move(via,start)
#             print(results)
#             move(target,start)
#             print(results)
#             return HanoiTowers(c,b,a,nof_plates)




# def move(a,b):
#     a.append(b.pop(-1))
    

# def is_valid(source, target):
#     if source[-1] < target[-1]:
#         return True
#     else:
#         return False


# HanoiTowers(a,c,b,nof_plates)

def HanoiTowers(start, via, target, n):
    if n == 0:
        return
    HanoiTowers(start, target, via, n-1)
    print(f'disk:{n},from: {start}, to:{target}')
    HanoiTowers(via, start, target, n-1)

HanoiTowers('a','b','c',3)