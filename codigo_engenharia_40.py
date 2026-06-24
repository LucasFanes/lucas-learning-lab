# Módulo de Gestão de Ingressos utilizando Herança (POO)

class Ingresso:
    def __init__(self, nome_evento, valor):
        self.nome_evento = nome_evento
        self.valor = valor

    def exibir_valor(self):
        return self.valor

class IngressoVip(Ingresso):
    def __init__(self, nome_evento, valor, adicional_vip):
        # Chama o construtor da classe pai (Ingresso)
        super().__init__(nome_evento, valor)
        self.adicional_vip = adicional_vip

    def exibir_valor_vip(self):
        # Retorna o valor base somado à taxa do VIP
        return self.valor + self.adicional_vip

# Exemplo de teste das classes:
ingresso_comum = Ingresso("Festival de Engenharia", 50.0)
print(f"Evento: {ingresso_comum.nome_evento} | Valor Comum: R$ {ingresso_comum.exibir_valor():.2f}")

ingresso_premium = IngressoVip("Festival de Engenharia", 50.0, 35.0)
print(f"Evento: {ingresso_premium.nome_evento} | Valor VIP: R$ {ingresso_premium.exibir_valor_vip():.2f}")