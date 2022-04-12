#     This code is used for
#     converting txt file to JSON
#     This is for ECDSA "mode": "SigGen" ---(SigGen.res)
#     Date : 13 August 2021
#     Author : @sam8k


import pandas as pd
import json
import optparse

sr = []
d = []
Qx = []
Qy = []
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
        for test in tests:
            for i, row in df.iterrows():

                tcid = int(test["tcId"])
                if tcid == row["Sr No"]:
                    test["d"] = row["d"]
                    test["qx"] = row["Qx"]
                    test["qy"] = row["Qy"]

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
                if line[0] == "d":
                    lis_d = line.split(" ")
                    d.append(lis_d[2])
                    count = count + 1
                    sr.append(count)

                if "Qx" in line:
                    lis_qx = line.split(" ")
                    Qx.append(lis_qx[2])

                if "Qy" in line:
                    lis_qy = line.split(" ")
                    Qy.append(lis_qy[2])

    dic = {"Sr No": sr, "d": d, "Qx": Qx, "Qy": Qy}
    df = pd.DataFrame(dic)
    getTemplate(jsonPath, output_path)
