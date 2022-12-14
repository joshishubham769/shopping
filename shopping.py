import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
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
            
            if line[17]=="TRUE":
                label.append(1)
            else:
                label.append(0)
    
    return evidence,label


def train_model(X_train,y_train):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model =KNeighborsClassifier(n_neighbors=1)
    if model.fit(X_train,y_train):
        return model
    
    
    
    


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    correct_true=0
    total_true=0
    correct_false=0
    total_false=0
    
    for actual,predicted in zip(labels,predictions):
        if actual==1:
            if actual==predicted:
                correct_true=correct_true+1
            total_true=total_true+1
        elif actual==0:
            if actual==predicted:
                correct_false=correct_false+1
            total_false=total_false+1
            
    
    if total_true==0:
        sensitivity=1
    else:
        sensitivity=correct_true/total_true
    if total_true==0:
        specificity=1
    else:
        specificity=correct_false/total_false
    
    return (sensitivity,specificity)


if __name__ == "__main__":
    main()
