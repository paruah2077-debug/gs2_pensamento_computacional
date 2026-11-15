from pathlib import Path

from base_conhecimento import BaseConhecimento
from assistente import Assistente


def main():
    pasta_projeto = Path(__file__).resolve().parent
    caminho_base = pasta_projeto / "data" / "base_conhecimento.json"
    base = BaseConhecimento(caminho_base)
    if not base.carregar():
        print("Não foi possível iniciar: verifique o arquivo data/base_conhecimento.json.")
        return
    assistente = Assistente("Citizen Assist AI", base)
    assistente.executar()


if __name__ == "__main__":
    main()
