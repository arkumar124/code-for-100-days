p_amt=float(input('Enterprinciple amount:'))
rate=(float(input('Enter the rate:')))/100
time=int(input('Enter the time in years:'))
time_div=int(input('compounded number per year:'))
intrest=p_amt*((1+rate/time_div)**(time_div*time)) - p_amt
print('Compound interest is: rs'+str(intrest))