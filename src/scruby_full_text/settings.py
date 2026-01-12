# Scruby-Manticore - Full-text search with Manticore Search.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Plugin settings.

The module contains the following parameters:

- `LANGUAGES` - List of supported languages and full-text search algorithms.
"""

from __future__ import annotations

__all__ = ("LANGUAGES",)


# List of supported languages for full-text search.
LANGUAGES: dict[str, str] = {
    "Arabic": "libstemmer_ar",
    "Catalan": "libstemmer_ca",
    "Chinese": "jieba_chinese",
    "Czech": "stem_cz",
    "Danish": "libstemmer_da",
    "Dutch": "libstemmer_nl",
    "English": "lemmatize_en_all",
    "Finnish": "libstemmer_fi",
    "French": "libstemmer_fr",
    "German": "lemmatize_de_all",
    "Greek": "libstemmer_el",
    "Hindi": "libstemmer_hi",
    "Hungarian": "libstemmer_hu",
    "Indonesian": "libstemmer_id",
    "Irish": "libstemmer_ga",
    "Italian": "libstemmer_it",
    "Japanese": "ngram_chars=japanese ngram_len=1",
    "Korean": "ngram_chars=korean ngram_len=1",
    "Lithuanian": "libstemmer_lt",
    "Nepali": "libstemmer_ne",
    "Norwegian": "libstemmer_no",
    "Portuguese": "libstemmer_pt",
    "Romanian": "libstemmer_ro",
    "Russian": "lemmatize_ru_all",
    "Spanish": "libstemmer_es",
    "Swedish": "libstemmer_sv",
    "Tamil": "libstemmer_ta",
    "Turkish": "libstemmer_tr",
}
