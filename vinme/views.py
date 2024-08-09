from django.shortcuts import render, redirect
from vinme.forms import contactForm
from vinme.models import ContactMessage
# from django.core.mail import send_mail

#pages
def pages():
    # header | footer
    vinme_links = [
        {'url': 'index', 'icon': 'fa-solid fa-house-chimney', 'name': 'home'},
        {'url': 'about', 'icon': 'fa-solid fa-user-astronaut', 'name': 'sobre nós'},
        {'url': 'services', 'icon': 'fa-solid fa-computer', 'name': 'serviços'},
        {'url': 'projects', 'icon': 'fa-solid fa-file-lines', 'name': 'projetos'},
        {'url': 'contact', 'icon': 'fa-solid fa-phone', 'name': 'contato'},
    ]

    blog_links = [
        {'url': 'blog', 'icon': 'fa-solid fa-blog', 'name': 'blog'},
    ]

    class_links = [
        {'url': 'index', 'icon': 'fa-solid fa-graduation-cap', 'name': 'school'},
    ]

    commu_links = [
        {'url': 'index', 'icon': 'fa-solid fa-rss', 'name': 'feed'},
    ]

    navigation = [
        {
            'title': 'VinMe',
            'icon': 'fa-solid fa-user-astronaut',
            'links': vinme_links
        },
        {
            'title': 'Verse',
            'icon': 'fa-solid fa-earth-americas',
            'links': blog_links
        },
        {
            'title': 'Class',
            'icon': 'fa-solid fa-school',
            'links': class_links
        },
        {
            'title': 'Community',
            'icon': 'fa-solid fa-people-group',
            'links': commu_links
        },
    ]


    user_links = [
            {'url': 'index', 'icon': 'fa-solid fa-star', 'label': 'favoritos'},
            {'url': 'index', 'icon': 'fa-solid fa-folder', 'label': 'arquivados'},
            {'url': 'index', 'icon': 'fa-solid fa-mug-hot', 'label': 'atividades'},
            {'url': 'index', 'icon': 'fa-solid fa-message', 'label': 'mensagens'},
            {'url': 'index', 'icon': 'fa-solid fa-bell', 'label': 'notificações'},
        ]
    
    user_config = [
            {'url': 'settings_view', 'icon': 'fa-solid fa-gear', 'label': 'configurações'},
            {'url': 'account_logout', 'icon': 'fa-solid fa-right-from-bracket', 'label': 'logout'},
    ]

    user_controls = [
        {
            'title': 'Perfil',
        },
        {
            'title': 'Menu',
            'links': user_links
        },
        {
            'title': 'Configurações',
            'links': user_config
        }
    ]
    
    # banner
    social_links = [
        {'url': 'https://instagram.com/viinifeliciano', 'icon': 'fa-brands fa-instagram'},
        {'url': 'https://www.linkedin.com/in/vinicius-feliciano-mello', 'icon': 'fa-brands fa-linkedin-in'},
        {'url': 'https://www.youtube.com/channel/UCPaMfm0d54sSeaX2RsCAB4A', 'icon': 'fa-brands fa-youtube'},
        {'url': 'https://www.behance.net/', 'icon': 'fa-brands fa-behance'},
    ]

    info_boxes = [
        {
            'img_src': 'assets/SVG/VINMEFRONT.svg',
            'alt_text': 'DESIGN',
            'icon': 'fa-solid fa-code',
            'title': 'Front-End'
        },
        {
            'img_src': 'assets/SVG/VINMEDESIGN.svg',
            'alt_text': 'DESIGN',
            'icon': 'fa-solid fa-pen-nib',
            'title': 'Design'
        },
        {
            'img_src': 'assets/SVG/VINMEBACK.svg',
            'alt_text': 'BACK END',
            'icon': 'fa-solid fa-keyboard',
            'title': 'Back-End'
        }
    ]

    events = [
        {'date': '29 / 05 / 2024', 'text': 'Criação e planejamento', 'icon': 'fa-scroll', 'side': 'left'},
        {'date': '12 / 06 / 2024', 'text': 'Design e identidade visual', 'icon': 'fa-pen-nib', 'side': 'left'},
        {'date': '07 / 08 / 2024', 'text': 'Lançamento do site', 'icon': 'fa-rocket', 'side': 'left'},
        {'date': '04 / 06 / 2024', 'text': 'Pesquisa de concorrentes e revisão', 'icon': 'fa-magnifying-glass', 'side': 'right'},
        {'date': '18 / 06 / 2024', 'text': 'Desenvolvimento web com Front-end e Back-end', 'icon': 'fa-laptop-code', 'side': 'right'},
        {'date': '11 / 08 / 2024', 'text': 'Primeiro trabalho realizado', 'icon': 'fa-laptop-file', 'side': 'right'}
    ]
    # membros
    members_card = [
        {
            'image': 'assets/img/fotografias/vinicius.png',
            'name': 'Vinicius Mello',
            'title': 'Fundador',
            'skills': ['Dono', 'Designer', 'Desenvolvedor', 'Analista', 'Atendente'],
            'portfolio_url': 'https://portifolio-vinicius-mello.vercel.app/',
            'linkedin_url': 'https://www.linkedin.com/in/vinicius-feliciano-mello/',
            'instagram_url': 'https://www.instagram.com/viinifeliciano',
        },
    ]
    # services
    services = [
        {
            'icon': 'fa-solid fa-laptop-code',
            'title': 'Web Design',
            'description': 'Sites personalizados e responsivos, com diversas animações e interações'
        },
        {
            'icon': 'fa-solid fa-window-restore',
            'title': 'Ui / Ux',
            'description': 'Desenvolvimento de interfaces intuitivas e atraentes para web e aplicativos'
        },
        {
            'icon': 'fa-solid fa-paintbrush',
            'title': 'Design Gráfico',
            'description': 'Criação da identidade visual completa da sua marca, além de banners, panfletos ou qualquer outro material gráfico.'
        },
        {
            'icon': 'fa-solid fa-server',
            'title': 'Programação',
            'description': 'Manutenção e atualizações, com extrema segurança, desempenho e otimização, sempre implementando melhorias contínuas'
        },
        {
            'icon': 'fa-solid fa-database',
            'title': 'Banco de dados',
            'description': 'Implementação e manutenção de banco de dados seguros e eficientes'
        },
        {
            'icon': 'fa-solid fa-robot',
            'title': 'Desenvolvimento',
            'description': 'Criação de plataformas completas com diversos sistemas integrados'
        }
    ]
    #projects
    projects = [
        {'id': 'tab1', 'image': 'assets/img/EmBreve1.png'},
        {'id': 'tab2', 'image': 'assets/SVG/VINME/VinmeIDE.svg'},
        {'id': 'tab3', 'image': 'assets/img/Backend.png'},
    ]

    projectsList = [
        {
            'background_image': 'assets/img/EmBreve1.png',
            'links': '#',
            'images': [
                'assets/img/projects/vinme/vinme1.png',
                'assets/img/projects/vinme/vinme2.png',
                'assets/img/projects/vinme/vinme3.png',
            ]
        },
        {
        },
        {
        },
        {
        },
    ]
    #contact
    contact_info = [
        {
            'icon': 'fa-face-laugh-squint', 
            'text': 'Vinicius Feliciano Mello', 
            'url': 'https://portifolio-vinicius-mello.vercel.app/'
        },
        {
            'icon': 'fa-envelope', 
            'text': 'vinme.geral@gmail.com',
            'url':  'contact'
        },
        {
            'icon': 'fa-phone', 
            'text': '(11) 9 7174-7781', 
            'url': 'https://wa.me/message/66LU3HDFMEWVO1'
        },
        {
            'icon': 'fa-location-dot', 
            'text': 'São Paulo, SP, Brasil'
        },
        {
            'icon': 'fa-clock', 
            'text': '8:00 - 18:00'
        }
    ]

    faqs = [
        {
            'question': 'O que é a VINME e porque nos escolher?',
            'answer': 'A VINME é uma startup especializada em desenvolvimento web, back-end e design gráfico. Nosso diferencial é a combinação de criatividade, inovação e foco na satisfação do cliente. Oferecemos soluções personalizadas, colaboramos com nossos clientes para entregar as melhores soluções para seus problemas.'
        },
        {
            'question': 'Vocês oferecem suporte e manutenção após a entrega do projeto?',
            'answer': 'Sim, oferecemos suporte e manutenção contínua para garantir que seu website funcione perfeitamente. Estamos disponíveis para implementar atualizações, resolver problemas técnicos e fazer melhorias conforme necessário.'
        },
        {
            'question': 'Qual é o processo de desenvolvimento de um website?',
            'answer': 'Nosso processo de desenvolvimento web inclui uma reunião inicial para entender as suas necessidades e objetivos, planejamento e esboço do projeto, design de interface e experiencia do usuario, desenvolvimento e programação, testes e revisões, e por fim, lançamento e suporte pos-lançamento'
        },
        {
            'question': 'Como posso solicitar um orçamento para um projeto?',
            'answer': 'Você pode solicitar um orçamento entrando em contato conosco através do formulário de contato em nosso site ou enviando um e-mail para vinme.geral@gmail.com. Nossa equipe retornará o contato o mais rápido possível para discutir os detalhes do seu projeto e fornecer um orçamento personalizado.'
        },
        {
            'question': 'Quais são os prazos de entrega para os projetos?',
            'answer': 'Os prazos de entrega variam dependendo da complexidade e do escopo do projeto. Após a reunião inicial, forneceremos um cronograma detalhado com os prazos estimados para cada etapa do projeto.'
        },
        {
            'question': 'Como funciona o processo de criação de identidade visual?',
            'answer': 'O processo de criação de identidade visual inclui reunião inicial para entender a visão e os valores da sua marca, pesquisa e brainstorming de conceitos, desenvolvimento de esboços e propostas, revisões e ajustes com base no seu feedback e entrega dos arquivos finais em diversos formatos para uso em diferentes mídias.'
        },
        {
            'question': 'Vocês trabalham com empresas de quais setores?',
            'answer': 'Trabalhamos com empresas de diversos setores, incluindo tecnologia, e-commerce, saúde, educação, entretenimento e muito mais. Nossa abordagem flexível nos permite adaptar nossos serviços às necessidades específicas de cada cliente.'
        },
        {
            'question': 'Quais são as garantias oferecidas pela VINME?',
            'answer': 'Garantimos a entrega de serviços de alta qualidade, alinhados com as suas expectativas. Oferecemos suporte pós-lançamento para resolver qualquer problema que possa surgir e garantir a satisfação do cliente.'
        },
        {
            'question': 'Vocês fazem redesign de sites existentes?',
            'answer': 'Sim, oferecemos serviços de redesign para modernizar e melhorar a performance de sites existentes. Analisamos o site atual, identificamos áreas de melhoria e implementamos um novo design alinhado com as melhores práticas e tendências atuais.'
        },
    ]

    context = {
        'vinme_links': vinme_links, 
        'blog_links': blog_links, 
        'class_links': class_links, 
        'commu_links': commu_links, 
        'navigation': navigation, 
        'user_links': user_links, 
        'user_config': user_config, 
        'user_controls': user_controls, 
        'social_links': social_links,
        'info_boxes': info_boxes,
        'events': events,
        'members_card': members_card,
        'services': services,
        'projects': projects,
        'projectsList': projectsList,
        'contact_info': contact_info,
        'faqs': faqs,
    }
    return context

