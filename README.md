# Image Retrieval from Scratch

**Status** · Starter scaffold

The goal is to retrieve visually similar images and measure whether learned embeddings improve on a simple feature baseline.

## Run the starter

From the repository root, run `python src/baseline.py` with Python 3.10 or later. It ranks three synthetic feature vectors by distance to a query.

- `src/baseline.py` contains exact nearest-neighbour ranking.
- `experiments/README.md` outlines the first retrieval benchmark.

The first milestone is a colour-histogram baseline on a labelled evaluation set. CNN embeddings, contrastive training, a FAISS index and a demo are planned.
