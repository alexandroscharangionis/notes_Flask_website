// Get note id and send request to '/delete-note' endpoint, and then reload window to homepage:
function deleteNote(noteId) {
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId }),
  }).then(_res => {
    window.location.href = '/'
  })
}
