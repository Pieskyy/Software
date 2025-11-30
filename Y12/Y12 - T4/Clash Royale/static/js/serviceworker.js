const CACHE_NAME = 'clash-royale-pwa-v6';

const APP_SHELL = [
  '/',
  '/static/css/styles.css',
  '/static/css/home.css', 
  '/static/css/navigation.css',
  '/static/js/script.js',
  '/static/js/app.js',
  '/static/js/accessibility.js',
  '/static/icons/crown.png',
  '/static/icons/Experience icon.png',
  '/static/icons/gold.png',
  '/static/icons/gem.png',
  '/static/icons/settings.png',
  '/static/images/battlebanner.png',
  '/static/images/arena.png',
  '/static/images/battlebutton.png',
  '/static/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.add(OFFLINE_URL).then(() => cache.addAll(APP_SHELL)))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    Promise.all([
      self.clients.claim(),
      caches.keys().then(cacheNames => 
        Promise.all(
          cacheNames.map(cacheName => 
            cacheName !== CACHE_NAME ? caches.delete(cacheName) : null
          )
        )
      )
    ])
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
          return response;
        })
        .catch(async () => {
          const cachedPage = await caches.match(event.request);
          return cachedPage || caches.match(OFFLINE_URL);
        })
    );
    return;
  }
  
  event.respondWith(
    caches.match(event.request)
      .then(cachedResponse => {
        if (cachedResponse) return cachedResponse;
        
        return fetch(event.request)
          .then(response => {
            if (response && response.status === 200) {
              const responseClone = response.clone();
              caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
            }
            return response;
          })
          .catch(() => new Response('Network error', {
            status: 408,
            headers: { 'Content-Type': 'text/plain' },
          }));
      })
  );
});