def add_pages_context(context):
    pages_context = pages()
    context.update(pages_context)
    return context

# contact form
def process_contact_form(request, template_name, context=None):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankspage')
    else:
        form = contactForm()

    if context is None:
        context = {}
    context['form'] = form
    return render(request, template_name, context)

def index(request):
    travel = [
        {'url': '#banner', 'icon': 'fa-solid fa-pager', 'text': 'Banner'},
        {'url': '#about', 'icon': 'fa-solid fa-user-astronaut', 'text': 'Sobre nós'},
        {'url': '#services', 'icon': 'fa-solid fa-computer', 'text': 'Serviços'},
        {'url': '#projects', 'icon': 'fa-solid fa-file-lines', 'text': 'Projetos'},
        {'url': '#contact', 'icon': 'fa-solid fa-phone', 'text': 'Contato'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return process_contact_form(request, 'vinme/index.html', context)

def about(request):
    travel = [
        {'url': '#about', 'icon': 'fa-solid fa-user-astronaut', 'text': 'Sobre nós'},
        {'url': '#history', 'icon': 'fa-solid fa-book-open', 'text': 'História'},
        {'url': '#membros', 'icon': 'fa-solid fa-users', 'text': 'Membros'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return render(request, 'vinme/about.html', context)

def services(request):
    travel = [
        {'url': '#services', 'icon': 'fa-solid fa-computer', 'text': 'Serviços'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return render(request, 'vinme/services.html', context)

def projects(request):
    travel = [
        {'url': '#projects', 'icon': 'fa-solid fa-file-lines', 'text': 'Projetos'},
        {'url': '#projectsList', 'icon': 'fa-solid fa-file-lines', 'text': 'Todos os projetos'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return render(request, 'vinme/projects.html', context)

def contact(request):
    travel = [
        {'url': '#faq', 'icon': 'fa-solid fa-question', 'text': 'FAQ'},
        {'url': '#testmonial', 'icon': 'fa-solid fa-comments', 'text': 'Testemunho'},
        {'url': '#contact', 'icon': 'fa-solid fa-phone', 'text': 'Contato'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return process_contact_form(request, 'vinme/contact.html', context)

def thankspage(request):
    return render(request, 'vinme/thankspage.html')