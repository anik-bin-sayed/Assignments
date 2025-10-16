// responsive nav menu
const hamburger = document.getElementById("hamburger");
const navMenu = document.querySelector(".nav__links");

// handle toggle menu
const toggleMenu = () => {
  navMenu.classList.toggle("active");
  // console.log("clicked");
};

hamburger.addEventListener("click", toggleMenu);
