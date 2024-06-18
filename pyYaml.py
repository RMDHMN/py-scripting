import yaml

def read_yaml():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        print(config)

def write_yaml():
    data = {'key': 'value'}
    with open('config.yaml', 'w') as file:
        yaml.dump(data, file)

read_yaml()
write_yaml()
