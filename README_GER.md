# 🎾 Tennis Turnier-API 🚀  
Dies ist die **inoffizielle API**, um relevante Turnierdaten von **Tennisturnieren in Deutschland** abzurufen.  

> [!WARNING]  
> Die API befindet sich in **aktiver Entwicklung** und kann fehlerhaft sein.  

## ⚙️ Funktionsweise  
🚀 Mithilfe der **`pyautogui`**-Bibliothek automatisiert das **`data_getter.py`**-Skript den Prozess Schritt für Schritt:  

🌐 **1. Browser starten:** Das Skript öffnet einen Webbrowser und navigiert zur Turnierplattform.  
🔍 **2. Turniere suchen:** Es sucht nach allen Turnieren einer bestimmten Altersklasse und scrollt durch die Einträge.  
📋 **3. Turnierdaten extrahieren:** Die Details jedes Turniers werden kopiert und in Variablen gespeichert.  
📂 **4. Daten zurückgeben:** Die extrahierten Informationen werden strukturiert und im **JSON-Format** zurückgegeben.  

## 📖 Verwendung  
1. Ein Verzeichnis öffnen.  
2. `python -m venv .` im Verzeichnis ausführen.  
3. Das Repository in das Verzeichnis klonen.  
4. `pip install -r src/requirements.txt` ausführen.  
5. Die Hauptdatei mit `python data_getter.py` starten.  

> [!CAUTION]  
> Beim Ausführen kann es vorkommen, dass die **Koordinaten der Elemente nicht mit deinem Bildschirm übereinstimmen**. Dadurch könnte `Enter` **zum falschen Zeitpunkt** gedrückt werden.  

## 💡 Motivation 💡  
🔍 Die aktuellen Turniersuchplattformen sind **ineffizient** und haben eine schlechte Benutzerfreundlichkeit.  
❌ Wichtige Features wie **Benachrichtigungen, erweiterte Filter** und eine bessere **Benutzeroberfläche** fehlen.  
💡 Das hat mich dazu inspiriert, meine **eigene Turnierplattform** mit besseren Funktionen zu entwickeln.  
🛠️ Dafür brauche ich zuverlässige Turnierdaten – **diese API bildet das Rückgrat für zukünftige Projekte**.  

## 🤝 Beitrag  
👨‍💻 **Beiträge sind willkommen!** Fühle dich frei, **Code beizutragen & die API zu verbessern**. 🚀  

🔹 **Wie kann ich beitragen?**  
1️⃣ **Einen Pull-Request senden**, und ich werde ihn prüfen.  
2️⃣ Wenn der Code gut ist, wird er **gemergt!** 🎉  

## 📌 Fortschrittsverfolgung  
📋 Den Entwicklungsfortschritt kannst du im **Notion Kanban Board** verfolgen:  
👉 [Notion Kanban Board](https://fearless-play-bd6.notion.site/18c17400d33a801983d3dc525004e33f?v=18c17400d33a808d863b000c23349fdb&pvs=4)
