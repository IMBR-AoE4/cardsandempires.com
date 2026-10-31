// Picks the page language from the browser's languages, only on the main page (/).
// A language chosen in the selector is remembered and always wins over the browser.
(function () {
    var paths = { en: '/', 'pt-br': '/pt-br/', es: '/es/', fr: '/fr/', de: '/de/', ru: '/ru/' };
    var key = 'ce-language';

    function remembered() {
        try { return window.localStorage.getItem(key); } catch (error) { return null; }
    }

    function remember(language) {
        try { window.localStorage.setItem(key, language); } catch (error) { /* private mode: the choice is just not kept */ }
    }

    function fromBrowser() {
        var languages = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
        for (var i = 0; i < languages.length; i++) {
            var tag = String(languages[i]).toLowerCase();
            var base = tag.split('-')[0];
            if (base === 'pt') return 'pt-br';
            if (paths[base]) return base;
        }
        return null;
    }

    if (window.location.pathname === '/') {
        var language = remembered() || fromBrowser();
        if (language && paths[language] && paths[language] !== '/') {
            window.location.replace(paths[language] + window.location.search + window.location.hash);
        }
    }

    // Choosing a language in the selector stores it, so the main page stops redirecting.
    document.addEventListener('click', function (event) {
        var link = event.target.closest ? event.target.closest('.languages a[hreflang]') : null;
        if (link) remember(link.getAttribute('hreflang').toLowerCase());
    });
})();
