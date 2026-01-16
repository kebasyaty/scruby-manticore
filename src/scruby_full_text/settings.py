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
        ({"Arabic", "ar"}, ("ar", "libstemmer_ar")),
        ({"Catalan", "ca"}, ("ca", "libstemmer_ca")),
        ({"Chinese", "zh"}, ("zh", "jieba_chinese")),
        ({"Czech", "cz"}, ("cz", "stem_cz")),
        ({"Danish", "da"}, ("da", "libstemmer_da")),
        ({"Dutch", "hl"}, ("hl", "libstemmer_nl")),
        ({"English", "en"}, ("en", "lemmatize_en_all")),
        ({"Finnish", "fi"}, ("fi", "libstemmer_fi")),
        ({"French", "fr"}, ("fr", "libstemmer_fr")),
        ({"German", "de"}, ("de", "lemmatize_de_all")),
        ({"Greek", "el"}, ("el", "libstemmer_el")),
        ({"Hindi", "hi"}, ("hi", "libstemmer_hi")),
        ({"Hungarian", "hu"}, ("hu", "libstemmer_hu")),
        ({"Indonesian", "id"}, ("id", "libstemmer_id")),
        ({"Irish", "ga"}, ("ga", "libstemmer_ga")),
        ({"Italian", "it"}, ("it", "libstemmer_it")),
        ({"Japanese", "ja"}, ("ga", "ngram_chars=japanese ngram_len=1")),
        ({"Korean", "ko"}, ("ko", "ngram_chars=korean ngram_len=1")),
        ({"Lithuanian", "lt"}, ("lt", "libstemmer_lt")),
        ({"Nepali", "ne"}, ("ne", "libstemmer_ne")),
        ({"Norwegian", "no"}, ("no", "libstemmer_no")),
        ({"Portuguese", "pt"}, ("pt", "libstemmer_pt")),
        ({"Romanian", "ro"}, ("ro", "libstemmer_ro")),
        ({"Russian", "ru"}, ("ru", "lemmatize_ru_all")),
        ({"Spanish", "es"}, ("es", "libstemmer_es")),
        ({"Swedish", "sv"}, ("sv", "libstemmer_sv")),
        ({"Tamil", "ta"}, ("ta", "libstemmer_ta")),
        ({"Turkish", "tr"}, ("tr", "libstemmer_tr")),
    ],
)
