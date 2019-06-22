import yaml


def yml_data_with_file(file_name):
    with open("../data/"+file_name+".yml", "r") as f:
        data=yaml.load(f)
        print(data)
        return data

# if __name__ == "__main__":
#     yml_data_with_file()