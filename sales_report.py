"""Generate sales report showing total melons each salesperson sold."""

# creates empty list that will hold names of salespeople
salespeople = []
# creates empty list that will hold total melons sold (by each salesperson)
melons_sold = []

# opens the sales-report file and saves it as a variable
f = open('sales-report.txt')
# iterates over each line in the file that was opened
for line in f:
    # removes trailing characters from the right end of each line
    line = line.rstrip()
    # splits each line on the pipe character and saves strings in a list
    entries = line.split('|')

    # defines salesperson name as being the string at entries at 0
    salesperson = entries[0]
    # defines melons variable as being the string at entries at 2, and converts
    # data type to variable. contains # of melons sold
    melons = int(entries[2])

    # checks to see if salesperson name already appears in salespeople list
    if salesperson in salespeople:
        # if it is, returns the index of that salesperson's name as the variable
        # position
        position = salespeople.index(salesperson)

        # adds the number of melons sold (from entries list) to the melons sold
        # at the same index (position) in melons_sold as the salesperson's
        # name in salespeople
        melons_sold[position] += melons

    # if their name isn't already in salespeople
    else:
        # adds them to the salespeople list
        salespeople.append(salesperson)
        # adds # of melons sold from entries to the melons sold list. But how
        # can we be sure it's at the same index as the above line?
        melons_sold.append(melons)

# iterates over a range of ints from 1 - however many salespeople there are
for i in range(len(salespeople)):
    # prints each salesperson's name and how many melons they sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
