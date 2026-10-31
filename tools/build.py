"""Builds the coming-soon page in every locale from one template."""
import html, os, sys
root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = [
 ("en", "en", "/", "English", {"t":"Coming soon","lang":"Language","lead":"Collectible cards from historic empires. Every copy is unique, with a serial number, an edition and a record of everyone who has owned it.","p":[("Collection","Gather cards of civilizations, troops, landmarks and buildings."),("Marketplace","Buy, sell and trade copies with other collectors."),("Strategy","Take your cards into a turn-based board game.")],"note":"The platform is in development. Check back soon.","desc":"Cards & Empires: unique collectible cards from historic empires, with a collection, a marketplace and a strategy game. Coming soon."}),
 ("pt-BR", "pt-br", "/pt-br/", "Português (Brasil)", {"t":"Em breve","lang":"Idioma","lead":"Cartas colecionáveis de impérios históricos. Cada exemplar é único, com serial, edição e histórico de quem já o teve.","p":[("Coleção","Reúna cartas de civilizações, tropas, marcos e construções."),("Marketplace","Compre, venda e troque exemplares com outros colecionadores."),("Estratégia","Leve as suas cartas para um jogo de tabuleiro por turnos.")],"note":"A plataforma está em desenvolvimento. Volte em breve.","desc":"Cards & Empires: cartas colecionáveis únicas de impérios históricos, com coleção, marketplace e um jogo de estratégia. Em breve."}),
 ("es", "es", "/es/", "Español", {"t":"Próximamente","lang":"Idioma","lead":"Cartas coleccionables de imperios históricos. Cada ejemplar es único, con número de serie, edición e historial de quienes lo han tenido.","p":[("Colección","Reúne cartas de civilizaciones, tropas, monumentos y edificios."),("Marketplace","Compra, vende e intercambia ejemplares con otros coleccionistas."),("Estrategia","Lleva tus cartas a un juego de tablero por turnos.")],"note":"La plataforma está en desarrollo. Vuelve pronto.","desc":"Cards & Empires: cartas coleccionables únicas de imperios históricos, con colección, marketplace y un juego de estrategia. Próximamente."}),
 ("fr", "fr", "/fr/", "Français", {"t":"Bientôt disponible","lang":"Langue","lead":"Des cartes à collectionner d’empires historiques. Chaque exemplaire est unique, avec un numéro de série, une édition et l’historique de ses propriétaires.","p":[("Collection","Réunissez des cartes de civilisations, de troupes, de monuments et de bâtiments."),("Marketplace","Achetez, vendez et échangez des exemplaires avec d’autres collectionneurs."),("Stratégie","Emmenez vos cartes dans un jeu de plateau au tour par tour.")],"note":"La plateforme est en cours de développement. Revenez bientôt.","desc":"Cards & Empires : des cartes à collectionner uniques d’empires historiques, avec collection, marketplace et jeu de stratégie. Bientôt disponible."}),
 ("de", "de", "/de/", "Deutsch", {"t":"Demnächst","lang":"Sprache","lead":"Sammelkarten historischer Reiche. Jedes Exemplar ist einzigartig, mit Seriennummer, Edition und der Geschichte aller bisherigen Besitzer.","p":[("Sammlung","Sammle Karten von Zivilisationen, Truppen, Wahrzeichen und Gebäuden."),("Marktplatz","Kaufe, verkaufe und tausche Exemplare mit anderen Sammlern."),("Strategie","Nimm deine Karten mit in ein rundenbasiertes Brettspiel.")],"note":"Die Plattform befindet sich in Entwicklung. Schau bald wieder vorbei.","desc":"Cards & Empires: einzigartige Sammelkarten historischer Reiche, mit Sammlung, Marktplatz und Strategiespiel. Demnächst."}),
 ("ru", "ru", "/ru/", "Русский", {"t":"Скоро","lang":"Язык","lead":"Коллекционные карты исторических империй. Каждый экземпляр уникален: у него есть серийный номер, выпуск и история всех владельцев.","p":[("Коллекция","Собирайте карты цивилизаций, войск, памятников и зданий."),("Торговая площадка","Покупайте, продавайте и обменивайте экземпляры с другими коллекционерами."),("Стратегия","Используйте свои карты в пошаговой настольной игре.")],"note":"Платформа в разработке. Загляните позже.","desc":"Cards & Empires: уникальные коллекционные карты исторических империй, с коллекцией, торговой площадкой и стратегической игрой. Скоро."}),
]
e = lambda s: html.escape(s, quote=True)
alternates = "\n".join(f'    <link rel="alternate" hreflang="{code}" href="https://cardsandempires.com{path}">' for code, _, path, _, _ in L)
alternates += '\n    <link rel="alternate" hreflang="x-default" href="https://cardsandempires.com/">'
for code, slug, path, name, t in L:
    switch = "\n".join(
        f'                <li><a href="{p}" hreflang="{c}" lang="{c}"' + (' aria-current="page"' if c == code else '') + f'>{e(n)}</a></li>'
        for c, _, p, n, _ in L)
    pillars = "\n".join(f'                <li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in t["p"])
    page = f'''<!doctype html>
<html lang="{code}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Cards &amp; Empires — {e(t["t"])}</title>
    <meta name="description" content="{e(t["desc"])}">
    <meta name="color-scheme" content="dark light">
    <meta name="theme-color" content="#10213d">
    <meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <link rel="canonical" href="https://cardsandempires.com{path}">
{alternates}
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <div class="backdrop" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
    <main class="landing" aria-labelledby="title">
        <section class="panel">
            <div class="panel-top">
                <picture class="mark">
                    <source srcset="/assets/brand-mark-navy.png" media="(prefers-color-scheme: light)">
                    <img src="/assets/brand-mark-cream.png" alt="" width="72" height="72">
                </picture>
                <nav class="languages" aria-label="{e(t["lang"])}">
                    <ul>
{switch}
                    </ul>
                </nav>
            </div>
            <p class="kicker">{e(t["t"])}</p>
            <h1 id="title">Cards &amp; Empires</h1>
            <p class="lead">{e(t["lead"])}</p>
            <ul class="pillars">
{pillars}
            </ul>
            <p class="note">{e(t["note"])}</p>
        </section>
        <footer class="footer">
            <p>&copy; 2026 Cards &amp; Empires</p>
        </footer>
    </main>
</body>
</html>
'''
    out = os.path.join(root, path.strip("/"), "index.html") if path != "/" else os.path.join(root, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(page)
    print(out)
