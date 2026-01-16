# Scruby-Full-Text - Full-text search with Manticore Search.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
"""Plugin settings.

The module contains the following parameters:

- `LANGUAGES` - List of supported languages and full-text search algorithms.
"""

from __future__ import annotations

__all__ = ("LANG_FULL_TEXT_SEARCH",)

from xloft import AliasDict

# List of supported languages for full-text search.
LANG_FULL_TEXT_SEARCH: AliasDict = AliasDict(
    [
        ({"Arabic", "ar"}, ("ar", "libstemmer_ar")),  # pyrefly: ignore[bad-argument-type]
        ({"Catalan", "ca"}, ("ca", "libstemmer_ca")),  # pyrefly: ignore[bad-argument-type]
        ({"Chinese", "zh"}, ("zh", "jieba_chinese")),  # pyrefly: ignore[bad-argument-type]
        ({"Czech", "cz"}, ("cz", "stem_cz")),  # pyrefly: ignore[bad-argument-type]
        ({"Danish", "da"}, ("da", "libstemmer_da")),  # pyrefly: ignore[bad-argument-type]
        ({"Dutch", "hl"}, ("hl", "libstemmer_nl")),  # pyrefly: ignore[bad-argument-type]
        ({"English", "en"}, ("en", "lemmatize_en_all")),  # pyrefly: ignore[bad-argument-type]
        ({"Finnish", "fi"}, ("fi", "libstemmer_fi")),  # pyrefly: ignore[bad-argument-type]
        ({"French", "fr"}, ("fr", "libstemmer_fr")),  # pyrefly: ignore[bad-argument-type]
        ({"German", "de"}, ("de", "lemmatize_de_all")),  # pyrefly: ignore[bad-argument-type]
        ({"Greek", "el"}, ("el", "libstemmer_el")),  # pyrefly: ignore[bad-argument-type]
        ({"Hindi", "hi"}, ("hi", "libstemmer_hi")),  # pyrefly: ignore[bad-argument-type]
        ({"Hungarian", "hu"}, ("hu", "libstemmer_hu")),  # pyrefly: ignore[bad-argument-type]
        ({"Indonesian", "id"}, ("id", "libstemmer_id")),  # pyrefly: ignore[bad-argument-type]
        ({"Irish", "ga"}, ("ga", "libstemmer_ga")),  # pyrefly: ignore[bad-argument-type]
        ({"Italian", "it"}, ("it", "libstemmer_it")),  # pyrefly: ignore[bad-argument-type]
        ({"Japanese", "ja"}, ("ga", "ngram_chars=japanese ngram_len=1")),  # pyrefly: ignore[bad-argument-type]
        ({"Korean", "ko"}, ("ko", "ngram_chars=korean ngram_len=1")),  # pyrefly: ignore[bad-argument-type]
        ({"Lithuanian", "lt"}, ("lt", "libstemmer_lt")),  # pyrefly: ignore[bad-argument-type]
        ({"Nepali", "ne"}, ("ne", "libstemmer_ne")),  # pyrefly: ignore[bad-argument-type]
        ({"Norwegian", "no"}, ("no", "libstemmer_no")),  # pyrefly: ignore[bad-argument-type]
        ({"Portuguese", "pt"}, ("pt", "libstemmer_pt")),  # pyrefly: ignore[bad-argument-type]
        ({"Romanian", "ro"}, ("ro", "libstemmer_ro")),  # pyrefly: ignore[bad-argument-type]
        ({"Russian", "ru"}, ("ru", "lemmatize_ru_all")),  # pyrefly: ignore[bad-argument-type]
        ({"Spanish", "es"}, ("es", "libstemmer_es")),  # pyrefly: ignore[bad-argument-type]
        ({"Swedish", "sv"}, ("sv", "libstemmer_sv")),  # pyrefly: ignore[bad-argument-type]
        ({"Tamil", "ta"}, ("ta", "libstemmer_ta")),  # pyrefly: ignore[bad-argument-type]
        ({"Turkish", "tr"}, ("tr", "libstemmer_tr")),  # pyrefly: ignore[bad-argument-type]
    ],
)
