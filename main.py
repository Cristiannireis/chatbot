from nltk.chat.util import Chat, reflections

# convertendo as expressões para português.

expressoes_pt = {
    'eu': 'você',
    'eu sou': 'você é',
    'eu era': 'você era',
    'eu iria': 'você iria',
    'eu irei': 'você irá',
    'meu': 'seu',
    'você': 'eu',
    'você é': 'eu sou',
    'você era': 'você era',
    'você irá': 'você irei',
    'seu': 'meu',
    

}

# Frases usadas para conversar com o bot

sentencas = [
    [
        r'oi|olá|opa|aee',
        ['olá', 'como vai?', 'tudo bem?']
    ],

    [
        r'Qual é o seu nome?',
        ['Meu nome é Cris, Em que posso ajudá-lo?'] 
     
    ],

    [
        r'(.*) sua idade',
        ['tenho poucos dias de criação']
     
    ],

    [
        r'meu nome é (.*)',
        ['oLá %1, como você está hoje?']
    ],

    [
        r'Quais linguagens você gosta de estudar?',
        ['Python', 'React', 'NodeJS']
    ],

    [
        r'qual livro você leu recentemente?',
        ['Código Limpo']
    ],

    [
        # escreva quit para sair
        r'quit',
        ['Até logo']
      
    ]

]

print("Olá sou a Cris")
chat = Chat(sentencas, expressoes_pt)
chat.converse()