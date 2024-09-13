# Import delle librerie:
# Importa due oggetti: il tokenizer (che converte il testo in numeri per l'elaborazione) 
# e il modello di sequenza a sequenza (Seq2Seq), che genera risposte testuali.
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Definizione del nome del modello
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Inizializzazione della cronologia delle conversazioni
conversation_history = []

# Ciclo interattivo della conversazione
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Get the input data from the user
    input_text = input("> ")

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
