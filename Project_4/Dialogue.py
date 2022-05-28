import random

class StoreVars:
    
    def __init__(self):
        self.store = {}
        self.level = 0

    def get_Variable(self,variable_Name):
        return self.store[variable_Name]

    def set_Variable(self, variable_Name, variable_Value):
        self.store[variable_Name] = variable_Value

    def clear(self):
        self.store = {}

def get_random(output_list):
    return random.choice(output_list)
    
def parse_lines(string):
    try:
        output = {"type":""}
        output["tabs"] = len(string.split("\t"))-1
        string = string.strip()
        if string[0] == "#":
            output["type"] = "comments"
            return output
        if string[0] == "~":
            output["type"] = "variable"
            seperated = string.split(":")
            name = seperated[0]
            output["name"] = name[1:]
            values = seperated[1].strip()
        else:
            output["type"] = "user_rule"
            seperated = string.split(":")
            output["identifier"] = seperated[0].strip()
            seperated = seperated[1:]
            input_line = seperated[0].replace("(", "")
            input_line = seperated[0].replace(")", "")
            output["input_line"] = input_line[1:].lower().strip().replace("(", "")
            values = seperated[1].strip()
            
        if "[" in values:
            values = values.replace("[", "")
            values = values.replace("]", "")
            strings = values.split("\"")
            values = [item.strip().split(" ") for item in strings[0::2]][0]
            strings = list(strings[1::2])
            
            output["values"] = (values + strings)
        else:
            output["values"] = values
        return output
    except:
        print("Conversation Error: ", string)
        return {"type":"error"}

def find_input(user_input, dictionary, last):
    if "~" in user_input:
        if user_input[1:] in variables:
            user_input = variables[user_input[1:]]
            if type(user_input) == list:
                user_input = get_random(user_input)
            print(user_input)
    for item in dictionary:
        if "~" in item["input_line"]:
            #print(item["input_line"][1:])
            #print(variables)
            if item["input_line"][1:].strip() in variables:
                if user_input.lower() in variables[item["input_line"][1:]]:
                    if item["tabs"] == 0:
                        #print("Item: ", item)
                        item["accessed"] = True
                        return item
                    else:
                        index = dictionary.index(item)
                        while dictionary[index]["tabs"] >= item["tabs"]:
                            index-=1
                        if "accessed" in dictionary[index]:
                            item["accessed"] = True
                            return item
                        else:
                            return None
        elif item["input_line"] == user_input.lower():
            if item["tabs"] == 0:
                item["accessed"] = True
                return item
            else:
                index = dictionary.index(item)
                while dictionary[index]["tabs"] >= item["tabs"]:
                    index-=1
                if "accessed" in dictionary[index]:
                    item["accessed"] = True
                    return item
                else:
                    return None
    input_seperated = user_input.split(" ")
    testing = []
    for index in range(0, len(input_seperated)):
        temp = input_seperated.copy()
        temp[index] = "_"
        temp = " ".join(temp)
        testing.append(temp)

    for tester in testing:
        for item in dictionary:
            if item["input_line"] == tester:  
                index = dictionary.index(item)
                if item["tabs"] == 0:
                    item["accessed"] = True
                    return (item, input_seperated[tester.split(" ").index("_")])
                while dictionary[index]["tabs"] >= item["tabs"]:
                    index-=1
                if "accessed" in dictionary[index]:
                    item["accessed"] = True
                    return (item, input_seperated[tester.split(" ").index("_")])
                else:
                    return None
    return None

def read_file(fin):
    #reads file
    file = open(fin, 'r')
    output = []

    for line in file:
        line = parse_lines(line)
        if line["type"] == "user_rule":  
            output.append(line)
        elif line["type"] == "variable":
            output.append(line)
    return output


def main():

    human_input = input().lower()
    last = ""
    
    while(human_input != 'exit'):
        output_field = find_input(human_input, output, last)
        #print(output_field)
        if type(output_field) != type(None):
            if type(output_field) == tuple:
                #print(len(output_field))
                #print(output_field)
                last = output_field[0]["input_line"]
                name = output_field[0]["values"]
                name = "".join([i[1:] for i in name.split() if '$' in i])
                #print(type(output_field[1]))
                user_variables[name] = output_field[1]
                output_line = output_field[0]["values"]
            elif type(output_field) == dict:
                last = output_field["input_line"]
                output_line = output_field["values"]
            if "~" in output_line:
                output_line = variables[output_line[1:]]
            if type(output_line) == list:
                output_line = get_random(output_line)
            if "$" in output_line:
                for item in [i for i in output_line.split(" ") if '$' in i]:
                    #print(item)
                    if item[1:] in user_variables:
                        #print(item, user_variables[item[1:]])
                        output_line = output_line.replace(item, user_variables[item[1:]])
                    else:
                        output_line = "I don't know"
        else:
            output_line = "invalid input"
        print(output_line)
            
        human_input = input().lower()
        
    print("Goodbye")

#Main Program Call
output = read_file('dialogue.txt')
    
variables = {}
for index in range(0, len(output)):
    if output[index]["type"] == "variable":
        variables[output[index]["name"]] = output[index]["values"]

for item in output:
    if item["type"] == "variable":
        output.remove(item)

user_variables = {}
#for item in output:
#    print(item)
#print(variables) 
main()
