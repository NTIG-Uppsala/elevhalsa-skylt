# Utvecklingsmiljö (Windows)
## Setup
1) Installera Python 3.8
2) Kör Test/setup_venv.bat
3) Installera webbläsare (Chrome/Chromium)
4) Verifiera att webbläsaren är uppdaterad
5) Ladda ner den senaste versionen av chromedriver: http://chromedriver.chromium.org/downloads
6) Extrahera filen från den nedladdade zip-filen till Test-mappen
7) Installera Python-tillägget till Visual Studio
8) Öppna `elevhalsa-digital-skylt.sln` i Visual Studio

## Skärmbildstest
Skärmbilder genereras i mappen `Test/screenshots` när man kör Test-projektet i Visual Studio.

### Ändra upplösningen för testet
Ändra `WIDTH` och `HEIGHT` i `Test/Test.py` till önskad bredd och höjd