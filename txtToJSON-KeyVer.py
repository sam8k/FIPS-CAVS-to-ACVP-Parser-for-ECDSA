#     This code is used for
#     converting txt file to JSON
#     This is for ECDSA "mode": "KeyVer"  --- (PKV.res)
#     Date : 13 August 2021
#     Author : @sam8k


import optparse
import pandas as pd
import json

sr = []
testPassed = []
count = 0


def get_input():
    parse = optparse.OptionParser()
    parse.add_option("-j", "--json", dest="json", help="Enter the path of the JSON file")
    parse.add_option("-t", "--txt", dest="txt", help="Enter the path of the txt file")
    parse.add_option("-o", "--output", dest="output", help="Enter the path of the destination")
    (options, arguments) = parse.parse_args()
    if not options.json:
        print("[-] Enter -h for Help")
        exit()
    elif not options.output:
        print("[-] Enter -h for Help")
        exit()
    elif not  options.txt:
        print("[-] Enter -h for Help")
        exit()
    return options


def getTemplate(jsonPath, output_path):
    f = open(jsonPath, "r", encoding='utf8')
    data = json.loads(f.read())

    testGroups = data[1]["testGroups"]

    for testGroup in testGroups:
        tests = testGroup["tests"]
        testGroup.pop("curve")
        testGroup.pop("testType")
        for test in tests:
            test.pop("qx")
            test.pop("qy")
            for i, row in df.iterrows():
                tcid = int(test["tcId"])
                if tcid == row["Sr No"]:
                    test["testPassed"] = row["testPassed"]

    with open(output_path, 'w') as data_file:
        json.dump(data, data_file)

    f.close()


if __name__ == "__main__":
    options = get_input()
    jsonPath = options.json
    txtPath = options.txt
    output_path = options.output

    with open(txtPath, "r") as lines:
        for line in lines:
            line = line.strip()
            size = len(line)
            if size != 0:
                if "Result" in line:
                    lis_d = line.split(" ")
                    result = lis_d[2]
                    if result == "P":
                        res = True
                    if result == "F":
                        res = False
                    testPassed.append(res)
                    count = count + 1
                    sr.append(count)

    dic = {"Sr No": sr, "testPassed": testPassed}
    df = pd.DataFrame(dic)
    getTemplate(jsonPath, output_path)
