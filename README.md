Streaming Unique Counting
==========================

Implementations of HyperLogLog and adaptive sampling for approximate counting of unique items
in a stream.

## Quickstart

```
pip install mmh3
git clone git@github.com:emaadmanzoor/streaming-unique-counting.git
cd streaming-unique-counting

python2 cardinality_estimation.py "test_data/wuthering_heights.txt" 0 exact
python2 cardinality_estimation.py "test_data/wuthering_heights.txt" 0 adaptive 1150

python2 cardinality_estimation.py "test_data/big_test/" 1 exact
python2 cardinality_estimation.py "test_data/big_test/" 1 adaptive 5000
```

## Contributors

   * [Emaad Ahmed Manzoor](http://eyeshalfclosed.com)
   * Tariq Alturkestani
   * Jumana Baghabra
   * Fatemah Alzayer
   * Meshari Alazmi

## References

   * HyperLogLog: Stefan Heule, Marc Nunkesser, Alex Hall. HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm. Proceedings of the EDBT 2013 Conference, ACM, Genoa, Italy.
   * Adaptive Sampling: Flajolet, Philippe. "On adaptive sampling." Computing 43.4 (1990): 391-400.
   * Wuthering Heights: [Project Gutenberg](http://www.gutenberg.org/cache/epub/768/pg768.txt)
