import csv

# Specify the indices of the headers you want to keep
headers_title = [0, 1, 2, 3, 5, 17]  # Adjust these indices as needed


PHONE_INDEX = 5

# Open the original CSV file and a new CSV file to write the filtered data
with open('csv_files/apollo-contacts-export (1).csv', 'r') as infile, open('csv_files/filtered_contacts.csv', 'w', newline='') as outfile:
    csvreader = csv.reader(infile)
    csvwriter = csv.writer(outfile)

    # Read the header
    header = next(csvreader)

    # Filter the header based on the specified indices
    filtered_header = [header[i] for i in headers_title]
    # Write the filtered header to the new file
    csvwriter.writerow(filtered_header)

    # Read and filter each row
    for row in csvreader:
        filtered_row = [row[i] for i in headers_title]

        if filtered_row[PHONE_INDEX]:
            filtered_row[PHONE_INDEX] = filtered_row[PHONE_INDEX].replace(
                "'", '')
            # Write the filtered row to the new file
            csvwriter.writerow(filtered_row)
