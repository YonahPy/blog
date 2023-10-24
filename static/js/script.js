document.addEventListener("DOMContentLoaded", function () {
    const postTitle = document.querySelectorAll('.post-titulo');


    postTitle.forEach(function (title) {
        title.addEventListener("click", function () {
            const modal = title.nextElementSibling;
            if (modal.style.display === 'block'){
              modal.style.display = 'none';
            } else{
              modal.style.display = 'block'
            }
            
            
        });
    });
});

const closeButtons = document.querySelectorAll(".fechar");

  closeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const modal = button.closest("dialog");
      modal.style.display = 'none';
    });
  });