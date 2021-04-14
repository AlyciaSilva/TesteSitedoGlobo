#language: pt
Funcionalidade: consultar classificação do Brasileirão

    '''Eu como usuário quero acessar a páginas de classificação do campeonato brasileiro 
    no globo esporte para consultar o primeiro colocado.'''

    Cenario: Consultar Primeiro Colocado no Brasileirao
    Dado acesso a pagina inicial do globo esporte
    Quando clico no menu brasileirao 
    E classificacao e exibida
    Então devo saber quem é o primeiro