document.querySelectorAll(".testimonial-slider").forEach(slider => {
    let index = 0;
    const cards = slider.children;
    const visible = 3;
    const intervalTime = 3000;
  
    function move() {
      index++;
      if (index > cards.length - visible) index = 0;
      slider.style.transform = `translateX(-${index * 340}px)`;
    }
  
    let interval = setInterval(move, intervalTime);
  
    slider.addEventListener("mouseenter", () => clearInterval(interval));
    slider.addEventListener("mouseleave", () => {
      interval = setInterval(move, intervalTime);
    });
  });
  