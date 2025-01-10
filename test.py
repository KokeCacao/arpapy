from arpapy import PhonemeError
from arpapy import get_arpa
from typing import List


if __name__ == '__main__':
    s: str = "What are you doing right now? Are you getting some food?"
    ls: List[str] = s.split(" ") # type: ignore
    print(get_arpa(ls))
    print(get_arpa(s))
    
    # load CMU dict
    import pathlib
    path = pathlib.Path("/home/koke_cacao/Documents/Koke_Cacao/Python/WorkSpace/GPT-SoVITS/GPT_SoVITS/text/cmudict-fast.rep")
    words = []
    with open(path, "r") as f:
        for line in f:
            if line.startswith(";;;"):
                continue
            word = line.split(" ")[0].lower()
            words.append(word)
    for i, word in enumerate(words):
        try:
            arpa_l = get_arpa(word)
            assert len(arpa_l) > 0, f"Error processing `{word}`: arpa is None"
        except PhonemeError as e:
            print(f"({i}/{len(words)}) Error processing `{word}`: {e}")
            raise
        print(f"{i}: {arpa_l}")
    print("Done!")