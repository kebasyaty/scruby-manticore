"""Test a settings module."""

from __future__ import annotations

from xloft import AliasDict

from scruby_full_text import settings

LANGUAGES = AliasDict(
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


class TestPositive:
    """Positive tests."""

    def test_supported_languages(self) -> None:
        """Testing supported languages."""
        for lang, data in LANGUAGES.items():
            tmp = settings.LANG_FULL_TEXT_SEARCH.get(lang[0])
            tmp_2 = settings.LANG_FULL_TEXT_SEARCH.get(lang[1])
            assert tmp is not None
            assert tmp_2 is not None
            assert tmp == data
            assert tmp_2 == data
