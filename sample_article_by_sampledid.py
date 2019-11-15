import argparse
import numpy as np
import os
from bs4 import BeautifulSoup

# get file name inputs
parser = argparse.ArgumentParser(description="sampled ids file name input")
parser.add_argument("--sample_ids", type=str, help="pass in the corresponding file with the sampled ids")
parser.add_argument("--data_dir", type=str, help="pass in the corresponding div dir")
parser.add_argument("--div", type=int, help="pass in the int value for current division working on")
args = parser.parse_args()

counter = 0
print("sampling from {}...".format(args.div))

# output file path
if not os.path.isdir("./samples"):
    os.mkdir("samples")
outfile = os.path.join("./samples/div{}_sampled_articles.xml".format(args.div))
with open(outfile, "w", encoding="utf-8"):
    pass 

# read in all ids and article names
sample_ids_in_div = list()
with open(args.sample_ids, "r", encoding="utf-8") as textfile:
    for line in textfile:
        line = line.split("\t")
        sample_ids_in_div.append(line[0])

# extract the articles out from the division
for root, dirs, files in os.walk(args.data_dir):
    for name in files:
        file_path = os.path.join(root, name)
        soup = BeautifulSoup(open(file_path, encoding="utf-8"), "html.parser")
        for article in soup.find_all("doc"):
            if article.get("id") in sample_ids_in_div:
                with open(outfile, "a", encoding="utf-8") as xmlfile:
                    xmlfile.write(article.prettify())
                idx_to_drop = sample_ids_in_div.index(article.get("id"))
                sample_ids_in_div.pop(idx_to_drop)
                counter += 1
                
print("\ttotal num articles sampled from div {}: {}".format(args.div, counter))
