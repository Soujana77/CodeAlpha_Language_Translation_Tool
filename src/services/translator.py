from deep_translator import GoogleTranslator


def translate_text(text, source_lang, target_lang):
    """
    Translate text from source language to target language.
    """

    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)

    return translated