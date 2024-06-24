from django.shortcuts import render

def index(request):
    navigation = [
        {
            'title': 'HOME',
            'icon': 'fas fa-house',
            'url': 'index',
            'dropdown': [
                {'title': 'Banner', 'url': '#banner'},
                {'title': 'Sobre', 'url': '#about'},
                {'title': 'Serviços', 'url': '#services'},
                {'title': 'Projetos', 'url': '#projects'},
                {'title': 'Blog', 'url': '#blog'},
                {'title': 'Contato', 'url': '#contact'},
            ]
        },
        {
            'title': 'SOBRE NÓS',
            'icon': 'fas fa-user',
            'url': '#',
            'dropdown': [
                {'title': 'Sobre Nós', 'url': '#aboutus'},
                {'title': 'Serviços', 'url': '#services'},
                {'title': 'História', 'url': '#history'},
                {'title': 'Membros', 'url': '#members'},
            ]
        },
        {
            'title': 'SERVIÇOS',
            'icon': 'fas fa-computer',
            'url': '#',
            'dropdown': [
                {'title': 'Serviços', 'url': '#services'},
            ]
        },
        {
            'title': 'Projetos',
            'icon': 'fas fa-file-lines',
            'url': '#',
            'dropdown': []
        },
        {
            'title': 'Blog',
            'icon': 'fas fa-blog',
            'url': '#',
            'dropdown': []
        },
        {
            'title': 'Contate',
            'icon': 'fas fa-phone',
            'url': '#',
            'dropdown': [
                {'title': 'FAQ', 'url': '#'},
                {'title': 'Testemunho', 'url': '#'},
                {'title': 'Contato', 'url': '#'},
            ]
        },
    ]
 
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
 
    #PATH
    return render(request, 'vinme/index.html', 
                  {'navigation': navigation, 
                   'social_links': social_links,
                   'info_boxes': info_boxes,
                    'services': services
                   })
