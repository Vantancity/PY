all_notes = {}

for i in range(3):
    title = input("title: ")
    text = input("text: ")
    
    all_notes[title] = text
    print(all_notes)
    
watch_note = input("Peak a notes ")
if watch_note in all_notes:
    print(all_notes[watch_note])
else: 
    print("Note don't finded")