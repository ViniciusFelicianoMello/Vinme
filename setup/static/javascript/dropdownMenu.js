document.querySelectorAll('.seta_dropdown').forEach(function(seta) {
    seta.addEventListener('click', function() {
        const menuDiv = this.closest('.dropdown_close, .dropdown_open');

        const isOpen = menuDiv.classList.contains('dropdown_open');

        document.querySelectorAll('.dropdown_open').forEach(function(openMenu) {
            openMenu.classList.remove('dropdown_open');
            openMenu.classList.add('dropdown_close');
        });

        if (isOpen) {
            menuDiv.classList.remove('dropdown_open');
            menuDiv.classList.add('dropdown_close');
        } else {
            menuDiv.classList.remove('dropdown_close');
            menuDiv.classList.add('dropdown_open');
        }
    });
});

document.querySelectorAll('.faq_ask').forEach(item => {
    item.addEventListener('click', event => {
        const faqBox = item.closest('.faq_box');
        const isOpen = faqBox.classList.contains('faq_dropdown_open');

        document.querySelectorAll('.faq_box').forEach(box => {
            box.classList.remove('faq_dropdown_open');
        });

        if (!isOpen) {
            faqBox.classList.add('faq_dropdown_open');
        }
    });
});