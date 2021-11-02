"""Generate sales report showing total melons each salesperson sold."""

#lists to store names and melons sold
#suggestion: dictionary to store both would be ideal
salespeople = []
melons_sold = []

melons_dict = {}

#open file and separate salesperson from melons sold into string and int, respectively
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    melons_dict[salesperson] = melons


    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
