def main():
    read_file(prompt_file())

def prompt_file():
    """
    Asks the user for a data file
    Returns: the filename
    """
    data_file = input("Please enter the data file: ")
    print()
    return data_file

def read_file(a_file):
    """
    Reads the file and gets the rate data
    """
    with open(a_file) as f:
        first_line = f.readline()
        values = first_line.split(",")
        column_indices = {}
        for index, value in enumerate(values):
            column_indices[value] = index

        total_comm_rate = 0
        line_count = 0
        comm_rate_column_index = column_indices["comm_rate"]
        min_values = None
        max_values = None
        for line in f:
            values = line.split(",")
            comm_rate = float(values[comm_rate_column_index])
            total_comm_rate += comm_rate
            line_count += 1
            if min_values == None or float(min_values[comm_rate_column_index]) > comm_rate:
                min_values = values
            if max_values == None or float(max_values[comm_rate_column_index]) < comm_rate:
                max_values = values

        zip_column_index = column_indices["zip"]
        name_column_index = column_indices["utility_name"]
        state_column_index = column_indices["state"]   

        print("The average commercial rate is: " + str(total_comm_rate/line_count))
        print()
        print("The highest rate is:")
        print("{} ({}, {}) - ${}".format(max_values[name_column_index], max_values[zip_column_index], max_values[state_column_index], float(max_values[comm_rate_column_index])))
        print()
        print("The lowest rate is:")
        print("{} ({}, {}) - ${}".format(min_values[name_column_index], min_values[zip_column_index], min_values[state_column_index], float(min_values[comm_rate_column_index])))

if __name__ == "__main__":
    main()