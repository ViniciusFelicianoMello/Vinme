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
        {'url': 'index', 'icon': 'fa-solid fa-blog', 'name': 'blog'},
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
            {'url': 'index', 'icon': 'fa-solid fa-bookmark', 'label': 'favoritos'},
            {'url': 'index', 'icon': 'fa-solid fa-folder', 'label': 'arquivados'},
            {'url': 'index', 'icon': 'fa-solid fa-mug-hot', 'label': 'atividades'},
            {'url': 'index', 'icon': 'fa-solid fa-message', 'label': 'mensagens'},
            {'url': 'index', 'icon': 'fa-solid fa-bell', 'label': 'notificações'},
        ]
    
    user_config = [
            {'url': 'index', 'icon': 'fa-solid fa-gear', 'label': 'configurações'},
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
        {'id': 'tab1', 'image': 'assets/img/EmBreve1.png', 'seemore': 'Ver mais'},
        {'id': 'tab2', 'image': 'assets/img/EmBreve2.png', 'seemore': 'Ver mais'},
        {'id': 'tab3', 'image': 'assets/img/EmBreve3.png', 'seemore': 'Ver mais'},
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
        'members_card': members_card,
        'services': services,
        'projects': projects,
        'contact_info': contact_info,
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
        {'url': '#histoy', 'icon': 'fa-solid fa-book-open', 'text': 'História'},
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
    context = add_pages_context({})
    return render(request, 'vinme/projects.html', context)

def contact(request):
    travel = [
        {'url': '#FAQ', 'icon': 'fa-solid fa-question', 'text': 'FAQ'},
        {'url': '#testmonial', 'icon': 'fa-solid fa-comments', 'text': 'Testemunho'},
        {'url': '#contact', 'icon': 'fa-solid fa-phone', 'text': 'Contato'},
    ]
    context = {'travel': travel}
    context = add_pages_context(context)
    return process_contact_form(request, 'vinme/contact.html', context)

def thankspage(request):
    return render(request, 'vinme/thankspage.html')