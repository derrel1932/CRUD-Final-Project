import definitions as df_
file_path = './6000_Largest_Companies_ranked_by_Market_Cap.csv'
# groupables are defined as the strings of the field_types in the header of the csv file
# fields in the groupables are to be main groups of fields with names
GROUPABLES = ["Symbol", "Country"]
# we only give an option to rank one field
RANKED_FIELD = "Marketcap"
# where to store the ranking
STORED_RANKS = "Rank"
main_data_dict = {}
groups_of_data = {}

# main to make it clear and explicit !
if __name__ == '__main__':
    # open the file and load its contents into the system
    fieldnames, main_data_dict, groups_of_data = df_.cf_.read_n_dict(file_path, GROUPABLES, RANKED_FIELD, STORED_RANKS)

    # program loop
    while True:
        df_.display_menu()
        # get an action input
        match input("Enter action : "):
            # CREATE
            case '1': main_data_dict, groups_of_data = df_.create(main_data_dict, groups_of_data, fieldnames)

            # READ
            case '2': main_data_dict, groups_of_data = df_.read(main_data_dict, groups_of_data, fieldnames)

            # UPDATE
            case '3': main_data_dict, groups_of_data = df_.update(main_data_dict, groups_of_data, fieldnames)
                
            # DELETE
            case '4': main_data_dict, groups_of_data = df_.delete(main_data_dict, groups_of_data, fieldnames)
                
            # EXIT
            case '5':
                print("End of Session. Have a nice day !")
                break

    # finish and write everything in the system back to file storage
    df_.cf_.write_dicts(file_path, fieldnames, main_data_dict, groups_of_data, RANKED_FIELD, STORED_RANKS)


    # df_.cf_.get_by_major_group(groups_of_data, "Marketcap")
    # for name in main_data_dict:
    #     print(f"{name} : {main_data_dict[name]}")
    # for major_group in groups_of_data:
    #     print(f"<<< {major_group} >>>")
    #     for group_name in groups_of_data[major_group]:
    #         print(f"{group_name} === {groups_of_data[major_group][group_name]}")
