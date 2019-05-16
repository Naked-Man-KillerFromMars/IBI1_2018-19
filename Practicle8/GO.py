import re
import xml.dom.minidom
import pandas as pd

DOMTree = xml.dom.minidom.parse("go_obo.xml")

collection = DOMTree.documentElement

genes = collection.getElementsByTagName('term')



genelists = [["id","name","definition","childnodes"],]
genelist = []


def Child(id, resultSet):
    for t in genes:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid,resultSet)

for gene in genes:
    defstr = gene.getElementsByTagName('defstr')[0].childNodes[0].nodeValue
    id = gene.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = gene.getElementsByTagName('name')[0].childNodes[0].nodeValue
    
    if re.search("autophagosome",defstr):
        resultSet = set()
        Child(id, resultSet)
        genelist = [id, name, defstr, len(resultSet)]
        genelists.append(genelist)
        
df = pd.DataFrame(genelists)
writer = pd.ExcelWriter('autophagosome.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='autophagosome')
writer.save()



