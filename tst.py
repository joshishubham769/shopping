import csv

month={"Jan":0,"Feb":1,"Mar":2,"Apr":3,"May":4,"June":5,"Jul":6,"Aug":7,"Sep":8,"Oct":9,"Nov":10,"Dec":11}
evidence=[]
label=[]
with open("shopping.csv","rt") as f:
    reader=csv.reader(f)
    next(reader)
    
    for line in reader:
        lst=[line[0],line[1],line[2],line[3],line[3],line[4],line[5],line[6],line[7],line[8],line[9]]
        lst.append(month[line[10]])
        lst=lst+[line[11],line[12],line[13],line[14]]
        
        if line[15]=="Returning_Visitor":
            lst=lst+[1]
        else:
            lst=lst+[0]
            
        if line[16]=="Weekend":
            lst=lst+[1]
        else:
            lst=lst+[0]
            
        evidence.append(lst)
        
        if line[17]==True:
            label.append(1)
        else:
            label.append(0)
            
print(evidence)
print(label)