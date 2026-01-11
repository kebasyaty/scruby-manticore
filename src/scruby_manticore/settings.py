# Scruby-Manticore - Full-text search with Manticore Search.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Plugin settings.

The module contains the following parameters:

- `LANGUAGES` - List of supported languages and full-text search algorithms.
"""

from __future__ import annotations

__all__ = ("LANGUAGES",)

from xloft import NamedTuple

# List of supported languages and full-text search algorithms.
LANGUAGES: NamedTuple = NamedTuple(
    Arabic="libstemmer_ar",  # pyrefly: ignore[bad-argument-type]
    Catalan="libstemmer_ca",  # pyrefly: ignore[bad-argument-type]
    Chinese="jieba_chinese",  # pyrefly: ignore[bad-argument-type]
    Czech="stem_cz",  # pyrefly: ignore[bad-argument-type]
    Danish="libstemmer_da",  # pyrefly: ignore[bad-argument-type]
    Dutch="libstemmer_nl",  # pyrefly: ignore[bad-argument-type]
    English="lemmatize_en_all",  # pyrefly: ignore[bad-argument-type]
    Finnish="libstemmer_fi",  # pyrefly: ignore[bad-argument-type]
    French="libstemmer_fr",  # pyrefly: ignore[bad-argument-type]
    German="lemmatize_de_all",  # pyrefly: ignore[bad-argument-type]
    Greek="libstemmer_el",  # pyrefly: ignore[bad-argument-type]
    Hindi="libstemmer_hi",  # pyrefly: ignore[bad-argument-type]
    Hungarian="libstemmer_hu",  # pyrefly: ignore[bad-argument-type]
    Indonesian="libstemmer_id",  # pyrefly: ignore[bad-argument-type]
    Irish="libstemmer_ga",  # pyrefly: ignore[bad-argument-type]
    Italian="libstemmer_it",  # pyrefly: ignore[bad-argument-type]
    Japanese="ngram_chars=japanese ngram_len=1",  # pyrefly: ignore[bad-argument-type]
    Korean="ngram_chars=korean ngram_len=1",  # pyrefly: ignore[bad-argument-type]
    Lithuanian="libstemmer_lt",  # pyrefly: ignore[bad-argument-type]
    Nepali="libstemmer_ne",  # pyrefly: ignore[bad-argument-type]
    Norwegian="libstemmer_no",  # pyrefly: ignore[bad-argument-type]
    Portuguese="libstemmer_pt",  # pyrefly: ignore[bad-argument-type]
    Romanian="libstemmer_ro",  # pyrefly: ignore[bad-argument-type]
    Russian="lemmatize_ru_all",  # pyrefly: ignore[bad-argument-type]
    Spanish="libstemmer_es",  # pyrefly: ignore[bad-argument-type]
    Swedish="libstemmer_sv",  # pyrefly: ignore[bad-argument-type]
    Tamil="libstemmer_ta",  # pyrefly: ignore[bad-argument-type]
    Turkish="libstemmer_tr",  # pyrefly: ignore[bad-argument-type]
)
