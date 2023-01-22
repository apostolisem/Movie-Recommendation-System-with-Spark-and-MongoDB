import re
import os

def convert_combined_to_csv(filename):
    """
    It reads the combined text file, converts to comma seperated format, 
    and writes the data to a CSV file
    
    :param filename: the name of the file to be converted
    :return: The number of lines in the file.
    """
    # filenames
    filename_csv = filename.replace(".txt", ".csv")
    try:
        os.remove(filename_csv)
    except FileNotFoundError:
        pass

    # read the source file
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()

    # set params
    count = 0
    movie_id = 0
    output = []

    # write headers
    with open(filename_csv, 'a') as the_file:
        the_file.write("MovieID,UserID,Rating,Date" + "\n")

    # convert
    for line in Lines:
        count += 1
        if (re.match("\d+:", line.strip())):
            movie_id = line.strip()
        else:
            result = str(movie_id[:-1]) + "," + str(line.strip()) + "\n"
            output.append(result)
        # if (count == 10):
        #     break

    # save the file
    file1 = open(filename_csv, 'a')
    Lines = file1.writelines(output)
    file1.close()

    return(count)

# init
total_count = 0
filenames = ["combined_data_1.txt", "combined_data_2.txt", "combined_data_3.txt", "combined_data_4.txt"]

# output
print("Start converting. Please wait... ", end="")
for filename in filenames:
    total_count += convert_combined_to_csv(filename)    
print("Done => converted {} records".format(total_count))
