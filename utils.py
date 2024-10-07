def remove_format(cnpj: str) -> str:
    return cnpj.replace(".","").replace("/","").replace("-","")

print(remove_format("00.623.904/0001-73"))