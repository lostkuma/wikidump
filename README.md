# wikidump

## Statistics  
* there are 5,940,667 total processed wikipedia articles and more raw articles in [10/01/2019 wikipedia dump](https://dumps.wikimedia.org/enwiki/20191001/)
  
## 
* code to scrape the data: scrape.py
* [wikiExtractor](https://github.com/attardi/wikiextractor) was used to clean the raw data
* a simple random stratified sampling by article ID: sample_article_ids.py
* retrieve sampled article texts from sampled IDs: sample_article_by_sampledids.py (need to run with a bash loop)
