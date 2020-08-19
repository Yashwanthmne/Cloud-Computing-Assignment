import csv 

subjectInfo ={}


with open('studentInfo.csv', 'r', encoding="utf-8-sig") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    # print(list_of_rows)
    studentInfo = list_of_rows

with open('subjectInfo.csv', mode='r', encoding="utf-8-sig") as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        subjectInfo = {rows[0]:rows[1] for rows in reader}
# print(subjectInfo["SUBJECT"])
masterlist =[]

for row in studentInfo:
	if row[0] == "NAME":
		continue
	#As soon as we get a student info we figure out the year
	if int(row[2]) % 2 != 0:
		year = (int(row[2]) + 1)/2
	else:
		year = int(row[2])/2
	year = int(year)

	#Now that we have the year, we need to figure out the Dept this student is in
	dept = row[1][0:2]
	# print(dept)

	#That simple, now we have sufficient information to allot subjects
	#let's create a key we can use to search the course

	phrase = dept + str(year)
	student = [row[1], row[0]]

	for key, value in subjectInfo.items():
		# print(value[0:3]
		if key == "SUBJECT":
			continue
		if value[0:3] == phrase:
			# print(key, "   ", value)
			student.extend([key, value])

	masterlist.append(student)

for r in masterlist:
	print(r, "\n")




