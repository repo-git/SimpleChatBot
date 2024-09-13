# SimpleChatBot
In this project, I've worked on creating a simple chatbot using Facebook’s Blenderbot model and Hugging Face’s Python library, Transformers.

* Chatbot is a computer program that simulates written or spoken human conversation.
* With the integration of generative AI technology such as natural language processing, or NLP, chatbots can understand questions and respond based on the data they have collected.
* A special program called a ‘transformer’ acts as the brain of the chatbot.
* The transformer comprises a large language model, or LLM, that helps the chatbot understand the input question and generate the human-like response as the output.
* To build the chatbot, you must select an LLM based on the chatbot’s purpose. Other important parameters for choosing an LLM include licensing, model size, training data, and performance and accuracy.
* Transformers and LLMs work together within a chatbot to enable conversation.
* In a chatbot application, the back-end server will receive the prompts from the front-end interface and feed them to the chatbot, which will process the prompts.

## Versione 2
Miglioramenti:

* Gestione delle eccezioni:
  - Aggiunta di un blocco try-except per catturare eventuali errori senza terminare bruscamente il programma.

* Chiusura della conversazione:
  - Se l'utente digita "exit" o "quit", la conversazione si interrompe in modo ordinato.

* Limite della cronologia:
  - Viene limitato il numero di turni conservati nella cronologia a 5, per evitare che il contesto diventi troppo lungo e rallenti il modello.

*  Parametri del modello
  - Vengono introdotti i parametri max_length (limite massimo di lunghezza della risposta) e temperature (che controlla la casualità della risposta). Questo permette un controllo più fine su come il modello genera risposte.

*  Funzioni modularizzate:
  - Abbiamo separato la logica della generazione della risposta e della gestione della cronologia in funzioni distinte per migliorare la leggibilità e la manutenibilità.

* Interfaccia più amichevole:
  - Il programma ora fornisce istruzioni chiare per iniziare la conversazione e per uscire. Questo approccio rende il codice più facile da estendere e manutenere, migliorando allo stesso tempo l'usabilità e la stabilità.
