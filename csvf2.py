import csv

# def writing(fileobj,data):
# 	pen = csv.writer(fileobj,delimiter = ',')
# 	print(pen)
# 	for a in data:
# 		print(a)
# 		pen.writerow(a)


#DictReader(fileobj,delimiter=',')
def getdata(fileobj):
    csv_reader = csv.DictReader(fileobj,delimiter=',')
    # print(next(csv_reader))
    for line in csv_reader:
    # 	print(a)
    	print(line['name'])
    	print(line['class'])
    	print(line['ph.No'])
    	print(line['address'])
    	print(60*'-')


if __name__ =='__main__':
	fileobj = open('info.csv','r')
	data = ['name,class,ph.No,address'.split(','),
	'superman,JL,802-4840-9283,USA'.split(','),
	'batman,JL,791-8468-8264,USA'.split(','),
	'wonderwomen,JL,397-2478-2834,USA'.split(','),
	'aquaman,JL,792-2893-1379,USA'.split(',')]
	# print(data)

	# print(fileobj)
	getdata(fileobj)
	# writing(fileobj,data)
#fileobj=open('details.csv','r')