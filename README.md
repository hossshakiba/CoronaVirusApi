# CoronaVirusApi
🦠 A django-rest-framework based API for Covid-19. **🌏-wide** statistics including fields below :<br>
- Country 🇮🇷
- Total Cases 😷
- New Cases 🆕
- Total Deaths ⚰️
- New Deaths 🆕
- Total Recovered ✅
- Active Cases 🆘
- Total Tests 💉
- Population 🏘️
- Continent 🗺️

Information based on https://www.worldmeters.com, get updated every minute.

# List-view
If you want to get all the *json-formatted* information of the whole world and all other 220 countries, the url would be ``http://127.0.0.1:8000/api`` on your **localhost**.

# A specific country?
If you want to retrieve information of a desired country, you just need to get to this url format : ``http://127.0.0.1:8000/api/{country}``. e.g. ``http://127.0.0.1:8000/api/iran``.

---
**NOTE**

country should be in **lower-case** format and countries with more than 1 part, like Saudi Arabia, will be accessed at ``http://127.0.0.1:8000/api/saudi-arabia``.

---

# Search
Isn't it cool to search among countries and continents ? you can easily search via this url : ``http://127.0.0.1:8000/api/?q=rus``. In the latter example, it will return a list of information consists of countries or continents containing ``rus``.

# Ordering
You are able to order the data both Asc and Desc based on **Total Cases**, **Total Deaths**, **Total Recovered**. ordering param is ``ordering``. So, an example could be this url : ``http://127.0.0.1:8000/api/ordering=total_deaths`` for Asc and simply add a ``-`` before param for Desc ordering.

# Contributions 
All welcomed 🙏🏻
