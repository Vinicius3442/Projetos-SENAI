document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelector(".nav-links");
  const menuIcon = document.createElement("span");
  menuIcon.className = "mobile-menu-icon";
  menuIcon.innerHTML = '<i class="fas fa-bars"></i>';
  document.querySelector(".header-content").appendChild(menuIcon);

  menuIcon.addEventListener("click", function () {
    navLinks.classList.toggle("open");
  });

  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("open");
    });
  });
});
