## **1. Legalità dello scraping secondo il CFAA**

- **Sentenza del Ninth Circuit (2022):** La Corte d'Appello degli Stati Uniti ha stabilito che lo scraping di dati pubblicamente accessibili non viola il **Computer Fraud and Abuse Act (CFAA)**[4](https://techcrunch.com/2022/04/18/web-scraping-legal-court/)[7](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/). Questo protegge attività di scraping a fini accademici, di ricerca o giornalistici.
    
- **Limiti:** Goodreads potrebbe comunque perseguire azioni legali se lo scraping:
    
    - **Danneggia il servizio** (es. sovraccarico dei server)[3](https://www.goodreads.com/topic/show/22205547-is-it-legal-to-scrape-goodreads).
        
    - **Violi i termini di servizio** (vedi punto 2)[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
        

## **2. Violazione dei termini di servizio di Goodreads**

I termini di Goodreads vietano esplicitamente:

- **Copia non autorizzata** di contenuti ("Except as explicitly provided herein, nothing in this Agreement shall be deemed to create a license [...] you agree not to [...] copy [...] any materials or content accessible on the Service")[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
    
- **Scraping automatizzato** senza consenso[3](https://www.goodreads.com/topic/show/22205547-is-it-legal-to-scrape-goodreads).
    

Il progetto GitHub, **non utilizzando l'API ufficiale** (deprecata o meno[3](https://www.goodreads.com/topic/show/22205547-is-it-legal-to-scrape-goodreads)) e basandosi su scraping diretto, viola questi termini, esponendosi a potenziali azioni civili da parte di Goodreads[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads)[7](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/).

## **3. Diritto d'autore sulle recensioni**

- **Copyright degli utenti:** Le recensioni su Goodreads sono proprietà intellettuale degli autori[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads). Utilizzarle senza autorizzazione (anche citando la fonte) potrebbe configurare violazione, a meno che non rientri nel **fair use** (es. scopi educativi o critica)[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
    
- **Rischi specifici:** Il progetto include dati come "User_Name Posted on Goodreads" e "Review Here", ma senza un'analisi caso per caso del fair use, questa pratica è rischiosa[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
    

## **4. Casi giuridici rilevanti**

- **hiQ v. LinkedIn (2019):** Ha stabilito che lo scraping di dati pubblici non viola il CFAA, purché non si aggirino barriere tecniche (es. login)[5](https://www.scrapeless.com/en/blog/is-web-scraping-legal)[7](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/).
    
- **Craigslist v. 3Taps (2013):** Ha condannato lo scraping dopo revoca esplicita del consenso[5](https://www.scrapeless.com/en/blog/is-web-scraping-legal), un precedente che Goodreads potrebbe invocare se inviasse un cease-and-desist.
    

## **5. Possibili conseguenze per il progetto**

- **Azioni legali da Goodreads:** Richiesta di rimozione del repository (DMCA), causa per violazione dei termini o diritto d'autore.
    
- **Responsabilità degli sviluppatori:** Multe o risarcimenti in caso di utilizzo commerciale dei dati[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads)[7](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/).
    

## **Raccomandazioni per un approccio legale**

1. **Utilizzare l'API ufficiale** (se disponibile) o richiedere autorizzazione scritta.
    
2. **Limitare lo scraping a dati non protetti da copyright** (es. titoli di libri, senza recensioni).
    
3. **Rispettare robots.txt** (sebbene non sia vincolante legalmente, è una buona pratica)[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
    
4. **Valutare il fair use** per eventuali dati estratti, documentando scopi non commerciali[6](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads).
    

In sintesi, **il progetto viola i termini di servizio di Goodreads e rischia di infringere il diritto d'autore sulle recensioni**, nonostante lo scraping di dati pubblici non sia di per sé illegale nel quadro del CFAA[4](https://techcrunch.com/2022/04/18/web-scraping-legal-court/)[7](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/). La legittimità dipende dall'uso specifico dei dati e dalla risposta di Goodreads.

### Citations:

1. [https://github.com/scostap/goodreads_bbe_dataset/tree/main](https://github.com/scostap/goodreads_bbe_dataset/tree/main)
2. [https://www.goodreads.com/list/show/1.Best_Books_Ever](https://www.goodreads.com/list/show/1.Best_Books_Ever)
3. [https://www.goodreads.com/topic/show/22205547-is-it-legal-to-scrape-goodreads](https://www.goodreads.com/topic/show/22205547-is-it-legal-to-scrape-goodreads)
4. [https://techcrunch.com/2022/04/18/web-scraping-legal-court/](https://techcrunch.com/2022/04/18/web-scraping-legal-court/)
5. [https://www.scrapeless.com/en/blog/is-web-scraping-legal](https://www.scrapeless.com/en/blog/is-web-scraping-legal)
6. [https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads](https://law.stackexchange.com/questions/88798/what-is-the-legality-of-webscraping-reviews-from-goodreads)
7. [https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/](https://www.jdsupra.com/legalnews/web-scraping-watch-cases-set-to-clarify-9249962/)
8. [https://github.com/topics/goodreads-data](https://github.com/topics/goodreads-data)
9. [https://www.reddit.com/r/webdev/comments/1340s6t/is_web_scraping_user_generated_content_for/](https://www.reddit.com/r/webdev/comments/1340s6t/is_web_scraping_user_generated_content_for/)
10. [https://www.reddit.com/r/webscraping/comments/18qt4q5/goodreads_webscraping_and_tos/](https://www.reddit.com/r/webscraping/comments/18qt4q5/goodreads_webscraping_and_tos/)
11. [https://brightdata.com/products/web-scraper/goodreads](https://brightdata.com/products/web-scraper/goodreads)
12. [https://www.goodreads.com/api/documentation](https://www.goodreads.com/api/documentation)
13. [https://www.kaggle.com/code/rohinikrishnamoorthy/goodreads-webscraping-using-beautifulsoup](https://www.kaggle.com/code/rohinikrishnamoorthy/goodreads-webscraping-using-beautifulsoup)
14. [https://blog.apify.com/is-web-scraping-legal/](https://blog.apify.com/is-web-scraping-legal/)
15. [https://www.goodreads.com/topic/show/314647-api-terms-of-service](https://www.goodreads.com/topic/show/314647-api-terms-of-service)
16. [https://www.actowizsolutions.com/goodreads-social-media-data-scraping.php](https://www.actowizsolutions.com/goodreads-social-media-data-scraping.php)
17. [https://www.goodreads.com/topic/show/478016-api-terms-of-service-question](https://www.goodreads.com/topic/show/478016-api-terms-of-service-question)
18. [https://www.octoparse.com/blog/how-to-scrape-goodreads-for-book-data](https://www.octoparse.com/blog/how-to-scrape-goodreads-for-book-data)
19. [https://www.iubenda.com/en/help/111092-is-web-scraping-legal-what-you-need-to-know](https://www.iubenda.com/en/help/111092-is-web-scraping-legal-what-you-need-to-know)
20. [https://www.neudata.co/blog/web-scraping-and-copyright-law](https://www.neudata.co/blog/web-scraping-and-copyright-law)
21. [https://crawlbase.com/blog/scrape-goodreads-ratings-and-comments/](https://crawlbase.com/blog/scrape-goodreads-ratings-and-comments/)
22. [https://www.internetandtechnologylaw.com/automated-web-scraping-public-sites-legal/](https://www.internetandtechnologylaw.com/automated-web-scraping-public-sites-legal/)
23. [https://www.reddit.com/r/learnpython/comments/1fknl27/so_close_to_getting_my_code_to_work_goodreads/](https://www.reddit.com/r/learnpython/comments/1fknl27/so_close_to_getting_my_code_to_work_goodreads/)
24. [https://www.skadden.com/-/media/files/publications/2014/01/070071319-skadden.pdf](https://www.skadden.com/-/media/files/publications/2014/01/070071319-skadden.pdf)
25. [https://stackoverflow.com/questions/52794154/blocked-while-scraping-goodreads-com](https://stackoverflow.com/questions/52794154/blocked-while-scraping-goodreads-com)
26. [https://www.troutman.com/insights/ninth-circuit-provides-guidance-on-web-scraping.html](https://www.troutman.com/insights/ninth-circuit-provides-guidance-on-web-scraping.html)
27. [https://github.com/maria-antoniak/goodreads-scraper](https://github.com/maria-antoniak/goodreads-scraper)
28. [https://www.morganlewis.com/blogs/sourcingatmorganlewis/2022/04/data-scraping-deemed-legal-in-certain-circumstances](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2022/04/data-scraping-deemed-legal-in-certain-circumstances)
29. [https://copyrightblog.kluweriplaw.com/2023/10/03/generative-ai-the-us-class-action-against-google-bard-and-other-ai-tools-for-web-scraping/](https://copyrightblog.kluweriplaw.com/2023/10/03/generative-ai-the-us-class-action-against-google-bard-and-other-ai-tools-for-web-scraping/)
30. [https://automatio.ai/templates/en/good-reads-page-info-scraping-data](https://automatio.ai/templates/en/good-reads-page-info-scraping-data)
31. [https://www.goodreads.com/about/terms](https://www.goodreads.com/about/terms)
32. [https://www.blog.datahut.co/post/is-web-data-scraping-legal](https://www.blog.datahut.co/post/is-web-data-scraping-legal)
33. [https://www.goodreads.com/topic/show/18513705-storing-goodreads-data](https://www.goodreads.com/topic/show/18513705-storing-goodreads-data)
34. [https://www.freeprivacypolicy.com/blog/web-scraping-legal/](https://www.freeprivacypolicy.com/blog/web-scraping-legal/)
35. [https://rollout.com/integration-guides/goodreads/api-essentials](https://rollout.com/integration-guides/goodreads/api-essentials)
36. [https://github.com/havanagrawal/GoodreadsScraper](https://github.com/havanagrawal/GoodreadsScraper)