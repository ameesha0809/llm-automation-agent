from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read comments
input_file = "../data/comments.txt"
output_file = "../data/comments-similar.txt"

with open(input_file, "r", encoding="utf-8") as f:
    comments = [line.strip() for line in f.readlines() if line.strip()]

# Compute embeddings
embeddings = model.encode(comments)

# Compute similarity matrix
similarity_matrix = cosine_similarity(embeddings)

# Find the most similar pair (excluding self-comparisons)
np.fill_diagonal(similarity_matrix, 0)  # Ignore diagonal (self-similarity)
most_similar_idx = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)

# Get the most similar comments
comment1 = comments[most_similar_idx[0]]
comment2 = comments[most_similar_idx[1]]

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(comment1 + "\n")
    f.write(comment2 + "\n")

print(f"Most similar comments saved to {output_file}")
