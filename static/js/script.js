/*jshint esversion: 6 */

// Important Note & Copyright
function showImportantNote() {
    const importantNote = document.getElementById("important-note");
    importantNote.classList.toggle("hide");
}

document.getElementById("copyright").textContent = new Date().getFullYear();