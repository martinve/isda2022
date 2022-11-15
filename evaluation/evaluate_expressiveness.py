from texttable import Texttable
import statistics
import sys

data_dir = "../results"
corpus_dir = "../corpus"


def calculate_metrics():
    file = corpus_dir + "/corpus-min.txt"
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    struct_ucca = read_ucca()
    struct_amr = read_amr()
    struct_ud = read_ud()
    struct_interpret = read_interpret()
    struct_drs = read_drs()

    k = 0

    metrics = {}
    metrics = {"amr": [], "ucca": [], "intp": [], "ud": [], "drs": []}

    for sent in lines:
        metrics["amr"].append(sentence_metrics(sent, struct_amr[k]))
        metrics["ucca"].append(sentence_metrics(sent, struct_ucca[k]))
        # metrics["intp"].append(sentence_metrics(sent, struct_interpret[k]))
        metrics["ud"].append(sentence_metrics(sent, struct_ud[k]))
        metrics["drs"].append(sentence_metrics(sent, struct_drs[k]))

        k = k + 1

    tbl = Texttable()
    tbl.set_cols_align(["l", "l", "c", "c", "c", "c"])
    tbl.header(["ID", "Sent", "AMR", "UCCA", "UD", "DRS"])

    k = 0
    for sent in lines:
        tbl.add_row([1 + k, sent, metrics["amr"][k], metrics["ucca"][k], metrics["ud"][k], metrics["drs"][k]])
        k = k + 1
    tbl.add_row(["", "TOTAL SCORE", get_score(metrics["amr"]), get_score(metrics["ucca"]),
                 get_score(metrics["ud"]),  get_score(metrics["drs"])])

    print(tbl.draw())


def read_ud():
    lines = readfile("corpus-min-ud-simple.txt")

    sent = -1
    struct = {}

    for line in lines:
        if not line.startswith("\t") and not line.strip() == "":
            sent = sent + 1
            struct[sent] = list()
            continue

        if line.strip() == "":
            continue

        struct[sent].append(line.strip())

    # print("Parsed UD: ", str(sent))
    return struct


def read_interpret():
    lines = readfile("corpus-min-interpret.txt")

    sent = -1
    skip = True
    empty = 0
    struct = {}

    for line in lines:
        line = line.strip()

        if line.startswith("#### Interpretation"):
            sent = sent + 1
            struct[sent] = list()
            empty = 0
            skip = False

        else:
            if line.strip() == "":
                empty = empty + 1

            if empty > 1 or skip:
                continue

            if line.strip() == "" or line.strip() == "```":
                skip_line = True
            else:
                skip_line = False

            if not skip_line:
                struct[sent].append(line)

    # print("Parsed Interpret: ", str(sent))
    # print(struct)
    return struct


def read_ucca():
    lines = readfile("corpus-min-ucca.md")

    sent = -1
    skip = True
    skip_lines = False
    struct = {}

    for line in lines:
        line = line.strip()

        if line.startswith("corpus-min_"):
            sent = sent + 1
            struct[sent] = list()
            skip = False
            skip_lines = False
        else:
            if skip:
                continue

            if line.startswith("Process:"):
                skip_lines = True
            if line.startswith("Participant:"):
                skip_lines = False

            if skip_lines:
                continue

            line = line.strip()
            if not skip_lines and len(line) > 0 and starts_with_number(line):
                struct[sent].append(line)

    # print("Parsed UCCA", str(sent))
    # print(struct[0])
    return struct


def read_amr():
    lines = readfile("corpus-min-amr.txt")

    sent = -1
    struct = {}

    for line in lines:
        line = line.strip()

        if line.startswith("# ::snt"):
            sent = sent + 1
            struct[sent] = list()
        else:
            if line.strip() != "":
                struct[sent].append(line)

    # print("Parsed AMR", str(sent))
    # print(struct)
    return struct


def read_drs():
    lines = readfile("corpus-min-drs.txt")

    # print(len(lines))
    # sys.exit(-1)

    sent = -1
    struct = {}

    for line in lines:
        line = line.strip()
        
        if not line:
            continue  

        if line.startswith("('Snt: "):
            sent += 1
            struct[sent] = list()
            continue

        if line and line != "---" and sent > -1: 
            if sent == -1:
                print("L", line)
            struct[sent].append(line)          


        #if line.startswith("('Snt:"):
        #    sent = sent + 1
        #    struct[sent] = list()
        #else:
        #    if line.strip() != "":
        #        struct[sent].append(line)

    # print("Parsed AMR", str(sent))
    # print(struct)
    return struct    


def starts_with_number(line):
    return line[0].isdigit()


def sentence_metrics(sent, struct):
    return len(struct) / len(sent)


def readfile(file):
    file = data_dir + "/" + file
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_score(values):
    return statistics.mean(values)


if __name__ == '__main__':
    calculate_metrics()
