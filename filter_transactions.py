import csv, datetime

offers_file = open('data/offers.csv')
transactions_file = open('data/transactions10K.csv')
reduced_file = open('data/transactions10K_reduced.csv', 'w')

offers_reader = csv.reader(offers_file)
transactions_reader = csv.reader(transactions_file)
reduced_reader = csv.writer(reduced_file)

offer_categories = {}
next(offers_reader)			# Skip Headers
for offer in offers_reader:
	offer_categories[offer[1]] = 1

# Write Header
reduced_reader.writerow(transactions_reader.next())

line = 0
for t in transactions_reader:
	line = line + 1
	if(offer_categories.has_key(t[3])):
		reduced_reader.writerow(t)
	if(line == 1000000):
		print "Processing line: " + str(line) + " at " + str(datetime.datetime.now())

offers_file.close()
transactions_file.close()
reduced_file.close()