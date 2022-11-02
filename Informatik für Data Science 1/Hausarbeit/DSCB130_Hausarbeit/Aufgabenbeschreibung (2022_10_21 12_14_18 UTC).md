# DSCB130 - Pong
Hausarbeit im WS 2022/23 - Bewertung mit max. 9 Punkten

| Gruppe | RZ-Kürzel | Name, Vorname |
|---|---|---|
|   |   |   |
|   |   |   |
|   |   |   |

## Hinweise
- Tragen Sie die fehlenden Daten in die Tabelle ein.
- Bearbeiten Sie Ihre Lösungen in diesem Dokument.
- Verwenden Sie folgende Dateinamen-Syntax entsprechend Ihrer Gruppe: **DSCB130_Hausarbeit_Gruppe**.
- Reichen Sie die Hausarbeit fristgerecht durch den Gruppenverantwortlichen per Upload in ILIAS ein.
- Verwenden Sie für den Upload das Dateiformat ZIP-Archiv.

## Story
Pong® ist ein Arcade-Sportvideospiel mit einfacher zweidimensionaler Grafik, das von [Atari](https://atari.com/pages/about) entwickelt und ursprünglich 1972 veröffentlicht wurde. Dies ist eines der ersten Arcade-Videospiele. Es wurde von Allan Alcorn als Trainingsübung für Atari-Mitbegründer Nolan Bushnell entwickelt, aber Bushnell und Atari-Mitbegründer Ted Dabney waren von der Qualität von Alcorns Arbeit überrascht und beschlossen, dieses Spiel zu entwickeln. Laut Bushnell basiert das Konzept dieses Spiels auf dem elektronischen Tischtennisspiel, das in [Magnavox Odyssey](https://www.heise.de/hintergrund/Magnavox-Odyssey-Erste-Spielkonsole-wird-50-Jahre-alt-7121128.html) (der ersten Heimkonsole) von [Ralph H. Baer](http://www.ralphbaer.com) enthalten ist. Daraufhin verklagte Magnavox Atari später wegen Patentverletzung.

Pong war das erste kommerziell erfolgreiche Videospiel und trug zusammen mit Magnavox Odyssey zum Aufbau der Videospielindustrie bei.

Kurz nach der Veröffentlichung begannen mehrere Unternehmen mit der Entwicklung von Spielen, die dem Gameplay eng folgten. Am Ende brachten die Konkurrenten von Atari neue Videospiele auf den Markt, die sich vom ursprünglichen Format von Pong unterschieden, was wiederum Atari dazu veranlasste, seine Mitarbeiter zu ermutigen, Pong zu übertreffen und selbst innovativere Spiele zu entwickeln.

Atari hat mehrere Pong-Fortsetzungen veröffentlicht, die auf dem ursprünglichen Gameplay aufbauen und neue Funktionen hinzufügen. Zu Weihnachten 1975 veröffentlichte Atari eine Heimversion von Pong, die nur über den Sears Store verkauft wurde. Auch die Home-Version ist kommerziell erfolgreich und hat zu unzähligen Nachahmungen geführt. Das Spiel wurde nach seiner Veröffentlichung für viele Heim- und tragbare Plattformen erneut veröffentlicht.

Ihre Version des Spiels Pong wird in etwa so aussehen:  

![DSCB130 - Pong](pong.png)

Die Darstellung der Highscore-Tabelle (Bestenliste) wird in etwa so aussehen:

![Pong-Highscore](pong-highscore.png)


## Aufgabenstellung
 1. Insgesamt sind 8 Methoden inhaltlich zu vervollständigen.
 2. Pro Methode gibt es einen Punkt.
 3. Ist das Spiel anschließend lauffähig und kann von jedem Gruppenmitglied am Präsentationstermin erklärt werden (Kolloquium), gibt es den finalen Punkt.

 Übersicht der Methoden und Variablen:

- [] `schwarz`
  - Eine Variable für den **RGB** Wert schwarz
- [] `weiss`
  - Eine Variable für den **RGB** Wert weiß
- [x] `generiereFarbe(): tuple`
  - Generiert einen zufällig erstellten validen RGB Wert
- [] `zeichneSpielfeld(): None`
  - Zeichnet die Basis des Spielfeldes
- [] `zeichneSchlaeger(schlaeger): None`
  - Zeichnet einen Schläger auf dem Spielfeld
- [] `zeichneBall(ball): None`
  - Zeichnet einen Ball
- [] `bewegeBall(ball, ballrichtungX, ballrichtungY): pygame.Rect`
  - Berechnet die folgenden Bewegungen des Balles nach einem Aufprall. Die neuen Koordinaten werden anschließend zurückgegeben.
- [] `computerGegner(ball, ballrichtungX, schlaeger2): pygame.Rect`
  - Simuliert die Bewegungen eines Gegners
- [] `leseHighscore(dateiName): []`
  - Liest eine Datei ein und gibt die besten n Spieler in einer Liste zurück.
- [] `schreibeHighscore(name, eintrag, dateiName): None`
  - Generiert einen Hash, speichert Hash / Name / Eintrag in einer Datei ab.
- [] `bekommeName(dateiName): string`
  - Generiert einen zufälligen Namen des Spielers und überprüft dessen Eindeutigkeit.
