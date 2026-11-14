/* ========================================
   DE-GREAT WELD ENTERPRISES - Main JavaScript
   ======================================== */

document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', function() {
    // Initialize smooth scrolling
    initSmoothScroll();
    
    // Initialize mobile menu
    initMobileMenu();
    
    // Initialize form handling
    initForms();

    // Initialize photo galleries
    initPhotoCarousels();
    initPhotoLightbox();
});

function initPhotoCarousels() {
    document.querySelectorAll('[data-photo-carousel]').forEach(carousel => {
        const slides = Array.from(carousel.querySelectorAll('[data-carousel-slide]'));
        const previous = carousel.querySelector('[data-carousel-previous]');
        const next = carousel.querySelector('[data-carousel-next]');
        const count = carousel.querySelector('[data-carousel-count]');

        if (!slides.length || !previous || !next || !count) return;

        let activeIndex = slides.findIndex(slide => slide.classList.contains('is-active'));
        if (activeIndex < 0) activeIndex = 0;

        const showSlide = index => {
            activeIndex = (index + slides.length) % slides.length;
            slides.forEach((slide, slideIndex) => {
                slide.classList.toggle('is-active', slideIndex === activeIndex);
            });
            count.textContent = `${activeIndex + 1} / ${slides.length}`;
        };

        previous.hidden = slides.length < 2;
        next.hidden = slides.length < 2;
        showSlide(activeIndex);

        previous.addEventListener('click', () => showSlide(activeIndex - 1));
        next.addEventListener('click', () => showSlide(activeIndex + 1));
    });
}

