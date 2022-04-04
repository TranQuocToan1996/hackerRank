#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen
def plusMinus(arr):
    countplus=0
    countzero=0
    for i in arr:
        if i >0:
            countplus+=1
        if i==0:
            countzero+=1
    return float(countplus/len(arr))
    return float(1-(countzero/len(arr))-(countplus/len(arr)))
    return float(countzero/len(arr))