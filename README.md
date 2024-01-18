# Projekta uzdevums:

Galvenais projekta uzdevums - automatizēt ikdienisķo uzdevumu. Lai to panāktu, bija nepieciešams izstrādāt programmatūru Python valodā.
Kā automatizējamais uzdevums tika izvēlēta ēdienu recepšu vākšana. To sasniedšanai vajadzēja izpētīt tīmekļa skrāpēšanas metodi Python valodā. 
Pētīšana iekļāva: iepazīšanās ar tīmekļa vietnes struktūru, saistīto Python bibliotēku pielietošanas metode, loģisko ķēžu izstrādāšana.

# Lietota Python bibliotēka:

bs4 - BeautifulSoup4 - bibliotēka, kas atļāva iegūt informāciju no tīmekļa vietnes. Šī gadījumā - par receptes karti (ēdiena nosaukums, tā sastāvdaļas un pagatavošana).

# Programmatūras izmantošanas metodes:

Izstrādātā programmatūra ir piemērojama visām recepšu kartēm no vietnes "jauns.lv". 
Lai iegūtu vajadzīgo recepti, ir nepieciešams nokopēt tīmekļa vietnes URL programmatūras 25. rindā " recepte_url='*IEVIETOT_URL*' ". 
Rezultātā terminālā tiks izvadīti ēdiena nosaukums, sastāvdaļu saraksts un to apjoms/skaits mērvienībās, pagatavošanas instrukcija.

Izvadīto tekstu ir iespējams mierīgi pārnest jebkurā teksta failā (piem., MC WORD dokumenta fails), izmainīt fonta izmēru un pēc tam izdrukāt.

Piedāvāta druka vietnē var būt nepiemērota lietotājam, jo tā iekļauj daudz krasainu elementu, attēlu un lielu teksta fonta izmēru. 
Tas ir it īpaši nepielietojami stradājot ar lielu recepšu skaitu vai sarežģīto pagatavošanas instrukciju.


*Saraksts ar iespējamām tīmekļa vietnēm programmatūras pārbaudei:*

https://jauns.lv/recepte/deserti/694-cepti-aboli-sarkanvina

https://jauns.lv/recepte/galas-edieni/2999-vista-vina-merce

https://jauns.lv/recepte/deserti/3440-varitais-vanilas-krems
