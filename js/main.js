/* ============================================================
   SCRIPT UTAMA - PORTOFOLIO ANITA TIARA SANI
   ------------------------------------------------------------
   Berisi:
   1. Animasi Background 3D (Three.js) - berjalan terus-menerus
   2. Toggle Tema Gelap/Terang (disimpan di localStorage)
   3. Widget Cuaca Real-time (Open-Meteo + Geolocation)
   4. Efek Mengetik Otomatis (Typing Effect)
   5. Navigasi: efek scroll, active link, menu mobile
   6. Scroll Reveal Animation (IntersectionObserver)
   7. Animasi Progress Bar Keahlian
   8. Animasi Angka Statistik
   9. Efek Glow Kursor
   10. Formulir Kontak
   11. Preloader (sembunyikan saat halaman siap)
   12. Scroll Progress Bar
   13. Tombol Back-to-Top
   14. Modal Detail Proyek (12 proyek)
   15. Efek 3D Tilt + Spotlight pada kartu
   16. Tombol Magnetic pada hero
   17. Dukungan prefers-reduced-motion (aksesibilitas)
   ============================================================ */

/* Pastikan seluruh kode berjalan setelah DOM siap */
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initTyping();
    initNavbar();
    initReveal();
    initSkillBars();
    initCounters();
    initCursorGlow();
    initContactForm();
    initWeather();
    init3D();
    initPreloader();
    initScrollProgress();
    initBackToTop();
    initProjectModal();
    initTiltSpotlight();
    initMagnetic();
    initLiveClock();
    initCustomCursor();
    initSectionDots();
    initScrollPercent();
    initToast();
    initFaqAccordion();
    initTestimonialCarousel();
    initClickBurst();
    initBlogReveal();
    initBlogModal();
});

/* ============================================================
   1. ANIMASI BACKGROUND 3D (THREE.JS)
   ============================================================ */
function init3D() {
    // Jika Three.js tidak termuat (misal offline), berhenti tanpa error
    if (typeof THREE === 'undefined') return;

    const canvas = document.getElementById('bg-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 30;

    const renderer = new THREE.WebGLRenderer({
        canvas: canvas,
        alpha: true,                 // background transparan
        antialias: true
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    /* --- A. Bintang / Partikel --- */
    const particleCount = 2500;
    const particleGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    // Dua warna partikel: cyan & magenta agar lebih hidup
    const colors = new Float32Array(particleCount * 3);
    const c1 = new THREE.Color(0x00f0ff);
    const c2 = new THREE.Color(0xff2ec4);
    const c3 = new THREE.Color(0x8b5cf6);
    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 140; // sebar acak di ruang
        positions[i * 3 + 1] = (Math.random() - 0.5) * 90;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 70;
        // Pilih warna acak di antara tiga warna neon
        const pick = Math.random();
        const c = pick < 0.45 ? c1 : pick < 0.75 ? c2 : c3;
        colors[i * 3] = c.r;
        colors[i * 3 + 1] = c.g;
        colors[i * 3 + 2] = c.b;
    }
    particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const particleMat = new THREE.PointsMaterial({
        size: 0.22,
        transparent: true,
        opacity: 0.9,
        vertexColors: true,       // pakai warna per-partikel
        blending: THREE.AdditiveBlending // efek menyala
    });
    const particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    /* --- A2. Partikel kecil tambahan (deep space) --- */
    const smallCount = 1000;
    const smallGeo = new THREE.BufferGeometry();
    const smallPos = new Float32Array(smallCount * 3);
    for (let i = 0; i < smallCount * 3; i++) {
        smallPos[i] = (Math.random() - 0.5) * 200;
    }
    smallGeo.setAttribute('position', new THREE.BufferAttribute(smallPos, 3));
    const smallPoints = new THREE.Points(smallGeo, new THREE.PointsMaterial({
        color: 0x93a4c3,
        size: 0.09,
        transparent: true,
        opacity: 0.35
    }));
    scene.add(smallPoints);

    /* --- B. Torus Knot wireframe (cincin 3D kompleks) --- */
    const knotGeo = new THREE.TorusKnotGeometry(6, 1.8, 128, 24);
    const knotMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true,
        transparent: true,
        opacity: 0.14
    });
    const knot = new THREE.Mesh(knotGeo, knotMat);
    knot.position.set(20, 7, -12);
    scene.add(knot);

    /* --- C. Icosahedron wireframe (bola polyhedron) --- */
    const icoGeo = new THREE.IcosahedronGeometry(4, 1);
    const icoMat = new THREE.MeshBasicMaterial({
        color: 0xff2ec4,
        wireframe: true,
        transparent: true,
        opacity: 0.2
    });
    const ico = new THREE.Mesh(icoGeo, icoMat);
    ico.position.set(-22, -10, -8);
    scene.add(ico);

    /* --- C2. Heliks DNA (dua untai titik berputar) --- */
    const helixGroup = new THREE.Group();
    const helixMat1 = new THREE.MeshBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.7 });
    const helixMat2 = new THREE.MeshBasicMaterial({ color: 0xff2ec4, transparent: true, opacity: 0.7 });
    const dotGeo = new THREE.SphereGeometry(0.35, 8, 8);
    const helixDots = [];
    for (let i = 0; i < 40; i++) {
        const t = i / 40;
        const angle = t * Math.PI * 6; // 3 lilitan
        const y = (t - 0.5) * 30;
        const r = 3.5;

        const dot1 = new THREE.Mesh(dotGeo, helixMat1);
        dot1.position.set(Math.cos(angle) * r, y, Math.sin(angle) * r);
        const dot2 = new THREE.Mesh(dotGeo, helixMat2);
        dot2.position.set(Math.cos(angle + Math.PI) * r, y, Math.sin(angle + Math.PI) * r);
        helixDots.push(dot1, dot2);
        helixGroup.add(dot1, dot2);
    }
    helixGroup.position.set(-24, 0, -20);
    scene.add(helixGroup);

    /* --- C3. Cincin raksasa mengelilingi layar --- */
    const rings = [];
    const ringColors = [0x00f0ff, 0xff2ec4, 0x8b5cf6];
    for (let i = 0; i < 3; i++) {
        const ringGeo = new THREE.TorusGeometry(14 + i * 4, 0.09, 12, 96);
        const ringMat = new THREE.MeshBasicMaterial({
            color: ringColors[i],
            transparent: true,
            opacity: 0.2 + i * 0.05,
            wireframe: true
        });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = Math.PI / 2.2 + i * 0.3;
        ring.rotation.y = i * 0.5;
        rings.push(ring);
        scene.add(ring);
    }

    /* --- D. Bola-bola neon melayang (floating orbs) --- */
    const orbGeo = new THREE.SphereGeometry(1.2, 32, 32);
    const orbColors = [0x00f0ff, 0xff2ec4, 0x8b5cf6, 0x00ffa3];
    const orbs = [];
    const orbPos = [
        [-26, 12, -18],
        [24, -14, -20],
        [2, 26, -24],
        [-10, -26, -16]
    ];
    orbPos.forEach((pos, i) => {
        const mat = new THREE.MeshBasicMaterial({
            color: orbColors[i],
            transparent: true,
            opacity: 0.5
        });
        const orb = new THREE.Mesh(orbGeo, mat);
        orb.position.set(...pos);
        orbs.push(orb);
        scene.add(orb);
    });

    /* --- D2. Bola-bola kecil berkilau (mini orbs) --- */
    const miniOrbs = [];
    const miniColors = [0x00f0ff, 0xff2ec4, 0x8b5cf6, 0x00ffa3];
    const miniPos = [
        [-14, 14, -10],
        [12, 20, -14],
        [30, -4, -22],
        [-30, -16, -12],
        [4, -6, -28]
    ];
    miniPos.forEach((pos, i) => {
        const mat = new THREE.MeshBasicMaterial({
            color: miniColors[i % miniColors.length],
            transparent: true,
            opacity: 0.7
        });
        const mini = new THREE.Mesh(new THREE.SphereGeometry(0.55, 16, 16), mat);
        mini.position.set(...pos);
        miniOrbs.push(mini);
        scene.add(mini);
    });

    /* --- E. Grid lantai digital --- */
    const grid = new THREE.GridHelper(80, 40, 0x00f0ff, 0x1a2a55);
    grid.position.y = -24;
    grid.material.transparent = true;
    grid.material.opacity = 0.2;
    scene.add(grid);

    /* --- E2. Depth fog agar terasa kedalaman ruang --- */
    scene.fog = new THREE.Fog(0x070b16, 45, 110);

    /* --- Interaksi mouse: kamera sedikit mengikuti kursor --- */
    let mouseX = 0;
    let mouseY = 0;
    document.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });

    /* --- Loop animasi --- */
    const clock = new THREE.Clock();
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Satu function untuk menghitung posisi objek & menggambar satu frame
    function renderFrame() {
        const t = clock.getElapsedTime();

        // Putar partikel perlahan
        particles.rotation.y = t * 0.04;
        particles.rotation.x = t * 0.015;

        // Putar partikel kecil deep space
        smallPoints.rotation.y = -t * 0.02;
        smallPoints.rotation.z = t * 0.01;

        // Putar torus knot
        knot.rotation.x = t * 0.18;
        knot.rotation.y = t * 0.26;
        knot.position.y = 7 + Math.sin(t * 0.4) * 2;

        // Putar icosahedron
        ico.rotation.x = t * 0.12;
        ico.rotation.z = t * 0.09;
        ico.position.y = -10 + Math.cos(t * 0.5) * 2;

        // Putar heliks DNA
        helixGroup.rotation.y = t * 0.28;

        // Rotasikan cincin raksasa pada sumbu berbeda
        rings.forEach((ring, i) => {
            ring.rotation.z = t * (0.1 + i * 0.05);
            ring.rotation.x = Math.PI / 2.2 + i * 0.3 + Math.sin(t * 0.2 + i) * 0.1;
        });

        // Gerakkan bola-bola neon (melayang naik-turun + membesar-mengecil)
        orbs.forEach((orb, i) => {
            orb.position.y += Math.sin(t * 0.5 + i * 1.3) * 0.012;
            const s = 1 + Math.sin(t * 0.8 + i * 2) * 0.25;
            orb.scale.setScalar(s);
        });

        // Mini orbs bergerak halus & berdenyut
        miniOrbs.forEach((mini, i) => {
            mini.position.y += Math.sin(t * 0.7 + i * 1.5) * 0.02;
            const s = 1 + Math.sin(t * 1.2 + i * 1.8) * 0.3;
            mini.scale.setScalar(Math.max(0.4, s));
        });

        // Kamera mengikuti posisi mouse secara halus
        camera.position.x += (mouseX * 5 - camera.position.x) * 0.04;
        camera.position.y += (-mouseY * 5 - camera.position.y) * 0.04;
        camera.lookAt(0, 0, 0);

        renderer.render(scene, camera);
    }

    // Loop animasi berjalan terus-menerus tanpa jeda
    // (tetap aktif walau tab sedang tersembunyi/diminimize)
    function animate() {
        requestAnimationFrame(animate);
        renderFrame();
    }

    // Hormati prefers-reduced-motion:
    // - reduce -> gambar satu frame statis (tanpa loop animasi)
    // - normal -> jalankan animasi 3D penuh secara terus-menerus
    if (reduceMotion) {
        renderFrame();
    } else {
        animate();
    }

    /* --- Responsif saat ukuran layar berubah --- */
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}

