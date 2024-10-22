def is_valid(curr_key, curr_value, important_keys):
    """
    Validates the datatype of curr_values. Datatype of curr_values should match with the one mentioned in important keys.
    """
    req_data_type = important_keys[curr_key]

    if req_data_type == "int":
        return curr_value.isnumeric()
    else:
        return curr_value.isalpha()


def process_file(lines, important_keys):
    """
    Processes the list of lines by identifying important keys in every line and verifying the datatype of values.
    Prepares a dictionary with key as type and values as list of all the dictionary of key-value pair of every line which have the same type.

    Args:
        lines: list of lines in input.txt
        important_keys: list of important keys which is inputted to the program.

    Returns:
        prepared_dict: processed data dictionary
    """
    prepared_dict = {}
    for line in lines:
        #Remove \n from the end of the string
        line = line.rstrip("\n")

        #Split string into key value pairs. Single line, comma separated values.
        key_value_pairs = line.split(",")
        validRow = True
        line_key_values = {}

        for key_value_pair in key_value_pairs:
            curr_key, curr_value = key_value_pair.split("=")
            #Only for keys which are identified as important keys 
            if curr_key in important_keys:
                #Datatype check for values
                if is_valid(curr_key, curr_value, important_keys):
                    line_key_values[curr_key] = curr_value
                else:
                    #Set flag to denote the value datatype do not match and the entire line needs to be skipped.
                    validRow = False
                    break
        
        #Skip the line if it is not valid.
        if not validRow:
            continue
        
        #Insert in prepared dict. If type already exists in dictionary, just append the new line as a dictionary of key-value pairs. Otherwise add as a new list.
        type_key = "type"
        if type_key in line_key_values:
            if line_key_values[type_key] in prepared_dict:
                prepared_dict[line_key_values[type_key]].append(line_key_values)
            else:
                prepared_dict[line_key_values[type_key]] = [line_key_values]
    return prepared_dict

def print_processed_data(prepared_dict, important_keys, hierarchy_list):
    """
    Prints comma separated values based on hierarchy

    Args:
        prepared_dict: processed data dictionary
        important_keys: list of important keys which is inputted to the program.
        hierarchy_list: hierarchy to be followed while printing

    """
    important_key_list = list(important_keys.keys())
    len_important_key_list = len(important_key_list)
    for ind in range(len_important_key_list):
        key = important_key_list[ind]
        if ind < len_important_key_list - 1:
            print(key, end=",")
        else:
            print(key)

    for curr_type in hierarchy_list:
        if curr_type in prepared_dict:
            ImportantKeyValueList = prepared_dict[curr_type]
            for KeyValuePair in ImportantKeyValueList:
                for ind in range(len_important_key_list):
                    key = important_key_list[ind]
                    if ind < len_important_key_list - 1:
                        print(KeyValuePair[key], end=",")
                    else:
                        print(KeyValuePair[key])


if __name__ == "__main__":
    with open("input.txt") as file_obj:
        lines = file_obj.readlines()

    input_important_keys = input() #Expected Format: "id:int,name:str,food:str,type:str"
    important_key_values = input_important_keys.split(",")
    important_keys = {}
    for keyValue in important_key_values:
        key, value = keyValue.split(":")
        important_keys[key] = value

    #important_keys = {"id":"int", "name":"str", "food":"str", "type":"str"}

    hierarchies = input() #Expected Format: "A->B->C"
    hierarchy_list = hierarchies.split("->")

    prepared_dict = process_file(lines, important_keys)
    print_processed_data(prepared_dict, important_keys, hierarchy_list)