# First benchmark

1. Pick a small image dataset with a documented licence and define which gallery images count as relevant for each query.
2. Keep queries separate from the gallery and split near-duplicate groups together when training and evaluating learned features.
3. Build normalised colour histograms and report Recall@1, Recall@5 and examples of failed matches.
4. Compare CNN embeddings on the same queries with exact search before adding an approximate index.
