"""Generate sales report showing total melons each salesperson sold."""


def print_sales_report(txt_file):
    '''print the sales report of number of melons sold by each salesperson'''

    f = open(txt_file)

    melons_dict = {}

    for line in f:
        line = line.rstrip()
        entries = line.split('|')

        salesperson = entries[0]
        melons = int(entries[2])

        melons_dict[salesperson] = melons

    for salesperson, value in melons_dict.items():
        print(f"{salesperson} sold {value} melons.")

print_sales_report("sales-report.txt")