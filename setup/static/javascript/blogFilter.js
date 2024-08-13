document.addEventListener("DOMContentLoaded", () => {
  const checkboxes = document.querySelectorAll(".filter");
  const posts = document.querySelectorAll(".blog-post_card");

  const filterPosts = () => {
    const selectedCategories = Array.from(checkboxes)
      .filter((checkbox) => checkbox.checked && checkbox.value !== "all")
      .map((checkbox) => checkbox.value.toLowerCase()); // Convertendo para lowercase

    posts.forEach((post) => {
      const postCategories = post
        .getAttribute("data-tags")
        .toLowerCase()
        .split(" "); // Convertendo para lowercase

      // Exibe ou oculta o post com base nas categorias selecionadas
      if (
        selectedCategories.length === 0 ||
        selectedCategories.some((category) => postCategories.includes(category))
      ) {
        post.style.display = "flex";
      } else {
        post.style.display = "none";
      }
    });
  };

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      // Se "Todos" for selecionado, desmarca outros filtros
      if (checkbox.value === "all") {
        checkboxes.forEach((cb) => {
          if (cb.value !== "all") cb.checked = false;
        });
      } else {
        // Se qualquer outro filtro for selecionado, desmarca "Todos"
        document.getElementById("filter_all").checked = false;
      }

      filterPosts();
    });
  });

  // Executa o filtro na inicialização para garantir o estado inicial
  filterPosts();
});

document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const postsContainer = document.getElementById("posts-container");

  // Adiciona um ouvinte de evento para a entrada de texto
  searchInput.addEventListener("input", function () {
    const searchTerm = searchInput.value.toLowerCase();
    const posts = postsContainer.querySelectorAll(".blog-post_card");

    // Filtra os posts com base no termo de pesquisa
    posts.forEach((post) => {
      const title = post
        .querySelector(".blog-post_content h3")
        .textContent.toLowerCase();

      if (title.includes(searchTerm)) {
        post.style.display = "flex"; // Mostra o post se corresponder
      } else {
        post.style.display = "none"; // Oculta o post se não corresponder
      }
    });
  });
});
