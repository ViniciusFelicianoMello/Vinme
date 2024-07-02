from django.shortcuts import render, redirect
from vinme.forms import contactForm
from django.core.mail import send_mail

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
        'social_links': social_links,
        'info_boxes': info_boxes,
        'services': services,
        'projects': projects,
        'contact_info': contact_info,
    }
    return context

def process_contact_form(request, template_name):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_email(name, email, subject, message)

            return redirect('thankspage')
    else:
        form = contactForm()

    context = {
        'form': form,
        **pages()
    }
    return render(request, template_name, context)

def send_email(name, email, subject, message):
    email_subject = f"{subject}"
    email_content = f"Nome: {name}\nEmail: {email}\n\nMensagem:\n{message}"
    send_mail(email_subject, email_content, 'vinme.geral@gmail.com', ['vinme.geral@gmail.com'])


def index(request):
    return process_contact_form(request, 'vinme/index.html')

def about(request):
    return process_contact_form(request, 'vinme/about.html')

def services(request):
    return process_contact_form(request, 'vinme/services.html')

def projects(request):
    return process_contact_form(request, 'vinme/projects.html')

def contact(request):
    return process_contact_form(request, 'vinme/contact.html')

def thankspage(request):
    return render(request, 'vinme/thankspage.html')