/* ============================================================
   2. TOGGLE TEMA GELAP/TERANG
   ============================================================ */
function initTheme() {
    const toggle = document.getElementById('theme-toggle');
    const root = document.documentElement;

    // Ambil tema tersimpan dari localStorage (jika ada)
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        root.setAttribute('data-theme', savedTheme);
    }

    toggle.addEventListener('click', () => {
        const current = root.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        localStorage.setItem('theme', next); // simpan pilihan pengguna
    });
}

/* ============================================================
   3. WIDGET CUACA REAL-TIME (OPEN-METEO, GRATIS TANPA API KEY)
   ============================================================ */
function initWeather() {
    const iconEl = document.getElementById('weather-icon');
    const tempEl = document.getElementById('weather-temp');
    const cityEl = document.getElementById('weather-city');

    /* Ambil lokasi pengguna; fallback ke Jakarta bila ditolak */
    const getLocation = () => new Promise((resolve) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (pos) => resolve({
                    lat: pos.coords.latitude,
                    lon: pos.coords.longitude
                }),
                () => resolve({ lat: -6.2088, lon: 106.8456 }), // Jakarta
                { timeout: 6000 }
            );
        } else {
            resolve({ lat: -6.2088, lon: 106.8456 });
        }
    });

    /* Petakan kode cuaca Open-Meteo ke emoji */
    const getIcon = (code) => {
        if (code === 0) return '☀️';                 // cerah
        if (code === 1) return '🌤️';                 // sedikit berawan
        if (code === 2) return '⛅';                  // berawan sebagian
        if (code === 3) return '☁️';                  // mendung
        if (code >= 45 && code <= 48) return '🌫️';  // kabut
        if (code >= 51 && code <= 57) return '🌦️';  // gerimis
        if (code >= 61 && code <= 67) return '🌧️';  // hujan
        if (code >= 71 && code <= 77) return '🌨️';  // salju
        if (code >= 80 && code <= 82) return '🌧️';  // hujan deras
        if (code >= 85 && code <= 86) return '🌨️';  // salju deras
        if (code >= 95 && code <= 99) return '⛈️';  // badai petir
        return '🌤️';
    };

    (async () => {
        try {
            const { lat, lon } = await getLocation();

            // Panggil API Open-Meteo (gratis, tanpa kunci)
            const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,weather_code&timezone=auto`;
            const res = await fetch(url);
            const data = await res.json();

            const current = data.current;
            tempEl.textContent = `${Math.round(current.temperature_2m)}°C`;
            iconEl.textContent = getIcon(current.weather_code);

            // Coba ambil nama kota via reverse geocoding gratis
            try {
                const geoRes = await fetch(
                    `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lon}&localityLanguage=id`
                );
                const geo = await geoRes.json();
                cityEl.textContent = geo.city || geo.locality || geo.principalSubdivision || 'Lokasi Anda';
            } catch (e) {
                cityEl.textContent = 'Lokasi Anda';
            }
        } catch (err) {
            // Bila gagal (offline dll), tampilkan nilai default
            iconEl.textContent = '🌤️';
            tempEl.textContent = '--°C';
            cityEl.textContent = 'Cuaca';
        }
    })();
}

/* ============================================================
   4. EFEK MENGETIK OTOMATIS (TYPING EFFECT)
   ============================================================ */
function initTyping() {
    const typeEl = document.getElementById('type-text');
    const roles = [
        'Anak Informatika',
        'Front End Developer',
        'App Developer',
        'Software Engineer',
        'Cyber Security Enthusiast',
        'Data & Analytics',
        'Finance Enthusiast',
        'Gold & Stock Investor',
        'Crypto & Blockchain',
        'Web3 & Web4 Explorer',
        'Tech Explorer'
    ];

    let roleIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function type() {
        const current = roles[roleIndex];

        if (!deleting) {
            // Mengetik huruf demi huruf
            typeEl.textContent = current.slice(0, charIndex++);
            if (charIndex > current.length) {
                deleting = true;
                setTimeout(type, 1800); // jeda saat teks penuh
                return;
            }
            setTimeout(type, 90);
        } else {
            // Menghapus huruf satu per satu
            typeEl.textContent = current.slice(0, charIndex--);
            if (charIndex < 0) {
                deleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                setTimeout(type, 300);
                return;
            }
            setTimeout(type, 45);
        }
    }
    type();
}

/* ============================================================
   5. NAVIGASI: EFEEK SCROLL, ACTIVE LINK, MENU MOBILE
   ============================================================ */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    const navLinks = document.getElementById('nav-links');
    const hamburger = document.getElementById('hamburger');

    // Tambah kelas 'scrolled' saat halaman di-scroll
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
        highlightActiveLink();
    });

    // Buka/tutup menu mobile
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    // Tutup menu mobile saat link diklik
    document.querySelectorAll('.nav-link').forEach((link) => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });

    // Tandai link navigasi sesuai section yang terlihat
    function highlightActiveLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 120;

        sections.forEach((section) => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            const link = document.querySelector(`.nav-link[href="#${section.id}"]`);

            if (scrollPos >= top && scrollPos < bottom && link) {
                document.querySelectorAll('.nav-link').forEach((l) => l.classList.remove('active'));
                link.classList.add('active');
            }
        });
    }
}

/* ============================================================
   6. SCROLL REVEAL ANIMATION
   ============================================================ */
function initReveal() {
    const revealEls = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15 }
    );
    revealEls.forEach((el) => observer.observe(el));

    // Timeline item memiliki animasi sendiri
    const timelineItems = document.querySelectorAll('.timeline-item');
    const timelineObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    timelineObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.2 }
    );
    timelineItems.forEach((el) => timelineObserver.observe(el));

    // Kartu layanan & blog memakai stagger reveal (delay berjenjang)
    const staggerEls = document.querySelectorAll('.reveal-stagger');
    const staggerObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const parent = entry.target.parentElement;
                    const children = Array.from(
                        parent.querySelectorAll('.reveal-stagger')
                    );
                    const idx = children.indexOf(entry.target);
                    entry.target.style.setProperty(
                        '--stagger-delay',
                        `${Math.min(idx, 6) * 0.1}s`
                    );
                    entry.target.classList.add('visible');
                    staggerObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.15 }
    );
    staggerEls.forEach((el) => staggerObserver.observe(el));
}

/* ============================================================
   7. ANIMASI PROGRESS BAR KEAHLIAN
   ============================================================ */
function initSkillBars() {
    const bars = document.querySelectorAll('.skill-fill');
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    // Set lebar sesuai atribut data-width
                    entry.target.style.width = entry.target.dataset.width;
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.4 }
    );
    bars.forEach((bar) => observer.observe(bar));
}

/* ============================================================
   8. ANIMASI ANGKA STATISTIK (COUNT UP)
   ============================================================ */
function initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = +el.dataset.target;
                    let current = 0;
                    const step = Math.max(1, Math.ceil(target / 60)); // kecepatan

                    const tick = () => {
                        current += step;
                        if (current >= target) {
                            el.textContent = target;
                        } else {
                            el.textContent = current;
                            requestAnimationFrame(tick);
                        }
                    };
                    tick();
                    observer.unobserve(el);
                }
            });
        },
        { threshold: 0.5 }
    );
    counters.forEach((counter) => observer.observe(counter));
}

/* ============================================================
   9. EFEK GLOW MENGIKUTI KURSOR
   ============================================================ */
function initCursorGlow() {
    const glow = document.getElementById('cursor-glow');

    // Hormati prefers-reduced-motion: sembunyikan glow kursor
    // (dekorasi ini bergerak terus mengikuti mouse).
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        glow.style.display = 'none';
        return;
    }

    let x = window.innerWidth / 2;
    let y = window.innerHeight / 2;
    let targetX = x;
    let targetY = y;

    document.addEventListener('mousemove', (e) => {
        targetX = e.clientX;
        targetY = e.clientY;
    });

    // Gerakan halus dengan requestAnimationFrame
    function move() {
        x += (targetX - x) * 0.08;
        y += (targetY - y) * 0.08;
        glow.style.left = `${x}px`;
        glow.style.top = `${y}px`;
        requestAnimationFrame(move);
    }
    move();
}

/* ============================================================
   10. FORMULIR KONTAK (DEMO TANPA BACKEND)
   ============================================================ */
function initContactForm() {
    const form = document.getElementById('contact-form');
    const status = document.getElementById('form-status');

    form.addEventListener('submit', (e) => {
        e.preventDefault(); // cegah reload halaman

        const name = document.getElementById('form-name').value.trim();
        const email = document.getElementById('form-email').value.trim();

        status.textContent = `✅ Terima kasih ${name}! Pesan Anda telah terkirim. Saya akan membalas ke ${email} secepatnya.`;
        status.style.color = 'var(--neon-green)';
        form.reset();

        // Notifikasi toast
        if (window.showToast) {
            window.showToast(`Pesan dari ${name} terkirim! 🎉`, 'success');
        }

        // Confetti sederhana
        launchConfetti();

        // Hapus pesan sukses setelah beberapa detik
        setTimeout(() => { status.textContent = ''; }, 6000);
    });

    // Confetti tanpa library eksternal
    function launchConfetti() {
        const colors = ['#00f0ff', '#ff2ec4', '#8b5cf6', '#00ffa3', '#7df9ff', '#ffd700'];
        const container = document.createElement('div');
        container.className = 'confetti-layer';
        container.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:10001;overflow:hidden;';
        document.body.appendChild(container);

        for (let i = 0; i < 60; i++) {
            const piece = document.createElement('span');
            const size = 6 + Math.random() * 8;
            const left = Math.random() * 100;
            const delay = Math.random() * 0.8;
            const duration = 2.2 + Math.random() * 2;
            piece.style.cssText = `
                position:absolute;
                top:-20px;
                left:${left}%;
                width:${size}px;
                height:${size * 0.5}px;
                background:${colors[i % colors.length]};
                border-radius:2px;
                opacity:0.9;
                animation:confettiFall ${duration}s ease-in ${delay}s forwards;
            `;
            container.appendChild(piece);
        }

        setTimeout(() => container.remove(), 6000);
    }
}

/* ============================================================
   11. PRELOADER (LOADING SCREEN)
   ============================================================ */
function initPreloader() {
    const preloader = document.getElementById('preloader');
    const percentEl = document.getElementById('preloader-percent');

    // Animasi persentase loading 0 → 100 dengan easing halus.
    // Berhenti otomatis bila halaman sudah selesai dimuat.
    let stopped = false;

    if (percentEl) {
        let p = 0;
        const target = 100;
        const step = Math.ceil(target / 40); // selesai dalam ±40 frame
        const tick = () => {
            if (stopped) return;
            p = Math.min(target, p + step);
            percentEl.textContent = `${p}%`;
            if (p < target) {
                requestAnimationFrame(tick);
            } else {
                hidePreloader();
            }
        };
        tick();
    }

    // Sembunyikan preloader setelah seluruh halaman (termasuk aset) selesai dimuat.
    // Fallback timeout 4 detik agar halaman tidak terkunci bila load lambat.
    const hidePreloader = () => {
        stopped = true;
        preloader.classList.add('hidden');
    };

    if (document.readyState === 'complete') {
        // Halaman sudah siap: sembunyikan segera
        percentEl && (percentEl.textContent = '100%');
        hidePreloader();
    } else {
        window.addEventListener('load', hidePreloader);
        setTimeout(hidePreloader, 4000); // pengaman
    }

    // Setelah transisi selesai, hapus dari aliran DOM agar tidak menutupi klik
    preloader.addEventListener('transitionend', (e) => {
        if (e.propertyName === 'opacity') preloader.style.display = 'none';
    });
}

/* ============================================================
   12. SCROLL PROGRESS BAR
   ============================================================ */
function initScrollProgress() {
    const bar = document.getElementById('scroll-progress');

    const update = () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        bar.style.width = `${progress}%`;
    };

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update(); // hitung posisi awal
}

/* ============================================================
   13. TOMBOL BACK-TO-TOP
   ============================================================ */
function initBackToTop() {
    const btn = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        btn.classList.toggle('show', window.scrollY > 600);
    }, { passive: true });

    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

/* ============================================================
   14. MODAL DETAIL PROYEK
   ============================================================ */
function initProjectModal() {
    const overlay = document.getElementById('project-modal-overlay');
    const modal = document.getElementById('project-modal');
    const body = document.getElementById('modal-body');
    const closeBtn = document.querySelector('.modal-close');

    // Data detail untuk 12 proyek (disesuaikan dengan kartu di index.html)
    const projectData = {
        1: {
            icon: '💻',
            title: 'Aplikasi E-Learning',
            desc: 'Platform belajar online interaktif dengan kuis, forum diskusi, dan pelacakan progres belajar siswa secara real-time.',
            tech: ['HTML', 'CSS', 'JavaScript'],
            points: ['Sistem kuis otomatis dengan skor instan', 'Forum diskusi antar siswa & mentor', 'Dashboard progres belajar per siswa']
        },
        2: {
            icon: '📊',
            title: 'Dashboard Analisis Data',
            desc: 'Visualisasi data penjualan menggunakan Python dan grafik interaktif untuk mendukung keputusan bisnis.',
            tech: ['Python', 'Pandas', 'Chart.js'],
            points: ['Pembersihan & eksplorasi data (EDA)', 'Grafik interaktif tren penjualan', 'Insight untuk strategi bisnis']
        },
        3: {
            icon: '🌡️',
            title: 'Sistem Monitoring Suhu',
            desc: 'Alat IoT berbasis Arduino untuk memantau suhu ruangan dan mengirim notifikasi otomatis saat melewati ambang batas.',
            tech: ['Arduino', 'C++', 'IoT'],
            points: ['Sensor suhu & kelembaban real-time', 'Notifikasi otomatis via buzzer/led', 'Log data historis']
        },
        4: {
            icon: '💳',
            title: 'Aplikasi Catatan Keuangan',
            desc: 'Aplikasi mobile untuk mengelola pemasukan, pengeluaran, dan menghasilkan laporan keuangan bulanan otomatis.',
            tech: ['React Native', 'Firebase'],
            points: ['Kategori transaksi & anggaran', 'Laporan bulanan otomatis', 'Sinkronisasi cloud real-time']
        },
        5: {
            icon: '🏢',
            title: 'Website Company Profile',
            desc: 'Website profil perusahaan modern dengan CMS sederhana dan optimasi SEO untuk visibilitas digital.',
            tech: ['Bootstrap', 'PHP', 'MySQL'],
            points: ['Konten dikelola via CMS', 'Optimasi SEO on-page', 'Responsif di semua perangkat']
        },
        6: {
            icon: '📈',
            title: 'Analisis Data Penjualan',
            desc: 'Proyek analisis data end-to-end: dari pembersihan data, eksplorasi, hingga menghasilkan insight bisnis yang actionable.',
            tech: ['Python', 'SQL', 'Power BI'],
            points: ['Pipeline ETL sederhana', 'Query SQL kompleks', 'Dashboard Power BI']
        },
        7: {
            icon: '📦',
            title: 'Sistem Inventaris Barang',
            desc: 'Manajemen inventaris dengan pencatatan stok, dukungan QR code, dan laporan real-time.',
            tech: ['Laravel', 'MySQL', 'AJAX'],
            points: ['Pencatatan stok masuk/keluar', 'Scan QR code untuk barang', 'Laporan stok real-time']
        },
        8: {
            icon: '💰',
            title: 'Aplikasi Budgeting Cerdas',
            desc: 'Aplikasi pengelolaan anggaran pribadi dengan fitur prediksi pengeluaran dan laporan keuangan otomatis.',
            tech: ['Python', 'SQLite', 'Fintech'],
            points: ['Klasifikasi pengeluaran otomatis', 'Prediksi anggaran bulanan', 'Laporan visual keuangan']
        },
        9: {
            icon: '🔐',
            title: 'Sistem Auth & Enkripsi',
            desc: 'Aplikasi login aman dengan hashing password, enkripsi data, dan proteksi terhadap serangan keamanan umum.',
            tech: ['Node.js', 'Crypto', 'JWT'],
            points: ['Hashing password bcrypt', 'Enkripsi data sensitif', 'Autentikasi JWT']
        },
        10: {
            icon: '🌀',
            title: 'Portofolio Web 3D Interaktif',
            desc: 'Website portofolio dengan Three.js, animasi 3D real-time, dan tema gelap-terang — website yang sedang Anda lihat ini!',
            tech: ['Three.js', 'JavaScript', 'CSS'],
            points: ['Animasi partikel & objek 3D', 'Tema gelap-terang dinamis', 'Efek glassmorphism & neon']
        },
        11: {
            icon: '📉',
            title: 'Dashboard Crypto & Saham Global',
            desc: 'Pantau harga emas, crypto, saham lokal & luar negeri, dan analisis tren pasar secara real-time.',
            tech: ['Python', 'API', 'Web3'],
            points: ['Integrasi API pasar global', 'Grafik tren harga real-time', 'Analisis portofolio']
        },
        12: {
            icon: '⛓️',
            title: 'Dompet Web3 & Kontrak Pintar',
            desc: 'Eksplorasi aplikasi terdesentralisasi (dApp), dompet kripto, dan smart contract di ekosistem Web3.',
            tech: ['Solidity', 'Web3.js', 'dApp'],
            points: ['Smart contract ERC-20', 'Interaksi dengan dompet kripto', 'Deploy dApp sederhana']
        }
    };

    function openModal(id) {
        const data = projectData[id];
        if (!data) return;

        body.innerHTML = `
            <div class="modal-thumb"><svg class="thumb-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 6 6 .5-4.5 4 1.5 6.5L12 16l-6 3L7.5 12.5 3 8.5 9 8z"></path></svg></div>
            <span class="project-tag">Detail Proyek</span>
            <h3>${data.title}</h3>
            <p>${data.desc}</p>
            <div class="project-tech">${data.tech.map((t) => `<span>${t}</span>`).join('')}</div>
            <ul class="modal-points">${data.points.map((p) => `<li>${p}</li>`).join('')}</ul>
        `;
        overlay.classList.add('open');
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        overlay.classList.remove('open');
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }

    // Buka modal saat tombol "Lihat Detail" diklik
    document.querySelectorAll('.project-detail-btn').forEach((btn) => {
        btn.addEventListener('click', () => openModal(btn.dataset.project));
    });

    // Tutup via tombol close, klik overlay, atau tombol ESC
    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', closeModal);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });
}

/* ============================================================
   15. EFEK 3D TILT + SPOTLIGHT KARTU
   ============================================================ */
function initTiltSpotlight() {
    // Hormati prefers-reduced-motion: nonaktifkan efek tilt
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const cards = document.querySelectorAll('[data-tilt]');
    if (!cards.length) return;

    cards.forEach((card) => {
        // Variabel posisi untuk spotlight
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Set posisi spotlight (dipakai CSS .spotlight-card::after)
            card.style.setProperty('--spot-x', `${x}px`);
            card.style.setProperty('--spot-y', `${y}px`);

            // Hitung rotasi tilt (maks ±6 derajat)
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const rotateY = ((e.clientX - centerX) / rect.width) * 12;
            const rotateX = -((e.clientY - centerY) / rect.height) * 12;
            card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
        });

        // Kembalikan posisi saat kursor keluar
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
}

/* ============================================================
   16. TOMBOL MAGNETIC (HERO)
   ============================================================ */
function initMagnetic() {
    // Hormati prefers-reduced-motion: nonaktifkan efek magnetic
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const magnets = document.querySelectorAll('.magnetic');
    if (!magnets.length) return;

    magnets.forEach((el) => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const relX = e.clientX - rect.left - rect.width / 2;
            const relY = e.clientY - rect.top - rect.height / 2;
            el.style.transform = `translate(${relX * 0.3}px, ${relY * 0.3}px)`;
        });

        el.addEventListener('mouseleave', () => {
            el.style.transform = '';
        });
    });
}


/* ============================================================
   17. LIVE CLOCK REAL-TIME
   ============================================================ */
function initLiveClock() {
    const timeEl = document.getElementById('clock-time');
    if (!timeEl) return;

    function update() {
        const now = new Date();
        const hh = String(now.getHours()).padStart(2, '0');
        const mm = String(now.getMinutes()).padStart(2, '0');
        const ss = String(now.getSeconds()).padStart(2, '0');
        timeEl.textContent = `${hh}:${mm}:${ss}`;
    }
    update();
    setInterval(update, 1000);
}

/* ============================================================
   18. CUSTOM CURSOR (DOT + RING)
   ============================================================ */
function initCustomCursor() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (window.matchMedia('(max-width: 768px)').matches) return;

    const dot = document.getElementById('cursor-dot');
    const ring = document.getElementById('cursor-ring');
    if (!dot || !ring) return;

    let mouseX = -100;
    let mouseY = -100;
    let ringX = mouseX;
    let ringY = mouseY;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        dot.style.left = `${mouseX}px`;
        dot.style.top = `${mouseY}px`;
    });

    // Perbesar ring saat hover elemen interaktif
    document.querySelectorAll('a, button, .nav-link, .btn, [data-tilt], .faq-question').forEach((el) => {
        el.addEventListener('mouseenter', () => ring.classList.add('hovering'));
        el.addEventListener('mouseleave', () => ring.classList.remove('hovering'));
    });

    function move() {
        ringX += (mouseX - ringX) * 0.16;
        ringY += (mouseY - ringY) * 0.16;
        ring.style.left = `${ringX}px`;
        ring.style.top = `${ringY}px`;
        requestAnimationFrame(move);
    }
    move();
}

/* ============================================================
   19. SECTION NAVIGATION DOTS
   ============================================================ */
function initSectionDots() {
    const container = document.getElementById('section-dots');
    if (!container) return;

    const sections = document.querySelectorAll('section[id]');
    const labels = {
        home: 'Beranda',
        tentang: 'Tentang',
        layanan: 'Layanan',
        keahlian: 'Keahlian',
        sertifikasi: 'Sertifikasi',
        blog: 'Blog',
        proyek: 'Proyek',
        testimoni: 'Testimoni',
        pendidikan: 'Pendidikan',
        faq: 'FAQ',
        kontak: 'Kontak'
    };

    sections.forEach((section) => {
        const dot = document.createElement('button');
        dot.className = 'dot';
        dot.dataset.label = labels[section.id] || section.id;
        dot.setAttribute('aria-label', `Ke ${labels[section.id] || section.id}`);
        dot.addEventListener('click', () => {
            section.scrollIntoView({ behavior: 'smooth' });
        });
        container.appendChild(dot);
    });

    const dots = container.querySelectorAll('.dot');
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    dots.forEach((d) => d.classList.remove('active'));
                    const idx = Array.from(sections).indexOf(entry.target);
                    if (dots[idx]) dots[idx].classList.add('active');
                }
            });
        },
        { threshold: 0.4 }
    );
    sections.forEach((s) => observer.observe(s));
}

/* ============================================================
   20. SCROLL PERCENTAGE
   ============================================================ */
function initScrollPercent() {
    const el = document.getElementById('scroll-percent');
    if (!el) return;

    const update = () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const percent = docHeight > 0 ? Math.round((scrollTop / docHeight) * 100) : 0;
        el.textContent = `${percent}%`;
        el.style.setProperty('--percent', `${percent}%`);
        el.classList.toggle('show', window.scrollY > 300);
    };

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
}

/* ============================================================
   21. TOAST NOTIFICATION
   ============================================================ */
function initToast() {
    window.showToast = (message, type = 'info') => {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const icons = { success: '✅', error: '⚠️', info: 'ℹ️' };
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.innerHTML = `<span class="toast-icon">${icons[type] || 'ℹ️'}</span><span>${message}</span>`;
        container.appendChild(toast);

        requestAnimationFrame(() => toast.classList.add('show'));

        setTimeout(() => {
            toast.classList.add('hide');
            setTimeout(() => toast.remove(), 400);
        }, 3200);
    };
}

/* ============================================================
   22. FAQ ACCORDION
   ============================================================ */
function initFaqAccordion() {
    const items = document.querySelectorAll('.faq-item');
    if (!items.length) return;

    items.forEach((item) => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        question.addEventListener('click', () => {
            const isOpen = item.classList.contains('open');

            // Tutup semua
            items.forEach((it) => {
                it.classList.remove('open');
                it.querySelector('.faq-answer').style.maxHeight = '0px';
                it.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            });

            // Buka yang diklik bila sebelumnya tertutup
            if (!isOpen) {
                item.classList.add('open');
                answer.style.maxHeight = `${answer.scrollHeight}px`;
                question.setAttribute('aria-expanded', 'true');
            }
        });
    });
}

/* ============================================================
   23. TESTIMONIAL CAROUSEL
   ============================================================ */
function initTestimonialCarousel() {
    const track = document.getElementById('testimonial-track');
    const dotsWrap = document.getElementById('testimonial-dots');
    const prevBtn = document.getElementById('testimonial-prev');
    const nextBtn = document.getElementById('testimonial-next');
    if (!track) return;

    const slides = track.querySelectorAll('.testimonial-slide');
    const total = slides.length;
    let current = 0;
    let autoTimer;

    // Buat dots
    slides.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.className = 't-dot';
        dot.setAttribute('aria-label', `Testimoni ${i + 1}`);
        dot.addEventListener('click', () => goTo(i));
        dotsWrap.appendChild(dot);
    });
    const dots = dotsWrap.querySelectorAll('.t-dot');

    function goTo(index) {
        current = (index + total) % total;
        track.style.transform = `translateX(-${current * 100}%)`;
        dots.forEach((d, i) => d.classList.toggle('active', i === current));
    }

    function next() { goTo(current + 1); }
    function prev() { goTo(current - 1); }

    nextBtn.addEventListener('click', () => { next(); resetAuto(); });
    prevBtn.addEventListener('click', () => { prev(); resetAuto(); });

    function resetAuto() {
        clearInterval(autoTimer);
        autoTimer = setInterval(next, 5000);
    }

    // Hentikan auto saat hover
    const carousel = document.getElementById('testimonial-carousel');
    carousel.addEventListener('mouseenter', () => clearInterval(autoTimer));
    carousel.addEventListener('mouseleave', resetAuto);

    // Navigasi keyboard (aksesibilitas): panah kiri/kanan
    carousel.setAttribute('tabindex', '0');
    carousel.setAttribute('aria-label', 'Carousel testimoni. Gunakan panah kiri dan kanan untuk berpindah.');
    carousel.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') { next(); resetAuto(); }
        if (e.key === 'ArrowLeft') { prev(); resetAuto(); }
    });

    // Inisialisasi
    goTo(0);
    resetAuto();
}

/* ============================================================
   24. REVEAL KHUSUS KARTU BLOG
   ============================================================ */
function initBlogReveal() {
    const cards = document.querySelectorAll('.blog-card');
    if (!cards.length) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    // Tambah delay berjenjang agar kartu muncul satu per satu
                    const idx = Array.from(cards).indexOf(entry.target);
                    entry.target.style.transitionDelay = `${Math.min(idx, 5) * 0.12}s`;
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.2 }
    );
    cards.forEach((card) => observer.observe(card));
}

/* ============================================================
   24b. MODAL DETAIL BLOG / ARTIKEL
   ============================================================ */
function initBlogModal() {
    const overlay = document.getElementById('blog-modal-overlay');
    const modal = document.getElementById('blog-modal');
    const body = document.getElementById('blog-modal-body');
    const closeBtn = modal ? modal.querySelector('.modal-close') : null;
    if (!overlay || !modal || !body || !closeBtn) return;

    // Konten lengkap 3 artikel
    const blogData = {
        1: {
            emoji: '🤖',
            cat: 'Teknologi',
            title: 'Mengenal Kecerdasan Buatan di Era Modern',
            date: '📅 Jan 2025',
            time: '⏱ 5 mnt',
            excerpt: 'Bagaimana AI mengubah cara kita bekerja, belajar, dan mengambil keputusan di berbagai bidang.',
            intro: 'Kecerdasan Buatan (AI) bukan lagi teknologi masa depan — ia sudah hadir di sekitar kita: dari asisten virtual, rekomendasi konten, hingga mobil otonom. Artikel ini mengajak Anda memahami apa itu AI dan bagaimana dampaknya terhadap kehidupan sehari-hari.',
            sections: [
                {
                    title: 'Apa Itu AI?',
                    points: [
                        'AI adalah simulasi kecerdasan manusia oleh mesin: belajar dari data (machine learning), memahami bahasa (NLP), hingga mengenali gambar (computer vision).',
                        'Tiga jenis utama: Narrow AI (satu tugas, misal chatbot), General AI (setara manusia, masih riset), dan Super AI (melampaui manusia, masih konsep).'
                    ]
                },
                {
                    title: 'AI di Kehidupan Sehari-hari',
                    points: [
                        'Rekomendasi film/lagu di platform streaming menggunakan algoritma AI yang mempelajari preferensi Anda.',
                        'Asisten virtual (Siri, Google Assistant) memakai NLP untuk memahami perintah suara.',
                        'Di dunia kerja, AI membantu otomasi tugas repetitif, analisis data besar, dan pengambilan keputusan yang lebih cepat.'
                    ]
                },
                {
                    title: 'Peluang & Tantangan',
                    points: [
                        'Peluang: efisiensi bisnis, diagnosis medis lebih akurat, pendidikan personal, dan inovasi di hampir semua industri.',
                        'Tantangan: privasi data, bias algoritma, keamanan siber, dan etika penggunaan AI.',
                        'Kuncinya: manusia yang memahami AI akan lebih unggul dibandingkan yang mengabaikannya.'
                    ]
                }
            ],
            closing: 'AI adalah alat — bukan pengganti manusia. Memahaminya sejak dini akan membuka peluang besar di era digital ini.'
        },
        2: {
            emoji: '🪙',
            cat: 'Finance',
            title: 'Panduan Investasi Emas & Saham untuk Pemula',
            date: '📅 Feb 2025',
            time: '⏱ 7 mnt',
            excerpt: 'Langkah awal membangun portofolio investasi: emas, saham lokal, hingga saham luar negeri.',
            intro: 'Memulai investasi bisa terasa menakutkan, tetapi dengan pemahaman dasar yang benar, siapa pun bisa membangun portofolio yang sehat. Berikut panduan praktis untuk pemula yang ingin mulai dari emas dan saham.',
            sections: [
                {
                    title: 'Kenapa Mulai dari Emas?',
                    points: [
                        'Emas adalah aset lindung nilai (hedge) terhadap inflasi dan gejolak ekonomi — nilainya cenderung stabil jangka panjang.',
                        'Mudah dicairkan: bisa dibeli dalam bentuk fisik (batangan, perhiasan) atau digital (tabungan emas, ETF emas).',
                        'Cocok untuk pemula karena risikonya lebih rendah dibandingkan instrumen lain.'
                    ]
                },
                {
                    title: 'Dasar Investasi Saham',
                    points: [
                        'Saham berarti memiliki sebagian kecil perusahaan — keuntungan dari kenaikan harga (capital gain) dan dividen.',
                        'Pelajari fundamental: laporan keuangan, prospek bisnis, dan valuasi sebelum membeli.',
                        'Mulai dari perusahaan besar yang stabil (blue chip) sambil belajar membaca pergerakan pasar.'
                    ]
                },
                {
                    title: 'Saham Lokal vs Luar Negeri',
                    points: [
                        'Saham lokal (misal IDX) lebih mudah dipantau dan tanpa kendala kurs, cocok untuk langkah pertama.',
                        'Saham luar negeri (misal US market) membuka akses ke perusahaan global dan diversifikasi mata uang.',
                        'Gunakan platform legal & berizin, dan alokasikan dana secara proporsional (jangan semua di satu instrumen).'
                    ]
                },
                {
                    title: 'Tips untuk Pemula',
                    points: [
                        'Mulai kecil dan rutin (investasi berkala/DCA) — konsistensi lebih penting daripada nominal besar.',
                        'Diversifikasi: jangan menaruh semua telur di satu keranjang.',
                        'Punya tujuan jelas & jangka waktu, serta siapkan dana darurat terpisah sebelum investasi.'
                    ]
                }
            ],
            closing: 'Investasi bukan tentang menjadi kaya secepat kilat, melainkan membangun kekayaan secara bertahap dengan disiplin dan ilmu.'
        },
        3: {
            emoji: '🔗',
            cat: 'Web3',
            title: 'Web3 & Web4: Masa Depan Internet Terdesentralisasi',
            date: '📅 Mar 2025',
            time: '⏱ 6 mnt',
            excerpt: 'Eksplorasi blockchain, smart contract, dApp, dan bagaimana Web4 membawa internet ke level berikutnya.',
            intro: 'Internet telah berevolusi: Web1 (statis, hanya baca), Web2 (interaktif & terpusat), dan kini Web3 (terdesentralisasi). Di depan mata, Web4 mulai menghadirkan internet yang lebih cerdas dan terhubung dengan dunia fisik.',
            sections: [
                {
                    title: 'Memahami Web3',
                    points: [
                        'Web3 adalah internet berbasis blockchain — data dimiliki pengguna, bukan korporasi raksasa.',
                        'Komponen utamanya: smart contract (kontrak pintar), dApp (aplikasi terdesentralisasi), dan dompet kripto (wallet).',
                        'Pengguna mengontrol identitas & aset digitalnya sendiri tanpa perantara.'
                    ]
                },
                {
                    title: 'Teknologi Kunci: Blockchain & Smart Contract',
                    points: [
                        'Blockchain adalah buku besar digital yang transparan, aman, dan tidak bisa diubah (immutable).',
                        'Smart contract menjalankan perjanjian otomatis saat kondisi terpenuhi — misalnya escrow, voting, atau royalty otomatis.',
                        'Ethereum adalah salah satu ekosistem terbesar untuk membangun dApp dengan bahasa Solidity.'
                    ]
                },
                {
                    title: 'Apa Itu Web4?',
                    points: [
                        'Web4 digambarkan sebagai internet simbiotik: AI, IoT, blockchain, dan interaksi manusia-mesin berpadu.',
                        'Fokus pada kecerdasan (AI-driven), konektivitas penuh antar perangkat, dan integrasi dunia fisik-digital.',
                        'Potensinya: asisten yang benar-benar personal, ekonomi token yang terintegrasi, dan akses internet yang lebih demokratis.'
                    ]
                },
                {
                    title: 'Cara Mulai Belajar',
                    points: [
                        'Buat dompet kripto non-custodial (misal MetaMask) dan coba transaksi di testnet terlebih dahulu.',
                        'Pelajari dasar Solidity & deploy smart contract sederhana di jaringan uji.',
                        'Ikuti komunitas Web3 dan baca dokumentasi resmi — ekosistem ini berkembang sangat cepat.'
                    ]
                }
            ],
            closing: 'Web3 dan Web4 sedang dibangun hari ini. Mereka yang memahami teknologinya sejak awal akan menjadi pemimpin di era internet berikutnya.'
        },
        4: {
            emoji: '📊',
            cat: 'Data Science',
            title: 'Belajar Python untuk Data Science dari Nol',
            date: '📅 Apr 2025',
            time: '⏱ 8 mnt',
            excerpt: 'Panduan langkah demi langkah menguasai Python untuk analisis data, visualisasi, dan machine learning.',
            intro: 'Python adalah bahasa paling populer untuk data science karena sintaksnya sederhana dan ekosistem librarinya lengkap. Artikel ini memandu Anda memulai perjalanan data science menggunakan Python dari nol.',
            sections: [
                {
                    title: 'Kenapa Python untuk Data Science?',
                    points: [
                        'Sintaks sederhana dan mudah dibaca — cocok untuk pemula tanpa latar belakang programming.',
                        'Ekosistem lengkap: NumPy & Pandas untuk manipulasi data, Matplotlib & Seaborn untuk visualisasi, Scikit-learn untuk machine learning.',
                        'Komunitas besar dan dokumentasi melimpah, sehingga mudah mencari solusi saat buntu.'
                    ]
                },
                {
                    title: 'Roadmap Belajar',
                    points: [
                        'Kuasai dasar Python: variabel, loop, fungsi, dan struktur data (list, dict, set).',
                        'Lanjut ke Pandas: membaca CSV/Excel, filtering, grouping, dan data cleaning.',
                        'Belajar visualisasi dengan Matplotlib & Seaborn untuk menyajikan insight secara menarik.',
                        'Tingkatkan ke Scikit-learn untuk membangun model machine learning sederhana (regresi & klasifikasi).'
                    ]
                },
                {
                    title: 'Proyek Praktis untuk Pemula',
                    points: [
                        'Analisis data penjualan: cari produk terlaris, tren bulanan, dan segmentasi pelanggan.',
                        'Visualisasi data COVID atau cuaca dengan dataset publik dari Kaggle.',
                        'Prediksi harga rumah atau klasifikasi spam menggunakan model machine learning sederhana.'
                    ]
                }
            ],
            closing: 'Kunci sukses data science adalah praktik konsisten. Mulai dari dataset kecil, bangun portofolio, dan terus belajar setiap hari.'
        },
        5: {
            emoji: '🎨',
            cat: 'UI/UX',
            title: 'Tips Desain UI/UX yang Bikin Pengguna Betah',
            date: '📅 Mei 2025',
            time: '⏱ 6 mnt',
            excerpt: 'Prinsip desain antarmuka yang intuitif, estetis, dan membuat pengalaman pengguna terasa menyenangkan.',
            intro: 'Desain yang baik tidak hanya indah dipandang, tetapi juga mudah digunakan. Artikel ini membahas prinsip UI/UX yang membuat pengguna betah dan kembali lagi ke produk Anda.',
            sections: [
                {
                    title: 'Prinsip Dasar UX',
                    points: [
                        'Kenali pengguna: riset kebutuhan, pain point, dan kebiasaan mereka sebelum mendesain.',
                        'Konsistensi: gunakan pola, warna, dan typography yang seragam di seluruh halaman.',
                        'Sederhanakan alur: kurangi jumlah langkah agar pengguna mencapai tujuan dengan cepat.'
                    ]
                },
                {
                    title: 'Prinsip Dasar UI',
                    points: [
                        'Hierarki visual: ukuran, warna, dan kontras mengarahkan mata ke elemen terpenting.',
                        'Spacing & whitespace yang cukup membuat antarmuka terasa lega dan mudah dipindai.',
                        'Gunakan grid & alignment yang rapi untuk menciptakan kesan profesional.'
                    ]
                },
                {
                    title: 'Tips Praktis yang Langsung Bisa Dicoba',
                    points: [
                        'Buat sistem desain (design tokens): warna, tipografi, spacing agar konsisten.',
                        'Uji dengan pengguna nyata (usability testing) meski hanya 5 orang — cukup untuk menemukan masalah besar.',
                        'Perhatikan accessibility: kontras teks, ukuran target klik, dan dukungan screen reader.'
                    ]
                }
            ],
            closing: 'Desain terbaik adalah yang tidak disadari pengguna — semuanya terasa natural, mudah, dan menyenangkan.'
        },
        6: {
            emoji: '💼',
            cat: 'Karir',
            title: 'Kiat Sukses Jadi Web Developer Profesional',
            date: '📅 Jun 2025',
            time: '⏱ 7 mnt',
            excerpt: 'Jalur karier, skill wajib, portofolio, dan strategi mendapatkan klien atau pekerjaan impian sebagai developer.',
            intro: 'Menjadi web developer profesional bukan hanya soal bisa coding, tetapi juga membangun portofolio, personal branding, dan jaringan. Berikut peta jalan menuju karier yang sukses.',
            sections: [
                {
                    title: 'Skill Wajib Web Developer',
                    points: [
                        'Frontend: HTML, CSS, JavaScript, dan framework modern seperti React atau Vue.',
                        'Backend: Node.js, Python (Django/Flask), atau PHP (Laravel) untuk membangun API & logika server.',
                        'Database: SQL (PostgreSQL, MySQL) dan NoSQL (MongoDB) untuk pengelolaan data.',
                        'Tooling: Git/GitHub, terminal, dan deployment (Vercel, Netlify, atau cloud server).'
                    ]
                },
                {
                    title: 'Membangun Portofolio yang Menarik',
                    points: [
                        'Buat 3–5 proyek nyata yang memecahkan masalah, bukan sekadar tutorial copy-paste.',
                        'Tulis studi kasus singkat: masalah, solusi, teknologi, dan hasil yang dicapai.',
                        'Deploy semua proyek dan tautkan di GitHub, portfolio pribadi, dan LinkedIn.'
                    ]
                },
                {
                    title: 'Strategi Mendapatkan Klien atau Pekerjaan',
                    points: [
                        'Aktif di komunitas: GitHub, LinkedIn, dan forum developer untuk membangun kredibilitas.',
                        'Mulai dari proyek kecil di platform freelance, lalu minta testimoni dari klien pertama.',
                        'Terus update skill sesuai tren industri — web3, AI, dan performa adalah nilai jual tambahan.'
                    ]
                }
            ],
            closing: 'Karier developer dibangun dari kombinasi skill teknis, portofolio yang kuat, dan konsistensi belajar sepanjang hayat.'
        }
    };

    function openBlog(id) {
        const data = blogData[id];
        if (!data) return;

        const sectionsHtml = data.sections.map((s) => `
            <h4>${s.title}</h4>
            <ul>${s.points.map((p) => `<li>${p}</li>`).join('')}</ul>
        `).join('');

        body.innerHTML = `
            <div class="blog-modal-thumb"><span class="blog-emoji">${data.emoji}</span></div>
            <span class="blog-cat">${data.cat}</span>
            <h3>${data.title}</h3>
            <div class="blog-meta"><span>${data.date}</span><span>${data.time}</span></div>
            <p><em>${data.excerpt}</em></p>
            <p>${data.intro}</p>
            ${sectionsHtml}
            <p><strong>${data.closing}</strong></p>
            <p class="blog-modal-close-note">Tekan ESC atau klik ✕ untuk menutup.</p>
        `;

        overlay.classList.add('open');
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeBlog() {
        overlay.classList.remove('open');
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }

    // Klik tombol "Baca Selengkapnya"
    document.querySelectorAll('.blog-detail-btn').forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            openBlog(btn.dataset.blog);
        });
    });

    // Klik seluruh kartu blog (selain tombol) juga membuka modal
    document.querySelectorAll('.blog-card[data-blog]').forEach((card) => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('.blog-detail-btn')) return;
            openBlog(card.dataset.blog);
        });
    });

    // Tutup via tombol close, klik overlay, atau ESC
    closeBtn.addEventListener('click', closeBlog);
    overlay.addEventListener('click', closeBlog);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeBlog();
    });
}

/* ============================================================
   25. PARTICLE BURST SAAT KLIK
   ============================================================ */
function initClickBurst() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const colors = ['#00f0ff', '#ff2ec4', '#8b5cf6', '#00ffa3', '#7df9ff'];

    document.addEventListener('click', (e) => {
        // Jangan aktif saat mengklik tombol/aksi penting
        if (e.target.closest('button, a, .faq-question, .project-detail-btn, .theme-toggle, .hamburger')) return;

        const count = 12;
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('span');
            particle.className = 'burst-particle';
            particle.style.left = `${e.clientX + window.scrollX}px`;
            particle.style.top = `${e.clientY + window.scrollY}px`;
            particle.style.background = colors[Math.floor(Math.random() * colors.length)];

            const angle = (Math.PI * 2 * i) / count;
            const dist = 40 + Math.random() * 50;
            const dx = Math.cos(angle) * dist;
            const dy = Math.sin(angle) * dist;
            particle.style.setProperty('--dx', `${dx}px`);
            particle.style.setProperty('--dy', `${dy}px`);
            particle.style.setProperty('--size', `${3 + Math.random() * 5}px`);

            document.body.appendChild(particle);
            setTimeout(() => particle.remove(), 700);
        }
    });
}

