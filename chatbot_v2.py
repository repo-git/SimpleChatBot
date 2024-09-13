from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Carica modello e tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []
history_limit = 5  # Limita la cronologia delle conversazioni per evitare input troppo lunghi

def truncate_history(history, limit):
    """Riduce la cronologia della conversazione al numero massimo di turni."""
    return history[-limit:]

def generate_response(input_text, history):
    """Genera una risposta in base all'input e alla cronologia della conversazione."""
    # Combina la cronologia in un'unica stringa
    history_string = "\n".join(history)
    
    # Tokenizza input e cronologia
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt", truncation=True)
    
    # Genera risposta dal modello
    outputs = model.generate(**inputs, max_length=100, num_return_sequences=1, temperature=0.7)
    
    # Decodifica la risposta generata
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    return response

def chat():
    """Avvia una conversazione con il modello."""
    print("Inizia la conversazione (digita 'exit' per uscire)")
    
    while True:
        try:
            # Input dell'utente
            input_text = input("> ").strip()
            
            # Verifica se l'utente vuole uscire
            if input_text.lower() in ['exit', 'quit']:
                print("Fine della conversazione.")
                break

            # Genera risposta dal modello
            response = generate_response(input_text, conversation_history)

            # Visualizza la risposta
            print(response)

            # Aggiorna la cronologia della conversazione
            conversation_history.append(input_text)
            conversation_history.append(response)
            
            # Troncamento della cronologia per evitare sequenze troppo lunghe
            conversation_history = truncate_history(conversation_history, history_limit)

        except Exception as e:
            print(f"Si è verificato un errore: {e}")

# Avvia la chat
if __name__ == "__main__":
    chat()
