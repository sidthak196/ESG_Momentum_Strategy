import pandas as pd

#Get data form the file and collate with ESG

# Price_Data = pd.read_excel("H:/My Drive/Projects/ESG_Momentum_Strategy/Data/StockPrice.xlsx")
# Price_Data.head()

def solution(area):
    # Your code here
    flag = 1
    new_area = area
    l = []
    while(new_area>0):
        for i in range(1,new_area+1):
            p=max(i-1,1)
            if (i*i)<=new_area:
                continue
            break
        l.append(p*p)
        new_area = new_area - (p*p)
            
    return l
    
print(solution(12))
