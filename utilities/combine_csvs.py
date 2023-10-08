from csv import writer
import os

def combine_csvs(csv_name_list, output_csv_name, has_headers=True):
    prefix = os.getcwd()
    with open(prefix + "/" + output_csv_name, 'a') as write_f_object:
        writer_obj = writer(write_f_object)
        for i, csv_name in enumerate(csv_name_list):
            with open(csv_name, 'r') as read_f:
                for j, line in enumerate(read_f):

                    if has_headers and j == 0:
                        continue

                    writer_obj.writerow(line.rstrip().split(','))
            read_f.close()
        write_f_object.close()

if __name__ == '__main__':
    names = [
        # 'size_9_games/v1/2005/2005-features.csv',
        'size_9_games/v1/2006/2006-features.csv',
        'size_9_games/v1/2007/2007-features.csv',
        'size_9_games/v1/2008/2008-features.csv',
    ]
    output_csv = '/size_9_games/v1/2006-2008-moveone.csv'
    combine_csvs(names, output_csv)
