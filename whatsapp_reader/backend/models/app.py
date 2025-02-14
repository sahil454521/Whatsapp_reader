def process_command(command):
    text = speech_to_text_model.predict(command)

    intent = intent_classification_model.predict(text)

    if intent == 'read_meassages':
        messages = fetch_whatsapp_messages()
        relevant_messages = message_processing_model.predict(messages)
        return relevent_messages
    else:
        return "Sorry, I don't understand that command"