# -*- coding: utf-8 -*-
#"""
#Created on Wed Apr 17 09:06:56 2019
#
#@author: 11601
#"""
import xlrd 
blosum62 = xlrd.open_workbook('C:/Users/11601/Desktop/IBI/IBI1_2018-19/Practicle9/BLOSUM62.xlsx')
sheet1 = blosum62.sheet_by_name('Sheet1')

myDict = {'A': 1, 'R': 2, 'N': 3, 'D': 4, 'C': 5, 'Q': 6, 'E': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}

Seq1 = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
Seq2 = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
Seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

Temp1 = list(Seq1)
Temp2 = list(Seq2)


Sim = 0
Diff = 0
Score = 0

while len(Temp1) > 0:
    Temp1_pop = Temp1.pop(0)
    Temp2_pop = Temp2.pop(0)
    if Temp1_pop == Temp2_pop:
        Sim = Sim + 1
    else:
        Diff = Diff + 1
    Column1 = myDict[Temp1_pop] - 1
    Column2 = myDict[Temp2_pop] - 1
    Score = Score + sheet1.cell(Column1,Column2).value

print('Comparing human sequence and mice:')
print('edit distance = ' + str(Diff))
print('ratio of difference = ' + str(Diff/(Diff + Sim)))

print('Score is ' + str(Score))

print('                    ')

Temp1 = list(Seq1)
Temp2 = list(Seq2)
Temp3 = list(Seq3)

Sim = 0
Diff = 0
Score = 0


while len(Temp1) > 0:
    Temp1_pop = Temp1.pop(0)
    Temp3_pop = Temp3.pop(0)
    if Temp1_pop == Temp3_pop:
        Sim = Sim + 1
    else:
        Diff = Diff + 1
    Column1 = myDict[Temp1_pop] - 1
    Column2 = myDict[Temp3_pop] - 1
    Score = Score + sheet1.cell(Column1,Column2).value

print('Comparing human sequence and random:')
print('edit distance = ' + str(Diff))
print('ratio of difference = ' + str(Diff/(Diff + Sim)))

print('Score is ' + str(Score))

print('                    ')

Temp1 = list(Seq1)
Temp2 = list(Seq2)
Temp3 = list(Seq3)

Sim = 0
Diff = 0
Score = 0

while len(Temp2) > 0:
    Temp1_pop = Temp2.pop(0)
    Temp3_pop = Temp3.pop(0)
    if Temp2_pop == Temp3_pop:
        Sim = Sim + 1
    else:
        Diff = Diff + 1
    Column1 = myDict[Temp2_pop] - 1
    Column2 = myDict[Temp3_pop] - 1
    Score = Score + sheet1.cell(Column1,Column2).value

print('Comparing mice sequence and random:')
print('edit distance = ' + str(Diff))
print('ratio of difference = ' + str(Diff/(Diff + Sim)))

print('Score is ' + str(Score))