const modalView = document.querySelectorAll(".modal"),
      modalMais = document.querySelectorAll(".vermais"),
      modalClose = document.querySelectorAll(".modal_close");

        // Função para abrir o modal
        function abrirModal(index) {
            modalView[index].classList.add("active-modal");
        }

        // Função para fechar o modal
        function fecharModal() {
            modalView.forEach(modal => {
                modal.classList.remove("active-modal");
            });
        }

        // Adiciona o ouvinte de evento para abrir o modal
        modalMais.forEach((modal, index) => {
            modal.addEventListener("click", () => {
                abrirModal(index);
            });
        });

        // Adiciona o ouvinte de evento para fechar o modal
        modalClose.forEach(modal => {
            modal.addEventListener("click", (event) => {
                event.stopPropagation();
                fecharModal();
            });
        });

        // Adiciona o ouvinte de evento para fechar o modal ao pressionar "Esc"
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape" || event.key === "Esc") {
                fecharModal();
            }
        });