document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll(".animate");
  
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("show");
          }
        });
      },
      { threshold: 0.15 }
    );
  
    elements.forEach(el => observer.observe(el));
  });
  
// Scroll progress indicator
window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY;
    const docHeight =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
  
    const scrollPercent = (scrollTop / docHeight) * 100;
    document.getElementById("scroll-progress").style.width =
      scrollPercent + "%";
  });