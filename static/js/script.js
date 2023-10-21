document.addEventListener("DOMContentLoaded", function () {
    const postTitle = document.querySelectorAll('[id^="titulo"]');


    postTitle.forEach(function (title) {
        title.addEventListener("click", function () {
            const postId = this.id.replace("titulo", "");
            const modal = document.querySelector('dialog[data-post-id="' + postId + '"]');
            modal.style.display = 'block';
            
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