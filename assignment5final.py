import os
import time

start_time = time.clock()

folder_arxiv = input('Enter the arxiv folder location (Example : C:/abc/arxiv):')
folder_jdm = input('Enter the jdm folder location (Example : C:/abc/jdm):')
folder_plos = input('Enter the plos folder location (Example : C:/abc/plos):')
stopfilelocation = input('Enter the stoplist.txt file location(Example : C:/abc/stoplist.txt):')


#First import all the training data from the arxiv folder
#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/arxiv'

i = 0
for filename in os.listdir(folder_arxiv):
    if i<=149:
        infilename = os.path.join(folder_arxiv, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        vocabulary = infile.read().split()
    i = i + 1

#print(vocabulary)
#print(len(vocabulary))

# Now we import all the training data from the jdm folder
#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/jdm'

i=0
for filename in os.listdir(folder_jdm):
    if i<=149:
        infilename = os.path.join(folder_jdm, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        vocabulary += infile.read().split()
    i = i + 1

#print(vocabulary)
#print(len(vocabulary))

# Now we import all the training data from the plos folder
#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/plos'

i = 0
for filename in os.listdir(folder_plos):
    if i<=149:
        infilename = os.path.join(folder_plos, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        vocabulary += infile.read().split()
    i = i + 1

#print(vocabulary)
#print(len(vocabulary))

# Now we import the stop text file into a new array

#infile = open('C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/stoplist.txt', 'r', encoding='UTF-8', errors='ignore')
infile = open(stopfilelocation, 'r', encoding='UTF-8', errors='ignore')
stopfilearray = infile.read().split()

#print(stopfilearray)

#Now we remove all the elements in the stopfile array from the vocabulary
vocabularycopy = [x for x in vocabulary if x not in stopfilearray]
vocabulary = vocabularycopy
vocabulary = sorted(vocabulary)
vocabulary = list(set(vocabulary))
#print(vocabulary)
print('Length of vocabulary after stop words removed : ',len(vocabulary))

#Now we convert the input articles into a set of features
w, h = 20761, 451;
classifierdataarray = [[]]
classifierdataarray = [[0 for x in range(w)] for y in range(h)]

#print(classifierdataarray[450])

#classifierdataarray = [[0] * 167346] * 450


print('Building feature set')

m = 1

#We now import the arxiv articles and create a feature vector of them, 450 subarrays and 167344 + 1 = 167345 in each subarray
#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/arxiv'

i = 1
j = 1
for filename in os.listdir(folder_arxiv):
    j = 1
    if i<=150:
        infilename = os.path.join(folder_arxiv, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        # Take the article and check if it contains words from vocabulary
        articletemparray = infile.read().split()
        articletemparray = sorted(articletemparray)
        print('ARXIV file number i = ',i)
        #print('m = ',m)
        for vocabulary_item in vocabulary:
            # print('j = ',j)
            if vocabulary_item in articletemparray:
                classifierdataarray[m][j] = 1
            else:
                classifierdataarray[m][j] = 0
            j = j + 1

    classifierdataarray[m][20760] = 'a'
    i = i + 1
    m = m + 1

#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/jdm'

i = 1
j = 1
m = 151
for filename in os.listdir(folder_jdm):
    j = 1
    if i<=150:
        infilename = os.path.join(folder_jdm, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        # Take the article and check if it contains words from vocabulary
        articletemparray = infile.read().split()
        articletemparray = sorted(articletemparray)
        print('JDM File Number i = ',i)
        #print('m = ', m)
        for vocabulary_item in vocabulary:
            # print('j = ',j)
            if vocabulary_item in articletemparray:
                classifierdataarray[m][j] = 1
            else:
                classifierdataarray[m][j] = 0
            j = j + 1

    classifierdataarray[m][20760] = 'j'
    i = i + 1
    m = m + 1

#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/plos'

i = 1
j = 1
m = 301
for filename in os.listdir(folder_plos):
    j = 1
    if i<=150:
        infilename = os.path.join(folder_plos, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        # Take the article and check if it contains words from vocabulary
        articletemparray = infile.read().split()
        articletemparray = sorted(articletemparray)
        print('PLOS file number i = ',i)
        #print('m = ', m)
        for vocabulary_item in vocabulary:
            # print('j = ',j)
            if vocabulary_item in articletemparray:
                classifierdataarray[m][j] = 1
            else:
                classifierdataarray[m][j] = 0
            j = j + 1

    #print('m = ',m)
    classifierdataarray[m][20760] = 'p'
    i = i + 1
    if m <= 449:
        m = m + 1
    else:
        break

print('Finished building feature set')
#print(classifierdataarray)


#Now we need to classify the testing data according to the training data
print('Started Classifying data')
arxiv_total_predictions = 450
arxiv_correct_predictions = 0
jdm_total_predictions = 450
jdm_correct_predictions = 0
plos_total_predictions = 450
plos_correct_predictions = 0


#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/arxiv'

width = 167345
testingtemparray = [0 for x in range(width)]
#print('length of testingtemparray is ',len(testingtemparray))
#print('testingtemparray[972] is ',testingtemparray[972])
i = 1
j = 1
for filename in os.listdir(folder_arxiv):
    if i >= 151 and i <= 300:
        arxiv_counter = 0
        jdm_counter = 0
        plos_counter = 0
        j = 1
        print('-----------------------------------------')
        #print('Testing file number i = ', i)
        print('Actual Class : ARXIV')
        infilename = os.path.join(folder_arxiv, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        inputtemparray = infile.read().split()
        inputtemparray = sorted(inputtemparray)
        for vocabulary_item in vocabulary:
            #print('j = ',j)
            if vocabulary_item in inputtemparray:
                testingtemparray[j] = 1
            else:
                testingtemparray[j] = 0
            if j<=167344:
                j = j + 1
            else:
                j = j

        for k in range(1,150):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    arxiv_counter = arxiv_counter + 1
        for k in range(151,300):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    jdm_counter = jdm_counter + 1
        for k in range(301,450):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    plos_counter = plos_counter + 1

        #print('arxiv counter : ',arxiv_counter)
        #print('jdm counter :',jdm_counter)
        #print('plos counter :', plos_counter)

        if arxiv_counter > jdm_counter  and arxiv_counter > plos_counter :
            largest = arxiv_counter
            print('Classified Class : ARXIV')
            arxiv_correct_predictions = arxiv_correct_predictions + 1
        elif jdm_counter > arxiv_counter and  jdm_counter > plos_counter :
            largest = jdm_counter
            print('Classified Class : JDM')
        else:
            largest = plos_counter
            print('Classified Class : PLOS')

    else:
        i = i

    i = i + 1

#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/jdm'

width = 167345
testingtemparray = [0 for x in range(width)]
#print('length of testingtemparray is ',len(testingtemparray))
#print('testingtemparray[972] is ',testingtemparray[972])
i = 1
j = 1
for filename in os.listdir(folder_jdm):
    if i >= 151 and i <= 300:
        arxiv_counter = 0
        jdm_counter = 0
        plos_counter = 0
        j = 1
        print('-----------------------------------------')
        #print('Testing file number i = ', i)
        print('Actual Class : JDM')
        infilename = os.path.join(folder_jdm, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        inputtemparray = infile.read().split()
        inputtemparray = sorted(inputtemparray)
        for vocabulary_item in vocabulary:
            #print('j = ',j)
            if vocabulary_item in inputtemparray:
                testingtemparray[j] = 1
            else:
                testingtemparray[j] = 0
            if j<=167344:
                j = j + 1
            else:
                j = j

        for k in range(1,150):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    arxiv_counter = arxiv_counter + 1
        for k in range(151,300):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    jdm_counter = jdm_counter + 1
        for k in range(301,450):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    plos_counter = plos_counter + 1

        #print('arxiv counter : ',arxiv_counter)
        #print('jdm counter :',jdm_counter)
        #print('plos counter :', plos_counter)

        if arxiv_counter > jdm_counter  and arxiv_counter > plos_counter :
            largest = arxiv_counter
            print('Classified Class : ARXIV')
        elif jdm_counter > arxiv_counter and  jdm_counter > plos_counter :
            largest = jdm_counter
            print('Classified Class : JDM')
            jdm_correct_predictions = jdm_correct_predictions + 1
        else:
            largest = plos_counter
            print('Classified Class : PLOS')

    else:
        i = i

    i = i + 1

#folder = 'C:/Users/Venkatesh Suvarna/PycharmProjects/DataMiningAssignment5/Assignment5InputFiles/Assignment5/articles/plos'

width = 167345
testingtemparray = [0 for x in range(width)]
#print('length of testingtemparray is ',len(testingtemparray))
#print('testingtemparray[972] is ',testingtemparray[972])
i = 1
j = 1
for filename in os.listdir(folder_plos):
    if i >= 151 and i <= 300:
        arxiv_counter = 0
        jdm_counter = 0
        plos_counter = 0
        j = 1
        print('-----------------------------------------')
        #print('Testing file number i = ', i)
        print('Actual Class : PLOS')
        infilename = os.path.join(folder_plos, filename)
        infile = open(infilename, 'r', encoding='UTF-8', errors='ignore')
        inputtemparray = infile.read().split()
        inputtemparray = sorted(inputtemparray)
        for vocabulary_item in vocabulary:
            #print('j = ',j)
            if vocabulary_item in inputtemparray:
                testingtemparray[j] = 1
            else:
                testingtemparray[j] = 0
            if j<=167344:
                j = j + 1
            else:
                j = j

        for k in range(1,150):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    arxiv_counter = arxiv_counter + 1
        for k in range(151,300):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    jdm_counter = jdm_counter + 1
        for k in range(301,450):
            for n in range(1,20759):
                if classifierdataarray[k][n] == 1 and testingtemparray[n] == 1:
                    plos_counter = plos_counter + 1

        #print('arxiv counter : ',arxiv_counter)
        #print('jdm counter :',jdm_counter)
        #print('plos counter :', plos_counter)

        if arxiv_counter > jdm_counter  and arxiv_counter > plos_counter :
            largest = arxiv_counter
            print('Classified Class : ARXIV')
        elif jdm_counter > arxiv_counter and  jdm_counter > plos_counter :
            largest = jdm_counter
            print('Classified Class : JDM')
        else:
            largest = plos_counter
            print('Classified Class : PLOS')
            plos_correct_predictions = plos_correct_predictions + 1

    else:
        i = i

    i = i + 1

print('ARXIV Total Predictions = ',arxiv_total_predictions)
print('ARXIV Correct Classifications =',arxiv_correct_predictions)
print('ARXIV Accuracy Percentage = ',(arxiv_correct_predictions/arxiv_total_predictions) * 100)
print('JDM Total Predictions = ',jdm_total_predictions)
print('JDM Correct Classifications = ',jdm_correct_predictions)
print('JDM Accuracy Percentage = ',(jdm_correct_predictions/jdm_total_predictions) * 100)
print('PLOS Total Predictions = ',plos_total_predictions)
print('PLOS Correct Classifications =',plos_correct_predictions)
print('PLOS Accuracy Percentage = ',(plos_correct_predictions/plos_total_predictions) * 100)

print(time.clock() - start_time, "seconds")