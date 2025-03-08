document.addEventListener('DOMContentLoaded', function() {
    // Animation on scroll
    AOS.init({
      duration: 800,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
    
    // Navbar scroll effect
    const selectHeader = document.querySelector('#header');
    if (selectHeader) {
      document.addEventListener('scroll', () => {
        window.scrollY > 100 
          ? selectHeader.classList.add('scrolled')
          : selectHeader.classList.remove('scrolled');
      });
    }
    
    // Back to top button
    const backtotop = document.querySelector('.back-to-top');
    if (backtotop) {
      const toggleBacktotop = () => {
        if (window.scrollY > 100) {
          backtotop.classList.add('active');
        } else {
          backtotop.classList.remove('active');
        }
      };
      window.addEventListener('load', toggleBacktotop);
      document.addEventListener('scroll', toggleBacktotop);
    }
    
    // Mobile nav toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    document.querySelectorAll('.nav-link').forEach(navLink => {
      navLink.addEventListener('click', () => {
        if (navbarCollapse.classList.contains('show')) {
          navbarToggler.click();
        }
      });
    });
    
    // Preloader
    const preloader = document.querySelector('#preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        setTimeout(() => {
          preloader.remove();
        }, 1000);
      });
    }
  });