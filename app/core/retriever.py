import os
import pickle
from pathlib import Path

import faiss
import numpy as np
import yaml

from app.core.embedder import embed_texts


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
CONFIG_PATH = CONFIG_DIR / "config.yaml"


def load_config():
    """Load config safely so import-time startup does not fail."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text("{}\n", encoding="utf-8")
        return {}

    with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file) or {}


cfg = load_config()


def get_paths(session_id):
    base_dir = BASE_DIR / "data" / f"session_{session_id}" / "backup"
    return {
        "INDEX_PATH": base_dir / "faiss.index",
        "META_PATH": base_dir / "chunks.pkl",
    }


def normalize_embeddings(vectors):
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / norms


def build_index(text_chunks, session_id, force_rebuild):
    paths = get_paths(session_id)
    index_path = paths["INDEX_PATH"]
    meta_path = paths["META_PATH"]

    os.makedirs(index_path.parent, exist_ok=True)

    if index_path.exists() and meta_path.exists() and not force_rebuild:
        print("Index already exists.")
        return

    print("Building FAISS index...")

    vectors = embed_texts(text_chunks)
    vectors = normalize_embeddings(np.array(vectors).astype("float32"))

    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)

    faiss.write_index(index, str(index_path))
    with open(meta_path, "wb") as meta_file:
        pickle.dump(text_chunks, meta_file)

    print("FAISS index saved.")


def load_index(session_id):
    paths = get_paths(session_id)
    index_path = paths["INDEX_PATH"]
    meta_path = paths["META_PATH"]

    if not index_path.exists():
        raise FileNotFoundError("FAISS index not found.")

    index = faiss.read_index(str(index_path))
    with open(meta_path, "rb") as meta_file:
        chunks = pickle.load(meta_file)

    return index, chunks


def retrieve_chunks(query, session_id, k=5):
    index, chunks = load_index(session_id)

    q_vec = embed_texts([query])
    q_vec = normalize_embeddings(np.array(q_vec).astype("float32"))

    _, indices = index.search(q_vec, k)
    return [chunks[i] for i in indices[0]]
