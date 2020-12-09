/* Delay visual feedback for invalid form items
 until initial submit or blur event */
Array.from(document.querySelectorAll('.Form input')).forEach(i => {
  i.addEventListener('invalid', () => {
    i.dataset.touched = true
  })
  i.addEventListener('blur', () => {
    if (i.value !== '') i.dataset.touched = true
  })
})

$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})