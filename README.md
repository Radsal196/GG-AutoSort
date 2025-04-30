📂 Filorganisatör – README
Detta program organiserar automatiskt filer i en valfri mapp baserat på deras filtyp. Det passar perfekt för att snabbt rensa upp till exempel din Nedladdningar-mapp.

🧑‍💻 Hur du använder programmet
1. Öppna Python-filen
Öppna inlamning.py i en kodredigerare som t.ex. Visual Studio Code, Thonny eller IDLE.

2. Ändra sökvägen till din egen mapp
Leta reda på raden i koden som ser ut så här (ungefär rad 6):

source_folder = r"C:\Users\Abdulrazzak Saleh\Downloads"

Byt ut sökvägen (C:\Users\...) till den mapp du vill organisera.

✅ Så här hittar du rätt sökväg:
Öppna Utforskaren (File Explorer).

Navigera till mappen du vill organisera.

Klicka i adressfältet längst upp (där det står t.ex. Den här datorn > Nedladdningar).

Högerklicka och välj Kopiera som sökväg.

Klistra in den i koden (kom ihåg att sätta ett r framför strängen eller använda \\ mellan mapparna):

Exempel:

source_folder = r"C:\Users\DittNamn\Documents\Kaosmapp"

eller

source_folder = "C:\\Users\\DittNamn\\Documents\\Kaosmapp"


3. Kör programmet
Öppna terminalen eller tryck på Run/Start i din editor. Programmet kommer då att:

Skanna mappen

Skapa undermappar som "Bilder", "Dokument", "Zipfiler" osv.

Flytta filerna till rätt plats

📌 Obs!
Inga filer raderas – de flyttas bara till nya mappar.

Programmet körs bara en gång – du kan köra det igen när du vill städa på nytt.

Vill du att jag genererar en färdig README-fil till dig att ladda ner?
