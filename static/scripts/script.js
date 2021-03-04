function toggleTag() {
  let to_add = document.getElementById('tagsList')
  let selectBox = document.getElementById('selectBox')

  to_add.innerHTML += ' ' + selectBox.options[selectBox.selectedIndex].text
}

function clearTags() {
  let tags = document.getElementById('tagsList')
  tags.innerHTML = 'Tags:';
}
