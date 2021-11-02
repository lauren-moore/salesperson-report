"""Generate sales report showing total melons each salesperson sold."""


def add_sales_to_report(txt_file):
    '''print the sales report of number of melons sold by each salesperson'''

    #open the text file
    f = open(txt_file)

    #dictionary to store salespeople annd melons sold
    melons_dict = {}

    for line in f:
        line = line.rstrip()
        entries = line.split('|')

        salesperson = entries[0]
        melons = int(entries[2])

        #add each salesperson and number of melons sold to dictionary
        melons_dict[salesperson] = melons

        if salesperson in melons_dict:
            melons_dict[salesperson] += melons
        else:
            melons_dict[salesperson] = melons
    
    return melons_dict

        

def print_sales_report(print_sales_report):
    '''print a report of the salespeople and the number of melons sold'''
  
    for salesperson, melons in print_sales_report.items():
        print(f'{salesperson} sold {melons} melons')


print_sales_report(add_sales_to_report('sales-report.txt'))