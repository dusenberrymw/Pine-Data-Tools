#! /usr/bin/env python3
"""
Preprocess csv data, line by line

    -Reads from csv input_file, and writes to new csv output_file

Usage:
    proprocess.py <input_file.csv> <output_file.csv> [<headers_present = 0>]
                  [<skip_missing_or_incorrect_data = 1>] [<default_value = 0>]

"""
import csv
import sys

def process_csv(input_file, output_file, headers_present=0,
                skip_missing_or_incorrect_data=1, default_value=0):
    pos_values = ['y','yes','positive','abnormal','male','m','t']
    neg_values = ['n','no','negative','normal','female','f','none']

    with open(input_file) as i, open(output_file, 'w') as o:
        reader = csv.reader(i)
        writer = csv.writer(o)

        if headers_present:
            new_headers = process_headers(next(reader))
            writer.writerow(new_headers)

        for line in reader:
            processed_line = process_line(line, pos_values, neg_values,
                                          skip_missing_or_incorrect_data,
                                          default_value)
            if processed_line:  # if list not empty
                writer.writerow(processed_line)


def process_headers(headers):
    new_headers = []
    for item in headers:
        item = (item.strip().replace(" ", "_").replace("|", "_")
                    .replace(":", "_").replace("?", ""))
        new_headers.append(item)
    return new_headers


def process_line(line, pos_values, neg_values, skip_missing_or_incorrect_data=1,
                 default_value=0):
    processed_line = []
    for item in line:
        item = item.strip().lower()
        if item in pos_values:
            item = 1
        elif item in neg_values:
            item = 0
        else:
            # this line is missing a data point
            if skip_missing_or_incorrect_data:
                # skip line
                processed_line = []
                break # return empty list
            else:
                item = default_value
        processed_line.append(item)
    return processed_line


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    headers_present = 0
    skip_missing_or_incorrect_data = 1
    default_value = 0

    try:
        headers_present = int(sys.argv[3])
        skip_missing_or_incorrect_data = int(sys.argv[4])
        default_value = int(sys.argv[5])
    except IndexError:
        pass

    process_csv(input_file, output_file, headers_present,
                skip_missing_or_incorrect_data, default_value)
