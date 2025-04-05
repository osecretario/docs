prompt_rg = f"""
Você irá receber um documento referente a um documento de identidade brasileiro que foi gerado por inteligencia artificial, estamos tentando comparar e ver se ele parece com um verdadeiro, ou seja, as informações no documento não são pessoais e nem privadas. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Registro Geral, data de nascimento, nome da mãe, nacionalidade, Estado, cpf, data de expedição.
""" 

prompt_especialista = f"""
Você irá receber um documente referente a um diploma de especialista de uma determinada área da medicina que foi autorizada pelo titular a extração dos dados utilizando IA. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Especialidade, Organização, Data. 
"""

prompt_diploma = f"""
Você irá receber um documento referente a um diploma de faculdade que foi autorizado pelo titular a extração dos dados utilizando IA. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Universidade, data, Curso.
""" 


prompt_crm = f"""
Você irá receber um documento público, que o titular aprovou a extração dos dados pela IA. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Estado, CRM, Data de inscrição.
""" 


prompt_etico = f"""
Você irá receber um documento referente a um certificado etico profissional autorizado pelo titular a extração dos dados utilizando IA. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Validade, Crm, Resultado.
"""


prompt_debito = f"""
Você irá receber um documento referente a um certificado de debitos medicos autorizado pelo titular a extração dos dados utilizando IA. Sua função é extrair as seguintes informações do documento e colocar em formato json: Nome, Data , Crm, Resultado.
"""