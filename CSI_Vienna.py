with open("dna.txt", "r") as dna_file:
    evidence = dna_file.read()

profile = []

gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}
hair_color = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
eye_color = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
facial_shape = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
characteristics = [gender, race, hair_color, eye_color, facial_shape]

for i in characteristics:
    for j in i:
        if i[j] in evidence:
            profile.append(j)


print("The suspect is a " + profile[1] + " " + profile[0] + " with " + profile[2] + " hair, " + profile[3] + " eyes and " + profile[4] + " face.")

guilty = {"gender" : profile[0], "race" : profile[1], "hair_color" : profile[2], "eye_color" : profile[3], "facial_shape" : profile[4]}

suspect1 = {"gender" : "female", "race" : "white", "hair_color" : "blonde", "eye_color" : "blue", "facial_shape" : "oval", "name" : "Eva"}
suspect2 = {"gender" : "female", "race" : "white", "hair_color" : "brown", "eye_color" : "brown", "facial_shape" : "oval", "name" : "Larisa"}
suspect3 = {"gender" : "male", "race" : "white", "hair_color" : "black", "eye_color" : "blue", "facial_shape" : "oval", "name" : "Matej"}
suspect4 = {"gender" : "male", "race" : "white", "hair_color" : "brown", "eye_color" : "green", "facial_shape" : "square", "name" : "Miha"}

suspects = [suspect1, suspect2, suspect3, suspect4]

for susp in suspects:
    for k in susp:
        verdict = {k: susp[k] for k in susp if k in guilty and susp[k] == guilty[k]}
    if len(verdict) < 5:
        print(susp["name"] + " is not guilty.")
    else:
        print(susp["name"] + " ate the icecream. Arrest him/her right away!!!")

