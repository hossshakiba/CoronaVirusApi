# CoronaVirusApi
A -django-rest-framework based- API for Covid-19. **World-wide** statistics including fields below :<br>
- Country
- Total Cases
- New Cases
- Total Deaths
- Nww Deaths
- Total Recovered
- Active Cases
- Total Tests
- Population
- Continent

Information based on https://www.worldmeters.com, get updated every minute.

# List-view
If you want to get all the *json-formatted* information of the whole world and all other 220 countries, the url would be ``http://127.0.0.1:8000/api`` on your **localhost**.

# A specific country?
If you want to retrieve information of a desired country, you just need to get to this url format : ``http://127.0.0.1:8000/api/{country}``. e.g. ``http://127.0.0.1:8000/api/iran``.


