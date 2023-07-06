d2={"python":{"Ml":{"batch1":1,"batch2":4}},"java":"springboot"}
print("Accession python: ",d2["python"],type(d2),len(d2))
print("Accession python and ML: ",d2["python"]["Ml"],type(d2),len(d2))
print("Accession python and ML and batch1: ",d2["python"]["Ml"]["batch1"],type(d2),len(d2))
print("Accession python and ML and batch2: ",d2["python"]["Ml"]["batch2"],type(d2),len(d2))
print("Accession Java: ",d2["java"])