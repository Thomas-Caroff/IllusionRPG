def quadgram_extracter(varchar: str):
    return varchar.split("-")

def quadgram_compacter(quadgram_list: list):
    return "-".join(quadgram_list)