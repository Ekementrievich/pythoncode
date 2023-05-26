import csv

def filter_csv_data(input_file, output_file, month):
    filtered_data = []

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row

        if len(header) > 4:
            for row in reader:
                if row[1].split('/')[1] == month or row[2].split('/')[1] == month:
                    filtered_data.append(row)

    filtered_data.sort(key=lambda x: x[0])  # Sort the filtered data by name

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Birthday', 'Anniversary', 'Phone Number'])  # Write the header row

        for row in filtered_data:
            writer.writerow([row[0], row[1], row[2], row[3]])

    print(f"Filtered data for month {month} has been saved to {output_file}.")


# Example usage
input_file = 'data.csv'
output_file = 'filtered_data.csv'
user_month = input("Enter the month (e.g., 01 for January): ")

filter_csv_data(input_file, output_file, user_month)
