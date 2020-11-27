from client import Client
import csv
import sys


def import_file(file, contact_list):
    """
    Import Client Information from CSV File
    Create list of Client objects
    """
    with open(file, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            contact_list.append(Client(row))


def export_file(failed_list, file):
    """
    Export list of failed messages to CSV file
    """
    with open(file, mode='w', newline='') as failed_file:
        file_writer = csv.writer(failed_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in failed_list:
            file_writer.writerow(i.export_failed())


def main():
    """
    Command line arguments:
    input_file: CSV of client information
    output_file: CSV of unsuccessful sends
    """
    if len(sys.argv) != 3:
        print("Usage: main.py input_file output_file")
        exit(2)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_list = []
    failed_list = []
    success_count = 0
    import_file(input_file, input_list)

    for i in input_list:
        if i.send_message():
            success_count += 1
        else:
            failed_list.append(i)

    export_file(failed_list, output_file)

    print(f'Number of Successful Sends: {success_count}')
    print(f'Number of Unsuccessful Sends: {len(failed_list)}')


if __name__ == "__main__":
    main()
