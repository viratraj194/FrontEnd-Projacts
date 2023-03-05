setInterval(function() {
    const firstCard = document.querySelector(".book_card:first-child");
    const cardWidth = firstCard.offsetWidth;
    const container = document.querySelector(".cards-container");

    container.style.transition = "transform 0.5s ease-in-out";
    container.style.transform = "translateX(-" + cardWidth + "px)";

    setTimeout(function() {
        container.appendChild(firstCard);
        container.style.transition = "none";
        container.style.transform = "translateX(0)";
    }, 500);

}, 5000);