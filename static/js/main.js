
/* Smooth scroll for nav links */
document.querySelectorAll('.nav-link').forEach(a=>{
  a.addEventListener('click', (e)=>{
    e.preventDefault();
    const id = a.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
  });
});

/* Theme toggle (persist in localStorage) */
const themeToggle = document.getElementById('theme-toggle');
const root = document.body;
const current = localStorage.getItem('theme') || 'dark';
if(current === 'dark') root.classList.add('dark'); else root.classList.remove('dark');
themeToggle.addEventListener('click', ()=>{
  root.classList.toggle('dark');
  const now = root.classList.contains('dark') ? 'dark' : 'light';
  localStorage.setItem('theme', now);
});

/* Twinkling stars generator */
(function createStars(){
  const stars = document.getElementById('stars');
  const count = 80;
  for(let i=0;i<count;i++){
    const s = document.createElement('div');
    s.className = 'star';
    const x = Math.random()*100;
    const y = Math.random()*100;
    const size = Math.random()*2 + 0.5;
    s.style.position = 'absolute';
    s.style.left = x + '%';
    s.style.top = y + '%';
    s.style.width = size + 'px';
    s.style.height = size + 'px';
    s.style.background = 'white';
    s.style.borderRadius = '50%';
    s.style.opacity = Math.random();
    s.style.filter = 'blur(0.6px)';
    s.style.animation = 'twinkle ' + (2+Math.random()*3) + 's infinite';
    stars.appendChild(s);
  }
  const style = document.createElement('style');
  style.innerHTML = '@keyframes twinkle { 0% {opacity:0.1} 50% {opacity:1} 100% {opacity:0.1} }';
  document.head.appendChild(style);
})();

/* Small entrance animations using GSAP if available */
window.addEventListener('load', ()=>{
  if(window.gsap) {
    gsap.from('.card', {y:20, opacity:0, stagger:0.12, duration:0.6, ease:'power2.out'});
  }
});
