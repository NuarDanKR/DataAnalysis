a,b=map(int, input().split())

power_list= [2**i for i in range(a,b+1) if a<b and 0<a<21 and 9<b<31]
'''
power_list.pop(1)
power_list.pop(len(power_list)-1)
'''

del power_list[1],power_list[-2]

print(power_list) 