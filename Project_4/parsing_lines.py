def parse_lines(string):
    try:
        output = {"type":""}
        output["tabs"] = string.count('\t')
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
            output["input_line"] = input_line[1:]
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

        print(output)
        return output
    except:
        #print("Invalid input")
        return {"type":"error"}

parse_lines('~choices: [choice robot \"I am a robot\"]')
parse_lines("u:(second test):second test worked")
parse_lines("    u1:(third test):~greetings")
parse_lines("u:(colon is missing) error should have been detected in parsing")
