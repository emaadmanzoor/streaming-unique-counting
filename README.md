# Streaming Unique Counting
*Algorithms, KAUST, Fall 2013 - with Prof. Mikhail Moshkov.*

Implementations of HyperLogLog and adaptive sampling for approximate counting of unique items in a stream. A [report](www.eyeshalfclosed.com/docs/CS260_Final_Report.pdf) describing some interesting empirical comparision results is also available.

## Quickstart

```
pip install mmh3
git clone git@github.com:emaadmanzoor/streaming-unique-counting.git
cd streaming-unique-counting

python cardinality_estimation.py "test_data/wuthering_heights.txt" 0 exact
python cardinality_estimation.py "test_data/wuthering_heights.txt" 0 adaptive 1150

python cardinality_estimation.py "test_data/big_test/" 1 exact
python cardinality_estimation.py "test_data/big_test/" 1 adaptive 5000
```

## Contributors

   * [Emaad Ahmed Manzoor](http://eyeshalfclosed.com)
   * Tariq Alturkestani
   * Jumana Baghabra
   * Fatemah Alzayer
   * Meshari Alazmi
