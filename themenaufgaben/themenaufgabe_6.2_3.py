# Python kennt das Prinzip der Vertauschung zweier Werte in Variablen
# Musterbeispiel
example_list = [0, 1, 2, 3, 4]
print(example_list)

# Die Syntax ist: zu_tauschende_var_1, zu_tauschende_var_2 = zu_tauschende_var_2, zu_tauschende_var_1
# Hier wird also der  Inhalt vom Element 1 mit dem Inhalt von Element 5 der Liste vertauscht.
example_list[0], example_list[4] = example_list[4], example_list[0] 
print(example_list)

sentence_parts = ['!', 'Ich', 'die', 'Wörter', 'wirble']
# hier Lösungsvorschlag zu 3. schreiben:
#Es sollte so sein: [0, 1, 2, 3, 4] = [1, 4, 2, 3, 0]

sentence_parts[0], sentence_parts[1], sentence_parts[4] = sentence_parts[1], sentence_parts[4], sentence_parts[0]

print(sentence_parts)