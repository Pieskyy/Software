const CACHE_NAME = 'my-site-cache-v1';

const STATIC_ASSETS = [
  '/index.html',
  '/about.html',
  '/blogs.html',
  '/card_detail.html',
  '/contact.html',
  '/decks.html',
  '/nav.html',
  '/blogs.css',
  '/card_details.css',
  '/home.css',
  '/navigation.css',
  '/searching.css',
  '/styles.css',
  '/accessibility.js',
  '/blogs.js',
  '/script.js',
  '/search.js',
  '/serviceworker.js',
  '/offline.html'
];


self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
});


self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});


self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      if (cachedResponse) return cachedResponse;

      return fetch(event.request).then(response => {
        if (event.request.method === 'GET' && event.request.url.startsWith(self.location.origin)) {
          return caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, response.clone());
            return response;
          });
        } else {
          return response;
        }
      }).catch(() => {
        if (event.request.destination === 'document') {
          return caches.match('/offline.html');
        }
      });
    })
  );
});
