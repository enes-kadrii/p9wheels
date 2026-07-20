document.addEventListener('DOMContentLoaded', () => {
    // Header Scroll Effect
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Initial Animations with GSAP
    if (typeof gsap !== 'undefined') {
        // Hero Animation (only if hero exists)
        if (document.querySelector('.hero')) {
            const tl = gsap.timeline();
            
            tl.fromTo('.hero-bg img', 
                { scale: 1.1 }, 
                { scale: 1, duration: 2, ease: 'power2.out' }
            )
            .from('.hero h1', 
                { y: 50, opacity: 0, duration: 1, ease: 'power3.out' },
                "-=1.5"
            )
            .from('.hero p', 
                { y: 30, opacity: 0, duration: 1, ease: 'power3.out' },
                "-=1.2"
            )
            .from('.hero-btns .btn', 
                { y: 20, opacity: 0, duration: 0.8, stagger: 0.2, ease: 'power3.out' },
                "-=1"
            )
            .from('header', 
                { y: -20, duration: 1, ease: 'power2.out' },
                "-=1.5"
            );
        } else {
            // If no hero (e.g., on Gallery page), just animate the header
            gsap.from('header', { y: -20, duration: 1, ease: 'power2.out' });
        }
    }

    // Mobile Menu Logic
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const closeBtn = document.querySelector('.close-menu');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (mobileBtn && mobileMenu && closeBtn) {
        mobileBtn.addEventListener('click', () => {
            mobileMenu.classList.add('open');
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });

        closeBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('open');
            document.body.style.overflow = '';
        });

        // Close when clicking a link
        const menuLinks = mobileMenu.querySelectorAll('a');
        menuLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    // Scroll Animations (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply animation classes to elements dynamically
    const elementsToAnimate = document.querySelectorAll('.card, .gallery-item, .story-content, .story-image, .page-header, .feature-text, .contact-form-wrapper');
    
    elementsToAnimate.forEach((el, index) => {
        el.classList.add('fade-up-element');
        
        // Add staggering if it's a grid item (like cards or gallery items)
        if (el.classList.contains('card') || el.classList.contains('gallery-item') || el.classList.contains('wheel-card')) {
            const staggerDelay = (index % 3) + 1; // 1, 2, or 3
            el.classList.add(`stagger-${staggerDelay}`);
        }
        
        observer.observe(el);
    });
});

