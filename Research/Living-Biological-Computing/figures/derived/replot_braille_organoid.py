#!/usr/bin/env python3
"""Replot mean 24-channel spike counts by Braille class from data.bris.

Source dataset: Ward-Cherrier, Liu & Philamore (2026), DOI 10.5523/bris.19qmlywobvl3u22pzo67z3bc6l.
Dataset licence: Non-Commercial Government Licence v2.0. This script downloads the
source ZIP to memory, extracts only the derived 24-channel CSV, and does not save
or redistribute the source data.
"""
from __future__ import annotations
import io
import urllib.request
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
plt.rcParams["svg.fonttype"] = "none"
import numpy as np
import pandas as pd

DATA_URL = (
    "https://data.bris.ac.uk/datasets/19qmlywobvl3u22pzo67z3bc6l/"
    "19qmlywobvl3u22pzo67z3bc6l.zip"
)
CSV_PATH = (
    "19qmlywobvl3u22pzo67z3bc6l/derived/"
    "three_organoid_24_channel_spike_counts.csv"
)
OUT = Path(__file__).resolve().parent / "braille_mean_spike_counts_by_letter.svg"


def load_data() -> pd.DataFrame:
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "NaturalDAO-research-figure/1.0"})
    with urllib.request.urlopen(req, timeout=60) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
        return pd.read_csv(archive.open(CSV_PATH))


def main() -> None:
    data = load_data()
    channels = [f"channel_{i}_spike_count" for i in range(40, 64)]
    letters = [chr(ord("A") + i) for i in range(26)]
    means = data.groupby("braille_letter", sort=True)[channels].mean().reindex(letters)
    if means.isna().any().any() or means.shape != (26, 24):
        raise ValueError("Expected a complete 26-letter × 24-channel table")

    fig, ax = plt.subplots(figsize=(13.2, 7.2), layout="constrained")
    im = ax.imshow(means.to_numpy(), aspect="auto", cmap="viridis", interpolation="nearest")
    ax.set_xticks(np.arange(24), [str(i) for i in range(1, 25)])
    ax.set_yticks(np.arange(26), letters)
    ax.set_xlabel("MEA channel (ordered by organoid: 1–8, 9–16, 17–24)")
    ax.set_ylabel("Braille letter")
    ax.set_title("Mean organoid spike counts by Braille letter")
    for boundary in (7.5, 15.5):
        ax.axvline(boundary, color="white", linewidth=1.6, alpha=0.9)
    cbar = fig.colorbar(im, ax=ax, pad=0.02)
    cbar.set_label("Mean threshold-based spike count per sample")
    per_letter = data.groupby("braille_letter").size()
    fig.text(
        0.01, -0.012,
        f"n={len(data):,} samples; {per_letter.min()}–{per_letter.max()} trials per letter. "
        "Replot from author-deposited derived data; no classifier rerun.",
        ha="left", va="top", fontsize=9,
    )
    fig.savefig(OUT, dpi=200, bbox_inches="tight")
    print(f"Saved {OUT}")
    print(f"Rows: {len(data)}; mean table: {means.shape}; min/max: {means.min().min():.2f}/{means.max().max():.2f}")


if __name__ == "__main__":
    main()
