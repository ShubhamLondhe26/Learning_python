#nested dictonary
d1={"python":{"batch1","batch2"},"java":"batch2"}
print(d1,type(d1),len(d1))
print("Accession: ",d1["python"])
d2={"python":{"ML":"batch2"},"data analytics":{"power bi":"visualization"}}
print(d2,type(d2),len(d2))
print("Accession python: ",d2["python"])
print("Accession python and ML: ",d2["python"]["ML"])

print("Accession data analytics: ",d2["data analytics"])
print("Accession data analytics and power: ",d2["data analytics"]["power bi"])