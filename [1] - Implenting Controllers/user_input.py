def get_input():
    user_input = input().strip()
    return user_input

def find_input(user_input, dictionary, last):
    for item in dictionary:
        if item["input_line"] == user_input:  
            if item["tabs"] == 0:
                return item
            else:
                index = dictionary.index(item)
                while dictionary[index]["tabs"] >= item["tabs"]:
                    index-=1
                if last == dictionary[index]["input_line"]:
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
    print(testing)
    for tester in testing:
        for item in dictionary:
            if item["input_line"] == tester:  
                index = dictionary.index(item)
                if item["tabs"] == 0:
                    return (item, input_seperated[tester.split(" ").index("_")])
                while dictionary[index]["tabs"] >= item["tabs"]:
                    index-=1
                if last == dictionary[index]["input_line"]:
                    return (item, input_seperated[tester.split(" ").index("_")])
                else:
                    return None
    return None


    
dictionary = [{'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': '~greetings', 'values': ['hi', 'hello', 'what up']}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u1', 'input_line': 'you', 'values': 'good'}, {'type': 'user_rule', 'tabs': 1, 'identifier': 'u1', 'input_line': 'and', 'values': ['one', 'two']}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': 'you', 'values': 'Should not be here'}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': 'test', 'values': 'two'}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u1', 'input_line': 'third', 'values': '~greetings'}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': 'my name is _', 'values': 'hello $name'}, {'type': 'user_rule', 'tabs': 1, 'identifier': 'u1', 'input_line': 'I am _ years old', 'values': 'You are $age years old'}, {'type': 'user_rule', 'tabs': 1, 'identifier': 'u1', 'input_line': 'do you remember my name ', 'values': 'Yes'}, {'type': 'user_rule', 'tabs': 2, 'identifier': 'u2', 'input_line': 'what is it', 'values': '$name'}, {'type': 'user_rule', 'tabs': 3, 'identifier': 'u3', 'input_line': 'you are very smart', 'values': 'I know'}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': 'what is my name ', 'values': 'your name is $name'}, {'type': 'user_rule', 'tabs': 0, 'identifier': 'u', 'input_line': '(how old am I ', 'values': 'you are $age'}]
tmp = get_input()
print(find_input(tmp,dictionary, ""))
