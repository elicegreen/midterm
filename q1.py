# This function computes a customer's "minimum payment" according to the following rule:
# The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater;
# however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance. 

def computeMinimumPayment( balance ):
    if balance < 10:
        return balance
    elif balance*0.021 < 10:
        return 10
    else:
        return balance*0.021
