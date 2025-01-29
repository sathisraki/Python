#!/usr/bin/python3.12

def decor_result(result_function):
    def distinction(marks):
        results = []
        for m in marks:
            if m > 75:
                print("Distinction")
                results.append("Distinction")
            else:
                results.append(result_function([m]))
        return results
    return distinction

@decor_result
def result(mark):
    for m in mark:
        if m > 33:
            #print("PASS")
            return "PASS"
        else:
            #print("FAIL")
            return "FAIL"

results =  result([45,70,80,32,66,90])
print("Results:", results)
