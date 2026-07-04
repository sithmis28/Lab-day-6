weight=float(input("enter_baggage_weight;"))
if weight<=20:
    print("no_charge")
elif 21<= weight <=30:
    extra_weight=weight-20
    charge = extra_weight*200
    print("extra_charge: Rs",charge)
else:
    print("The baggage is not allowed")
 
