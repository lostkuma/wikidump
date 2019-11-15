
import argparse
import numpy as np
import os
from bs4 import BeautifulSoup

np.random.seed(32)

# initialization
root_dir = os.path.join(os.getcwd(), "extractor_log")
metadata_path = os.path.join(os.getcwd(), "extractor_log/metadata.log")
articles_sampling = 50000

div_stats = np.zeros(57)
total_articles = 0


# check if dir exists
if not os.path.isdir("./samples"):
    os.mkdir("./samples")
if not os.path.isdir("./samples/sampled_ids"):
    os.mkdir("./samples/sampled_ids")

# get file stats
with open(metadata_path, "r", encoding="utf-8") as logfile:
    idx = 0
    for line in logfile:
        if idx == 57:
            break 
        line = line.split()
        num_articles = int(line[-1])
        div_stats[idx] = num_articles
        idx += 1

total_articles = np.sum(div_stats) # total num articles
div_percentage = div_stats / total_articles # percentage taken of each div in respect to total 
sample_each_div = np.rint(articles_sampling = 50000 * div_percentage) # round to nearest int, sample needed for each div 
count_total_samples = np.sum(sample_each_div)
print("total articles sampling: {}".format(count_total_samples))

for i in range(57): 
    current_sample_idx = np.random.choice(int(div_stats[i]), int(sample_each_div[i]), replace=False) # random sample idx without replacement
    sorted_current_sample_idx = sorted(current_sample_idx) # sorted sample idx asc
    original_file_path = os.path.join(root_dir, "{}.txt".format(i+1))
    log_dir = os.path.join("./samples/sampled_ids/", "div{}_sample.log".format(i+1))
    
    print("sampling {}/{} articles from {}...".format(int(sample_each_div[i]), int(div_stats[i]), "{}.txt".format(i+1)))
    
    # open source file 
    with open(original_file_path, "r", encoding="utf-8") as textfile:
        # read 3 lines header away
        textfile.readline()
        textfile.readline()
        textfile.readline()
        line_num = 0
        line = textfile.readline()
        current_sample_idx = sorted_current_sample_idx.pop(0)
        samples = list()
        while line:
            if not line[6].isdigit(): 
                line = textfile.readline() 
            if line_num == current_sample_idx:
                samples.append(line[6:])            
                #with open(log_dir, "a", encoding="utf-8") as outfile: 
                    # append selected sample to file 
                    #outfile.write(line[6:]) 
                if len(sorted_current_sample_idx) == 0:
                    break
                current_sample_idx = sorted_current_sample_idx.pop(0)
            line = textfile.readline()
            line_num += 1
        samples = sorted(samples) # sort sample based on article ID order 
        
        # write to output file
        with open(log_dir, "w", encoding="utf-8") as outfile:
            for s in samples:
                outfile.write(s)


