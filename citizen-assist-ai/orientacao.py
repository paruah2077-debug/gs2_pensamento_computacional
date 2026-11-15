class Orientacao:
    def __init__(self, dados):
        campos = ["id", "categoria", "titulo", "palavras_chave", "resposta",
                  "documentos", "onde", "fonte", "verificado_em"]
        if not isinstance(dados, dict):
            raise ValueError("Cada orientação precisa ser um objeto JSON.")
        faltantes = [campo for campo in campos if campo not in dados]
        if faltantes:
            raise ValueError(f"Campos ausentes na orientação: {', '.join(faltantes)}")
        if not isinstance(dados["palavras_chave"], list) or len(dados["palavras_chave"]) < 3:
            raise ValueError("Cada orientação precisa ter pelo menos 3 palavras-chave.")
        if not isinstance(dados["documentos"], list):
            raise ValueError("O campo 'documentos' precisa ser uma lista.")
        self.id = dados["id"]
        self.categoria = dados["categoria"]
        self.titulo = dados["titulo"]
        self.palavras_chave = dados["palavras_chave"]
        self.resposta = dados["resposta"]
        self.documentos = dados["documentos"]
        self.onde = dados["onde"]
        self.fonte = dados["fonte"]
        self.verificado_em = dados["verificado_em"]

    def exibir(self, pontos=None):
        print("\n>>", self.titulo, f"[{self.categoria}]")
        if pontos is not None:
            print(f"Pontuação: {pontos}")
        print(self.resposta)
        print("Documentos ou informações necessárias:")
        if self.documentos:
            for documento in self.documentos:
                print(f"  - {documento}")
        else:
            print("  - Consulte a fonte oficial para verificar os requisitos do seu caso.")
        print("Onde:", self.onde)
        print(f"Fonte: {self.fonte} (verificado em {self.verificado_em})")
        print("Aviso: este assistente NÃO é um canal oficial.")
