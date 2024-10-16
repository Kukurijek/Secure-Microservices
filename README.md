# 12-Factor App - #2 Dependencies & 4# Backing Service Erklärung

Von Filipović Nemanja, Christoph Hiess, Resch Maximilian

### 12-Factor kurz erklärt

Um skalierbare Anwendungen zu entwickeln, die sich flexibel und kontinuierlich bereitstellen lassen, kann die 12-Factor-Methode angewendet werden.

Die 12 Faktoren und deren Beschreibungen zeigen bewährte Methoden zur Erstellung von plattformunabhängigen und wartbaren SaaS Anwendungen.

Die Programmiersprache, verwendete Frameworks und Services - wie z.B. Datenbanken - haben dabei keinen Einfluss auf die Verwendung dieser Methode.

### #2 Dependencies erklärt

Damit eine Anwendung plattformunabhängig betrieben werden kann, muss zu jedem Zeitpunkt der Ausführung sichergestellt werden, dass alle benötigten Softwarepakete/Libaries in der richtigen Version vorhanden sind. Dazu gibt es für diverse Programmiersprachen in der Entwicklungsphase einen "Dependency-Manager", der sich um die Einbindung der definierten Pakte in dem Projekt kümmert.

Die Verwaltung von Abhängigkeiten besteht aus zwei Teilen, die beide erfüllt sein müssen, um diesen Faktor zur gänze zu erfüllen:

- Deklaration von Abhänigkeiten

- Isolation von Abhängigkeiten

###### Deklaration von Abhänigkeiten

Je nach Programmiersprache wird eine Abhängigkeitsdeklaration in einer Datei erstellt, die diese durch Ausführung eines Befehls interpretiert und alle Paket auf dem Entwicklersystem zur Verfügung stellt. In der Produktion werden diese Pakete dann mit der Anwendung ausgeliefert.

###### Isolation von Abhängigkeiten

Während der Laufzeit wird sichergestellt, dass implizite Abhängigkeiten nicht auf anderen Wegen eines Subsystems benutzt werden. Dabei ist es notwendig, die Version eines Paketes explizit zu definieren.

### #4 Backing Service erklärt

Bei Backing Services handelt es sich um Dienste, die an eine Anwendung angehängt sind und diese konsumiert. Der Vorteil dieser Verbindungsart besteht in der Möglichkeit, Dienste einfach auszutauschen, ohne Codeänderungen in der Anwendung durchzuführen.

Als Beispiel: Eine Anwendung verwendet einen externen Zahlungsdienstleister, Firma A, zum verarbeiten der Zahlungen. Dieser Anbieter erhöhte die Preise, und die Administratoren finden einen anderen Anbieter, Firma B. Durch die Sicht des Payment Gateways als "angehängte Ressourcen", müssen nur die Konfirgurationsparamter in Richtung des neuen Anbieters (Firma B) geändert werden. Es sind keine weiteren Codeänderungen an der Anwendung nötig. Hierbei ist auch unerheblich, ob die Änderung von intern (eigene Payment Software) oder extern (SaaS Payment Anbieter) durchgeführt wird.

Weitere Beispiele von angehängten Diensten sind:

- Datenbanken

- Payment Gateways

- Storage

- CRM (Kundenmanagement System)

### Quellen

[The Twelve-Factor App | FORTIX GmbH](https://fortix.io/blog/die-12-faktoren-app)[The Twelve-Factor App | FORTIX GmbH](https://fortix.io/blog/die-12-faktoren-app)

https://12factor.net

[Twelve-Factor App: 12 Prinzipien zur Entwicklung von Webanwendungen](https://www.hosteurope.de/blog/die-twelve-factor-app-12-prinzipien-fuer-die-einfache-und-komfortable-entwicklung-von-webanwendungen/)

Developing, deploying, and operating twelve-factor applications with TOSCA [Developing, deploying, and operating twelve-factor applications with TOSCA | Proceedings of the 19th International Conference on Information Integration and Web-based Applications & Services](https://dl.acm.org/doi/abs/10.1145/3151759.3151830)
