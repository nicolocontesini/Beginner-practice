total = 0

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

days_of_training = 0

def duration():
    while True:
        try:
            drt = (input("Duration: "))
            hrs, mins = drt.split(":")
            usvh = convertd(hrs)                      
            usvm = convertm(mins)
            usv = usvh + usvm        #"usv" stands for "usable value" (str-->float)
            return usv
                                
        
        except ValueError:
            print("duration= hrs:min")
            
               
def power():
    while True:
        try:
            pwr = float(input("Avg power output: "))
            return pwr
        except ValueError:
            print("Power is float")
                   
def heart_rate(): 
    while True:
        try:
            hr = float(input("Avg HR: "))
            return hr
            
        except ValueError:
            print("HR is float")
            
def main():
    usv = duration()
    pwr = power()
    hr = heart_rate()
    Load = load(usv, hr, pwr)
    return Load
    
def load(t, h, p):    #load math
    
    training = t + h + p 
    print(training) 
    
    if 0 < training <= 100:
        print("deload")
    elif 100 < training <= 200:
        print("maintenance")
    elif 200 < training:
        print("productive")
    return training

def convertd(d):     #conversion
    d = float(d)
    return float(d)
def convertm(m):
    m = float(m)
    return float(m / 60)

for d in days:
    print("Day of the week: ", d)
    while True:
        try:
            today = input("Did you train today? yes/no ").lower().lstrip()
            if today == "yes":                                                
                #load imported from main()
                total += main() 
                days_of_training = days_of_training + 1
                break                                       #we need to keep it running to the next day 
            elif today == "no": 
                break                                       #break and not continue because we have code below (belonging to the while loop)
            else:
                raise ValueError
        except ValueError:
            print("Type 'yes' or 'no' ")

print("Weekly load: ", total)        #recap           
avg = round(total / len(days), )
print("Average daily load: ", avg)
try:
    active_avg = round(total / days_of_training, )
    print("Average daily load (calculated only on training days): ", active_avg)
except ZeroDivisionError:
    print("Average daily load (calculated only on training days) can't be estimated since there are not active days ")








    














        









