// Archivo JS para los Botones de me gusta con los iconos incluidos

document.addEventListener("DOMContentLoaded",() => {
    console.log('DOM cargado');

    // Selecciono todos los botones de megusta
    const likeButtons = document.querySelectorAll('a.likeButton');

    // De cada uno de ellos cojo su Span y modifico su valor de Likes y caambio el icono si corresponde
    likeButtons.forEach(likeButton => {
        let nLikesSpan = likeButton.querySelector('span');
        let nLikes = parseInt(nLikesSpan.innerHTML);
        likeButton.addEventListener('click',(event) => {

        // Prevenimos el comportamiento por defecto del boton
        event.preventDefault();

        // Hacemos una peticion GET al href del boton
        fetch(likeButton.href)
            .then(response => response.json())
            .then(data => {

                // Si la peticion fue exitosa, cambiamos el contenido del boton
                if (data.liked) {
                    nLikes += 1;
                    likeButton.innerHTML = `<span>${nLikes} </span><i class="bi bi-suit-heart-fill">`;
                    
                // Si la peticion fue Falsa, cambiamos el contenido del boton
                } else {
                    nLikes -= 1;
                    likeButton.innerHTML = `<span>${nLikes} </span><i class="bi bi-heart">`;
                }
            });
        })
    })
})
