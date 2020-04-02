
def cap_value (value, max_val, min_val):
    capped_value = min(value, max_val) 
    capped_value = max(capped_value, min_val)
    print(capped_value)
cap_value(, 5, 0)