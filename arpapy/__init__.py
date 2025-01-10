# -*- coding: utf-8 -*-
from .model.phoneme import Phoneme
from .model.stress import Stress
from .excepts import PhonemeError
from .arpa import get_arpa
from .const import vowels, consonants, auxiliary, all_diacritics_ipa, suprasegmental_duration_ipa, suprasegmental_prosodic_ipa, suprasegmental_pitch_ipa

def get_supported_arphabet():
    return set([o.arpabet for o in vowels + consonants + auxiliary])
