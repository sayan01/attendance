#!/bin/env python3
import sys

al1 = ['21BCAA01','21BCAA03','21BCAA04','21BCAA07','21BCAA16','21BCAA24','21BCAA25','21BCAA28','21BCAA33','21BCAA36','21BCAA37','21BCAA41','21BCAA42','21BCAA47','21BCAA49','21BCAA52','21BCAB01','21BCAB03','21BCAB04','21BCAB05','21BCAB12','21BCAB17','21BCAB20','21BCAB30','21BCAB37','21BCAB43','21BCAB45','21BCAB46','21BCAB52','21BCAB55','21BCAC02','21BCAC05','21BCAC09','21BCAC18','21BCAC20','21BCAC29','21BCAC34','21BCAC41','21BCAC47','21BCAC51','21BCAC55','21BCAC59','21BCAD01','21BCAD04','21BCAD06','21BCAD11','21BCAD12','21BCAD17','21BCAD18','21BCAD20','21BCAD21','21BCAD25','21BCAD27','21BCAD33','21BCAD38','21BCAD43','21BCAD45','21BCAD46','21BCAD50','21BCAD51','21BCAD57','21BCAD58']
al2 = ['21BCAE04','21BCAE10','21BCAE19','21BCAE20','21BCAE24','21BCAE30','21BCAE32','21BCAE35','21BCAE36','21BCAE42','21BCAE44','21BCAE55','21BCAF04','21BCAF11','21BCAF14','21BCAF23','21BCAF29','21BCAF34','21BCAF36','21BCAF37','21BCAF48','21BCAF49','21BCAF50','21BCAF51','21BCAF56','21CSMM05','21CSMM07','21CSMM10','21CSMM13','21CSMM16','21CSMM35','21CSMM37','21CSMM42','21CSMM45','21CSMM46','21CSMM47','21CSMM53','21PHCS02','21PHCS04','21PHCS11','21PHCS13','21PHCS18','21STMM10','22BCAA08','22BCAA15','22BCAA17','22BCAA19','22BCAA20','22BCAA24','22BCAA25','22BCAA30','22BCAA32','22BCAA36','22BCAA42','22BCAA44','22BCAA45','22BCAA46','22BCAA47','22BCAA50','22BCAA54','22BCAA58','22BCAA59','22BCAA60','22BCAA69','22BCAA71']
m12 = ['22BCAB01','22BCAB03','22BCAB04','22BCAB05','22BCAB08','22BCAB11','22BCAB14','22BCAB17','22BCAB19','22BCAB20','22BCAB22','22BCAB26','22BCAB27','22BCAB29','22BCAB30','22BCAB32','22BCAB33','22BCAB34','22BCAB39','22BCAB44','22BCAB45','22BCAB47','22BCAB50','22BCAB51','22BCAB53','22BCAB54','22BCAB55','22BCAB56','22BCAB57','22BCAB58','22BCAB60','22BCAB61','22BCAB64','22BCAB67','22BCAB69','22BCAB70','22BCAC03','22BCAC24','22BCAC29','22BCAC35','22BCAC37','22BCAC49','22BCAC53','22BCAC54','22BCAC66','22BCAD01','22BCAD04','22BCAD08','22BCAD17','22BCAD18','22BCAD20','22BCAD21','22BCAD23','22BCAD26','22BCAD41','22BCAD46','22BCAD47','22BCAD49','22BCAD57','22BCAD60','22BCAD62','22BCAD64','22BCAD67','22BCAD68','22BCAD69','22BCAD70','22BCAD71','22BCAE03','22BCAE05','22BCAE13','22BCAE19','22BCAE24','22BCAE29','22BCAE30','22BCAE32','22BCAE34','22BCAE36','22BCAE40','22BCAE43','22BCAE46','22BCAE54','22BCAE63','22BCAE64','22BCAE66','22BCAE68','22BCAE69','22BCAF01','22BCAF03','22BCAF06','22BCAF15','22BCAF16','22BCAF25','22BCAF32','22BCAF71','22CDSA03']
m5 = ['22CDSA06','22CDSA10','22CDSA11','22CDSA12','22CDSA13','22CDSA14','22CDSA18','22CDSA20','22CDSA21','22CDSA24','22CDSA35','22CDSA36','22CDSA52','22CDSA59','22CDSA60','22CSEL05','22CSEL07','22CSEL09','22CSEL13','22CSEL16','22CSEL24','22CSEL25','22CSEL27','22CSEL29','22CSEL36','22CSEL38','22CSEL39','22CSEL42','22CSMM02','22CSMM04','22CSMM05','22CSMM10','22CSMM17','22CSMM22','22CSMM26','22CSMM33','22CSMM37','22CSMM43','22CSMM47','22CSMM48','22CSMM49','22CSMM50','22CSMM53','22CSMM54','22CSMM55','22CSMM56','22CSMM58','22CSMM60','22CSMM61','22CSMM63','22CSMM64','22CSMM68','22CSMM73','22CSMM74','22CSMM76','22CSMM77','22PHCS02','22PHCS06','22PHCS08']


print("Venue? \n1.AL1\n2.AL2\n3.M12\n4.M5\nEnter: ", end="")
inp = int(input()[0])
attn = []
venue = al1 if inp == 1 else al2 if inp == 2 else m12 if inp == 3 else m5 if inp == 4 else []
if not venue: exit(0)
while True:
    num = input("Enter regno: ").upper()
    if num in attn:
        print("Already taken.")
    elif not num:
        break
    elif num in venue:
        attn.append(num)
        print("??? attendance taken")
    elif num in al1:
        print("??? Student is supposed to be in AL1, not here")
    elif num in al2:
        print("??? Student is supposed to be in AL2, not here")
    elif num in m12:
        print("??? Student is supposed to be in M1, not here")
    elif num in m5:
        print("??? Student is supposed to be in M5, not here")
    else:
        print("??? Invalid Participant")

print("Attendance of", ["AL1", "AL2", "M12", "M5"][inp-1],": ")
for stud in attn:
    print(stud)