function initPhotoLightbox() {
    const triggers = document.querySelectorAll('[data-lightbox-trigger]');
    if (!triggers.length) return;

    const dialog = document.createElement('div');
    dialog.className = 'photo-lightbox';
    dialog.hidden = true;
    dialog.setAttribute('role', 'dialog');
    dialog.setAttribute('aria-modal', 'true');
    dialog.setAttribute('aria-label', 'Photo viewer');

    const image = document.createElement('img');
    image.className = 'photo-lightbox-image';
    image.alt = '';
    image.draggable = false;
    image.addEventListener('load', () => applyTransform());

    const caption = document.createElement('p');
    caption.className = 'photo-lightbox-caption';

    const close = document.createElement('button');
    close.className = 'photo-lightbox-button photo-lightbox-close';
    close.type = 'button';
    close.setAttribute('aria-label', 'Close photo viewer');
    close.textContent = '\u00d7';

    const previous = document.createElement('button');
    previous.className = 'photo-lightbox-button photo-lightbox-previous';
    previous.type = 'button';
    previous.setAttribute('aria-label', 'Previous photo');
    previous.textContent = '\u2190';

    const next = document.createElement('button');
    next.className = 'photo-lightbox-button photo-lightbox-next';
    next.type = 'button';
    next.setAttribute('aria-label', 'Next photo');
    next.textContent = '\u2192';

    const zoomOut = document.createElement('button');
    zoomOut.className = 'photo-lightbox-button photo-lightbox-zoom-out';
    zoomOut.type = 'button';
    zoomOut.setAttribute('aria-label', 'Zoom out');
    zoomOut.textContent = '\u2212';

    const zoomReset = document.createElement('button');
    zoomReset.className = 'photo-lightbox-button photo-lightbox-zoom-reset';
    zoomReset.type = 'button';
    zoomReset.setAttribute('aria-label', 'Reset zoom');
    zoomReset.textContent = '100%';

    const zoomIn = document.createElement('button');
    zoomIn.className = 'photo-lightbox-button photo-lightbox-zoom-in';
    zoomIn.type = 'button';
    zoomIn.setAttribute('aria-label', 'Zoom in');
    zoomIn.textContent = '+';

    const count = document.createElement('span');
    count.className = 'photo-lightbox-count';
    count.setAttribute('aria-live', 'polite');

    const frame = document.createElement('div');
    frame.className = 'photo-lightbox-frame';
    const zoomControls = document.createElement('div');
    zoomControls.className = 'photo-lightbox-zoom-controls';
    zoomControls.append(zoomOut, zoomReset, zoomIn);

    frame.append(image, close, previous, next, zoomControls);

    const footer = document.createElement('div');
    footer.className = 'photo-lightbox-footer';
    footer.append(caption, count);

    const content = document.createElement('div');
    content.className = 'photo-lightbox-content';
    content.append(frame, footer);
    dialog.append(content);
    document.body.append(dialog);

    let galleryTriggers = [];
    let activeIndex = 0;
    let returnFocus = null;
    let scale = 1;
    let offsetX = 0;
    let offsetY = 0;
    let dragStart = null;
    let pinchStart = null;
    const pointers = new Map();
    const minScale = 1;
    const maxScale = 5;

    const applyTransform = () => {
        const frameRect = frame.getBoundingClientRect();
        const maxX = Math.max(0, (image.offsetWidth * scale - frameRect.width) / 2);
        const maxY = Math.max(0, (image.offsetHeight * scale - frameRect.height) / 2);
        offsetX = Math.max(-maxX, Math.min(maxX, offsetX));
        offsetY = Math.max(-maxY, Math.min(maxY, offsetY));
        image.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(${scale})`;
        image.classList.toggle('is-zoomed', scale > 1);
        zoomReset.textContent = `${Math.round(scale * 100)}%`;
        zoomOut.disabled = scale <= minScale;
        zoomIn.disabled = scale >= maxScale;
    };

    const setScale = newScale => {
        scale = Math.max(minScale, Math.min(maxScale, newScale));
        if (scale === minScale) {
            offsetX = 0;
            offsetY = 0;
        }
        applyTransform();
    };

    const pointerDistance = () => {
        const points = Array.from(pointers.values());
        return Math.hypot(points[0].x - points[1].x, points[0].y - points[1].y);
    };

    const showPhoto = index => {
        activeIndex = (index + galleryTriggers.length) % galleryTriggers.length;
        const trigger = galleryTriggers[activeIndex];
        const alt = trigger.dataset.lightboxAlt || '';
        scale = 1;
        offsetX = 0;
        offsetY = 0;
        image.src = trigger.dataset.lightboxSrc;
        image.alt = alt;
        image.style.transform = '';
        caption.textContent = alt;
        count.textContent = `${activeIndex + 1} / ${galleryTriggers.length}`;
        previous.hidden = galleryTriggers.length < 2;
        next.hidden = galleryTriggers.length < 2;
        applyTransform();
    };

    const closeDialog = () => {
        dialog.hidden = true;
        document.body.classList.remove('photo-lightbox-open');
        image.removeAttribute('src');
        if (returnFocus) returnFocus.focus();
    };

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const carousel = trigger.closest('[data-photo-carousel]');
            galleryTriggers = Array.from(carousel.querySelectorAll('[data-lightbox-trigger]'));
            returnFocus = trigger;
            showPhoto(galleryTriggers.indexOf(trigger));
            dialog.hidden = false;
            document.body.classList.add('photo-lightbox-open');
            close.focus();
        });
    });

    close.addEventListener('click', closeDialog);
    previous.addEventListener('click', () => showPhoto(activeIndex - 1));
    next.addEventListener('click', () => showPhoto(activeIndex + 1));
    zoomOut.addEventListener('click', () => setScale(scale - 0.5));
    zoomIn.addEventListener('click', () => setScale(scale + 0.5));
    zoomReset.addEventListener('click', () => setScale(minScale));
    frame.addEventListener('wheel', event => {
        event.preventDefault();
        setScale(scale + (event.deltaY < 0 ? 0.25 : -0.25));
    }, { passive: false });
    frame.addEventListener('pointerdown', event => {
        if (event.target.closest('.photo-lightbox-button')) return;
        frame.setPointerCapture(event.pointerId);
        pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
        if (pointers.size === 1) {
            dragStart = { x: event.clientX, y: event.clientY, offsetX, offsetY };
        } else if (pointers.size === 2) {
            pinchStart = { distance: pointerDistance(), scale };
            dragStart = null;
        }
    });
    frame.addEventListener('pointermove', event => {
        if (!pointers.has(event.pointerId)) return;
        pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
        if (pointers.size === 2 && pinchStart) {
            setScale(pinchStart.scale * pointerDistance() / Math.max(1, pinchStart.distance));
        } else if (pointers.size === 1 && dragStart && scale > 1) {
            offsetX = dragStart.offsetX + event.clientX - dragStart.x;
            offsetY = dragStart.offsetY + event.clientY - dragStart.y;
            applyTransform();
        }
    });
    const finishPointer = event => {
        pointers.delete(event.pointerId);
        if (pointers.size < 2) pinchStart = null;
        if (pointers.size === 1) {
            const remaining = Array.from(pointers.values())[0];
            dragStart = { x: remaining.x, y: remaining.y, offsetX, offsetY };
        } else {
            dragStart = null;
        }
    };
    frame.addEventListener('pointerup', finishPointer);
    frame.addEventListener('pointercancel', finishPointer);
    dialog.addEventListener('click', event => {
        if (event.target === dialog) closeDialog();
    });
    document.addEventListener('keydown', event => {
        if (dialog.hidden) return;
        if (event.key === 'Escape') closeDialog();
        if (event.key === 'ArrowLeft' && galleryTriggers.length > 1) showPhoto(activeIndex - 1);
        if (event.key === 'ArrowRight' && galleryTriggers.length > 1) showPhoto(activeIndex + 1);
        if (event.key === '+' || event.key === '=') setScale(scale + 0.5);
        if (event.key === '-') setScale(scale - 0.5);
        if (event.key === '0') setScale(minScale);
        if (event.key === 'Tab') {
            const focusable = [close, previous, next, zoomOut, zoomReset, zoomIn].filter(button => !button.hidden);
            const first = focusable[0];
            const last = focusable[focusable.length - 1];
            if (event.shiftKey && document.activeElement === first) {
                event.preventDefault();
                last.focus();
            } else if (!event.shiftKey && document.activeElement === last) {
                event.preventDefault();
                first.focus();
            }
        }
    });
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Initialize mobile menu toggle
 */
function initMobileMenu() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');

    if (!menuToggle || !navMenu) return;

    const closeMenu = () => {
        navMenu.classList.remove('active');
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', 'Open navigation menu');
    };

    menuToggle.addEventListener('click', () => {
        const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
        navMenu.classList.toggle('active', !isExpanded);
        menuToggle.setAttribute('aria-expanded', String(!isExpanded));
        menuToggle.setAttribute('aria-label', isExpanded ? 'Open navigation menu' : 'Close navigation menu');
    });

    navMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') closeMenu();
    });

    window.addEventListener('resize', () => {
        if (window.matchMedia('(min-width: 769px)').matches) closeMenu();
    });
}

/**
 * Initialize form handling with validation
 */
function initForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Basic validation
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
}

/**
 * Format phone numbers
 */
function formatPhoneNumber(input) {
    const value = input.value.replace(/\D/g, '');
    
    if (value.length <= 7) {
        input.value = value;
    } else if (value.length <= 10) {
        input.value = value.slice(0, 3) + '-' + value.slice(3);
    } else {
        input.value = value.slice(0, 3) + '-' + value.slice(3, 6) + '-' + value.slice(6, 10);
    }
}

/**
 * Handle WhatsApp redirects with pre-filled messages
 */
function redirectToWhatsApp(phone, message) {
    const encodedMessage = encodeURIComponent(message);
    const whatsappUrl = `https://wa.me/${phone}?text=${encodedMessage}`;
    window.open(whatsappUrl, '_blank');
}

/**
 * Lazy load images
 */
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => observer.observe(img));
    } else {
        // Fallback for browsers without IntersectionObserver
        images.forEach(img => {
            img.src = img.getAttribute('data-src');
        });
    }
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type}`;
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 10000;
        animation: slideInRight 0.3s ease-out;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

/**
 * Track page views with Google Analytics (if enabled)
 */
function trackPageView() {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'page_view', {
            page_path: window.location.pathname,
            page_title: document.title
        });
    }
}

/**
 * Handle contact form AJAX submission
 */
async function submitContactForm(formData) {
    try {
        const response = await fetch("{% url 'core:contact' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            showToast('Message sent successfully! Redirecting to WhatsApp...', 'success');
            setTimeout(() => {
                window.open(data.whatsapp_url, '_blank');
            }, 1000);
            return true;
        } else {
            showToast('Error: ' + data.message, 'error');
            return false;
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('An error occurred. Please try again.', 'error');
        return false;
    }
}

/**
 * Validate email format
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Format currency for display
 */
function formatCurrency(amount, currency = '₦') {
    return currency + new Intl.NumberFormat('en-NG').format(amount);
}

/**
 * Initialize tooltips
 */
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltipText = this.getAttribute('data-tooltip');
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = tooltipText;
            tooltip.style.cssText = `
                position: absolute;
                background: #333;
                color: white;
                padding: 8px 12px;
                border-radius: 4px;
                font-size: 12px;
                white-space: nowrap;
                z-index: 1000;
                margin-top: 5px;
            `;
            
            this.parentElement.appendChild(tooltip);
        });
        
        element.addEventListener('mouseleave', function() {
            const tooltip = this.parentElement.querySelector('.tooltip');
            if (tooltip) tooltip.remove();
        });
    });
}

// Initialize on page load
window.addEventListener('load', function() {
    initLazyLoading();
    initTooltips();
    trackPageView();
});
