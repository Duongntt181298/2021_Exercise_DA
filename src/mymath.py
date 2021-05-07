import numpy as np 
import pandas as pd

def tan_xuat_xuat_hien_nhieu_nhat(_list):
    list_sorted = sorted(_list)
    _max = 1
    count = 1
    for i in range(1,len(list_sorted)):
        if list_sorted[i] == list_sorted[i-1]:
            count+=1
            _max = max(_max,count)
        else:
            count = 1
            
    frequencies = {i: list_sorted.count(i) for i in list_sorted}
    mode = [i for i in frequencies if frequencies[i] == _max]
    return mode

def tinh_giai_thua(a):
    tempt = 1
    for i in range(2,a+1):
        tempt = tempt*i
    return tempt

def check_so_nguyen_to(a):
    count = 0
    for i in range(2,a):
        if a%i == 0:
            count+=1
            print(f"{a} không là số nguyên tố")
            break
    if count == 0:
        print(f"{a} là số nguyên tố")

def check_so_chinh_phuong(a):
    sqrt_a = math.sqrt(a)
    if sqrt_a*sqrt_a == a:
        print(f"{a} là số chính phương")
    else:
        print(f"{a} không là số chính phương")