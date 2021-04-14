from behave import given, when, then

#variavel com a URL do site que será interagido.
 base_url = 'https://globoesporte.globo.com/'

@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    context.web.get(base_url)
    raise NotImplementedError(u'STEP: Given acesso a pagina inicial do globo esporte')


@when(u'clico no menu brasileirao')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no menu brasileirao')


@when(u'classificacao e exibida')
def step_impl(context):
    raise NotImplementedError(u'STEP: When classificacao e exibida')


@then(u'devo saber quem é o primeiro')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo saber quem é o primeiro')