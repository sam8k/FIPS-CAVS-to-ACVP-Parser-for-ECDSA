#     This code is used for
#     comparing two dict object
#     Date : 13 August 2021
#     Author : @sam8k

import json
import optparse
from deepdiff import DeepDiff


def get_input():
    parse = optparse.OptionParser()
    parse.add_option("-p", "--p4", dest="p4", help="Enter the path of the p4 sample expected json file")
    parse.add_option("-g", "--gen", dest="gen", help="Enter the path of the generated expected json file")
    (options, arguments) = parse.parse_args()
    if not options.p4:
        print("[-] Enter -h for Help")
        exit()
    elif not options.gen:
        print("[-] Enter -h for Help")
        exit()
    return options


def comp(p4_path, gen_path):
    f = open(p4_path, "r"
             , encoding='utf8')
    g = open(gen_path, "r", encoding='utf8')
    data_p4 = json.loads(f.read())
    data_gen = json.loads(g.read())

    if data_gen == data_p4:
        print("[+] Both the Files are same")
    else:
        print("[-] Files are not same")
        print("[!] Diff between the files")
        diff = DeepDiff(data_p4, data_gen)
        print(diff)

    f.close()
    g.close()


if __name__ == "__main__":
    options = get_input()
    p4_path = options.p4
    gen_path = options.gen
    comp(p4_path, gen_path)
