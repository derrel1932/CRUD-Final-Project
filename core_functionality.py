import csv

# READ THE FILE AND LOAD THE CONTENTS INTO THE PROGRAM'S DICTIONARY
def read_n_dict(file_path, main_key, groupables, ranked_field, rank_storage):
    main_dict = {}
    group_dict = {}
    # good practice to use with when opening files to properly auto close the file after use !
    with open(file_path, 'r', newline='', encoding='utf-8') as file_:
        # This CRUD is very field name dependent so we need to use DictReader to abstract away unneccessary complexity
        reader = csv.DictReader(file_)
        # append the ranked field to groupables to make ranking easy
        groupables.append(ranked_field) 
        # initialize the group_dict
        for fieldname in groupables: group_dict[fieldname] = {}
        
        # populate the main dictionary and group
        for row_ in reader:
            name = row_.pop(main_key) # the Name field becomes the keys
            row_[ranked_field] = int(row_[ranked_field]) # convert these as numerical value
            row_[rank_storage] = int(row_[rank_storage]) # convert these as numerical value
            main_dict[name] = row_ # main contains all the fields as value of each Name as key

            for group in groupables: # populate the group_dict
                group_name = row_[group] # get the name of the current row's group
                if group_name not in group_dict[group]: # create the list if it havent existed yet
                    group_dict[group][group_name] = [name] # This creates the first list of names!
                else : group_dict[group][group_name].append(name) # just append otherwise
        # return the dicts and fieldname
        return reader.fieldnames, main_dict, group_dict



# Write back to file from the dictionaries
def write_dicts(file_path, headers, main_key, main_dict, group_dict, ranked_field, stored_rank):
    with open(file_path, "w", newline='', encoding='utf-8') as file_:
        # get the rank sorted out in decending order
        ranked_values = list(group_dict[ranked_field].keys())
        ranked_values.sort(reverse=True)

        # prepare the writer and write the header first
        writer = csv.DictWriter(file_, fieldnames=headers)
        writer.writeheader()

        # write to file based on the sorted ranks
        for rank, value in enumerate(ranked_values):
            # get the names first stored in group_dict
            list_of_names = group_dict[ranked_field][value]
            # if there are more than one name with the same ranked score 
            # then it is considered the same ranking
            for name in list_of_names:
                main_dict[name][stored_rank] = rank + 1 # set the rank first
                writer.writerow({main_key : name, **main_dict[name]}) # WRITE !

# make it easy to prompt numerical values
def get_numeric(prompt_string):
    while True:
        try :
            return float(input(prompt_string))
        except ValueError:
            continue

# debug tools
def get_by_major_group(dict_, major_group):
    print(f"<<< {major_group} >>>")
    for target_ in dict_[major_group]:
        print(f"{target_} === {dict_[major_group][target_]}")

def get_by_group(dict_, major_group, target_):
    print(f"{target_} === {dict_[major_group][target_]}")
