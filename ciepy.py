
subject=input("What subject do you want past papers for? [Choose from Maths, Chemistry and Physics] ")
if subject=="Maths":
    subjectcode="9709"
    subjectname="Mathematics (9709)"
elif subject=="Chemistry":
    subjectcode="9701"
    subjectname="Chemistry (9701)"
elif subject=="Physics":
    subjectcode="9702"
    subjectname="Physics (9701)"

year=input("Which year is the past paper from? ")
yearlast=year[-2::]
session=input("Which session is the question paper from? [s for May/June, m for March, w for October/November] ")

variant=input("What is the variant and paper of the question paper? [Example: 13 for Pure Maths 1 Variant 3] ")

type=input("Do you want the mark scheme or question paper? ")
if type=="Mark scheme":
    typevar="ms"
elif type=="Question paper":
    typevar="qp"
    

print("https://papers.gceguide.com/A Levels/"+subjectname+"/"+year+"/"+subjectcode+"_"+session+yearlast+"_"+typevar+"_"+variant+".pdf")
input("Enter any key to exit: ")