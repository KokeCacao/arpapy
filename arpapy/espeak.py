import subprocess

from .excepts import MissingLibrary
from .util import remove_suprasegmental, remove_diacritics

from typing import List


def get_ipa_transcriptions(
    phrases: List[str],
    preserve_suprasegmental=False,
    preserve_diacritics=False,
) -> List[str]:
    """
    Converts a list of phrases into their IPA transcriptions using espeak-ng.
    
    Args:
        phrases (List[str]): A list of phrases to transcribe into IPA.
        preserve_suprasegmental (bool, optional): Whether to preserve suprasegmental features in the IPA transcriptions. Defaults to False.
        preserve_diacritics (bool, optional): Whether to preserve diacritics in the IPA transcriptions. Defaults to False.
    
    Returns:
        List[str]: A list of IPA transcriptions for each phrase.
    """
    ipa_transcriptions: List[str] = []

    for phrase in phrases:
        try:
            # Execute espeak-ng with the specified options
            result: subprocess.CompletedProcess = subprocess.run(
                ["espeak-ng", "-x", phrase, "--ipa=3", "--sep=", "-q"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
            # Capture the IPA transcription from stdout
            ipa_transcriptions.append(result.stdout.strip())
        except Exception:
            # testing if espeak-ng is installed
            result: subprocess.CompletedProcess = subprocess.run(
                ["espeak-ng", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
            if "espeak" not in result.stdout.lower():
                raise MissingLibrary("espeak-ng is not installed.")
            else:
                raise

    if not preserve_suprasegmental:
        ipa_transcriptions = [
            remove_suprasegmental(ipa)
            for ipa in ipa_transcriptions
        ]
    
    if not preserve_diacritics:
        ipa_transcriptions = [
            remove_diacritics(ipa)
            for ipa in ipa_transcriptions
        ]

    return ipa_transcriptions
