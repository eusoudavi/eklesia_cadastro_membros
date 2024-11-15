# Defina a classe com os atributos que correspondem às colunas da planilha
class Entity:
    def __init__(self, data, nome_completo, data_nascimento, email, sexo, telefone, estado_civil, status, autorizacao):
        self.data = data
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.sexo = sexo
        self.telefone = telefone
        self.estado_civil = estado_civil
        self.status = status
        self.autorizacao = autorizacao

    def __repr__(self):
        return (f"MeuObjeto(data={self.data}, nome_completo={self.nome_completo}, "
                f"data_nascimento={self.data_nascimento}, email={self.email}, "
                f"sexo={self.sexo}, telefone={self.telefone}, estado_civil={self.estado_civil}, "
                f"status={self.status}, autorizacao={self.autorizacao})")
