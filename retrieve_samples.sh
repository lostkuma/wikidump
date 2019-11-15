i=0;
for i in {0..10};
do
python sample_article_by_sampledid.py --samples_log ".sample/samples/div$i_sample.txt" --data_dir "all_5.9million/output_$i_enwiki" --div $i;
done;