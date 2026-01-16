"""Test a settings module."""

from __future__ import annotations

from scruby_full_text import settings

LANGUAGES = {
    "Arabic": ("ar", "libstemmer_ar"),
    "Catalan": ("ca", "libstemmer_ca"),
    "Chinese": ("zh", "jieba_chinese"),
    "Czech": ("cz", "stem_cz"),
    "Danish": ("da", "libstemmer_da"),
    "Dutch": ("nl", "libstemmer_nl"),
    "English": ("en", "lemmatize_en_all"),
    "Finnish": ("fi", "libstemmer_fi"),
    "French": ("fr", "libstemmer_fr"),
    "German": ("de", "lemmatize_de_all"),
    "Greek": ("el", "libstemmer_el"),
    "Hindi": ("hi", "libstemmer_hi"),
    "Hungarian": ("hu", "libstemmer_hu"),
    "Indonesian": ("id", "libstemmer_id"),
    "Irish": ("ga", "libstemmer_ga"),
    "Italian": ("it", "libstemmer_it"),
    "Japanese": ("ja", "ngram_chars=japanese ngram_len=1"),
    "Korean": ("ko", "ngram_chars=korean ngram_len=1"),
    "Lithuanian": ("lt", "libstemmer_lt"),
    "Nepali": ("ne", "libstemmer_ne"),
    "Norwegian": ("no", "libstemmer_no"),
    "Portuguese": ("pt", "libstemmer_pt"),
    "Romanian": ("ro", "libstemmer_ro"),
    "Russian": ("ru", "lemmatize_ru_all"),
    "Spanish": ("es", "libstemmer_es"),
    "Swedish": ("sv", "libstemmer_sv"),
    "Tamil": ("ta", "libstemmer_ta"),
    "Turkish": ("tr", "libstemmer_tr"),
}


class TestPositive:
    """Positive tests."""

    def test_supported_languages(self) -> None:
        """Testing supported languages."""
        for lang, data in LANGUAGES.items():
            tmp = settings.LANG_FULL_TEXT_SEARCH.get(lang)
            assert tmp is not None
            assert tmp[0] == data[0]
            assert tmp[1] == data[1]
