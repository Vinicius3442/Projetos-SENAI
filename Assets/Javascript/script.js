// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });

    // Update active link
    document.querySelectorAll(".nav-links a").forEach((link) => {
      link.classList.remove("active");
    });
    this.classList.add("active");
  });
});

// Animation on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
  });
});

const hiddenElements = document.querySelectorAll(
  ".skills-card, .timeline-item"
);
hiddenElements.forEach((el) => {
  el.classList.add("hidden");
  observer.observe(el);
});

(function () {
  emailjs.init("tSRfpA16QKlRch5It");
})();

document.getElementById("emailForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const status = document.getElementById("formStatus");
  status.textContent = "Enviando...";
  emailjs
    .send("service_dzli1jr", "template_bq1r32m", {
      from_name: document.getElementById("name").value,
      from_email: document.getElementById("email").value,
      message: document.getElementById("message").value,
    })
    .then(
      function () {
        status.style.color = "var(--primary)";
        status.textContent = "Mensagem enviada com sucesso!";
        document.getElementById("emailForm").reset();
      },
      function (error) {
        status.style.color = "var(--accent)";
        status.textContent = "Erro ao enviar. Tente novamente.";
      }
    );
});
