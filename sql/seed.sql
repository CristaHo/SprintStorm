INSERT INTO category ( name, user_id ) VALUES ( 'technology', 1 );

INSERT INTO book ( cite_key, author, title, year, publisher, category_id, user_id ) 
    VALUES ( 'latexcompanion', 'Michel Goossens and Frank Mittelbach and Alexander Samarin', 'The \LaTeX\ Companion', '1993', 'Addison-Wesley', 1, 1 );

INSERT INTO article ( cite_key, author, title, year, journal, volume, pages, category_id, user_id ) 
    VALUES ( 'the_post', 'Tiku Nitasha', 'The Google engineer who thinks the company’s AI has come to life', '2022', 'The Washington Post', '1', '10-23', 1, 1 );

INSERT INTO misc ( cite_key, author, title, year, url, urldate, category_id, user_id )
    VALUES ( 'internet', 'Wikipedia.org', 'Internet', '2023', 'https://en.wikipedia.org/wiki/Internet', '1.10.2023', 1, 1 ), ( 'agile101', 'Agile Alliance', 'Agile 101', '2022', 'https://www.agilealliance.org/agile101/', '16.11.2022', 1, 1 );

--@book{latexcompanion,
--    author    = "Michel Goossens and Frank Mittelbach and Alexander Samarin",
--    title     = "The \LaTeX\ Companion",
--    year      = "1993",
--    publisher = "Addison-Wesley",
--    address   = "Reading, Massachusetts"
--}
--@article{
--    the_post,
--    title = "The Google engineer who thinks the company’s AI has come to life",
--    journal = "{The Washington Post}",
--    author = "{Tiku, Nitasha}",
--    year = {2022},
--    url = "https://www.washingtonpost.com/technology/2022/06/11/google-ai-lamda-blake-lemoine/",
--    note = "[Online; accessed 3-November-2022]"
--}
--
--@misc{Internet,
--author = {wikipedia.org},
--title = {Internet},
--url = {https://en.wikipedia.org/wiki/Internet},
--year = "2023",
--urldate = {1.10.2023}
--}
--
--@article{agile101,
--    title   = "{Agile 101}",
--    author  = "{Agile Alliance}",
--    year    = {2022},
--    note    = "Agile resources",
--    url     = "https://www.agilealliance.org/agile101/",
--    note    = "[online; accessed 16-November-2022]"
--}
--
--@article{fowler,
--    title   = "{The New Methodology}",
--    author  = "Fowler, Martin",
--    year    = {2005},
--    note    = "web blog post",
--    url     = "https://www.martinfowler.com/articles/newMethodology.html",
--    note    = "[Online; accessed 16-November-2022]"
--}
