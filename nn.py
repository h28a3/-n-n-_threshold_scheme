
#-------01/2-------#
def mapping(share):
    leakage = []
    for c in share:
        x = []
        for j in range(len(c)):
            if(c[j] > p/2):
                x.append(1)
            else:
                x.append(0)
        leakage.append(x)
    return leakage

#-------01/2-------#
# def mapping(share):
    # leakage = []
    # for c in share:
    #     x = []
    #     for j in range(len(c)):
    #         if(c[j] < p/3):
    #             x.append(0)
    #         elif(c[j] < 2*p/3):
    #             x.append(1)
    #         else:
    #             x.append(2)
    #     leakage.append(x)
    # return leakage

import itertools
import pandas as pd
import numpy as np

#�Q���Ґ�
n = 5
#�L���̂̃T�C�Y
p = 3

#leakage�̏W��
leakages = []

#leakage�̑S��
pat = []
nums = [0,1]
for c in itertools.product(nums, repeat = n):
    pat.append(list(c))

nums = range(p)
#print(pat)

for i in range(p):
    #secret
    s = i
    
    #share�̏W��
    share = []
    for c in itertools.product(nums, repeat = n - 1):
        x = []
        sum_x = 0
        for j in range(n - 1):
            x.append(c[j])
            sum_x = sum_x + c[j]
        x.append((s - sum_x) % p)
        share.append(x)
        
    #leakage�̐���
    leakage = mapping(share)
    
    #share�P���Ƃ̊m��
    pr = p ** (1 - n)
    
    #leakage�̑S�p�^�[���̌��J�E���g
    counter = []
    for j in range(len(pat)):
        counter.append(leakage.count(pat[j]))  
    
    #print(counter)
    
    #leakage�̑S�p�^�[���̊m���v�Z
    leakage = []
    for j in range(len(counter)):
        leakage.append(pr * counter[j])
    leakages.append(leakage)

#secret���Œ肵���Ƃ��̓��v����
def SD(x,y):
    ans = 0
    for i in range(len(x)):
        ans = ans + abs(x[i] - y[i])
    return ans

#�S�Ă�secret�̓��v����
def SD_array(x):
    ans = []
    for i in range(len(x)):
        ans0 = []
        for j in range(len(x)):
            ans0.append(SD(x[i], x[j]))
        ans.append(ans0)
    return ans

index = []
for i in range(p):
    index.append("s = "+str(i))
df = pd.DataFrame(SD_array(leakages), index=index, columns=index)
print(df)

#np.amax(SD_array(leakages))