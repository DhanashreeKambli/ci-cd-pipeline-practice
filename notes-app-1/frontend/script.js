const API_URL = "http://YOUR_BACKEND_EXTERNAL_IP/notes";

async function fetchNotes() {
    const response = await fetch(API_URL);
    const notes = await response.json();

    const notesList = document.getElementById("notesList");
    notesList.innerHTML = "";

    notes.forEach(note => {
        const li = document.createElement("li");
        li.textContent = note;
        notesList.appendChild(li);
    });
}

async function addNote() {
    const noteInput = document.getElementById("noteInput");

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            note: noteInput.value
        })
    });

    noteInput.value = "";
    fetchNotes();
}

fetchNotes();