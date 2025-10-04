// Simple copy-to-clipboard function
function copyText(text) {
  if (!text) { alert('Nothing to copy'); return; }
  navigator.clipboard.writeText(text).then(() => {
    showToast('Copied: ' + text);
  }).catch((err) => alert('Copy failed: ' + err));
}

document.getElementById('translate-btn').addEventListener('click', () => {
  const word = document.getElementById('word-input').value.trim();
  if (!word) return alert('Enter a word');

  fetch(`/api/translate?q=${encodeURIComponent(word)}`)
    .then(res => res.json())
    .then(data => {
      const resultsSection = document.querySelector('.results') || document.createElement('section');
      resultsSection.className = 'results';
      resultsSection.innerHTML = `
        <div class="result-field"><strong>English:</strong> ${data.english}</div>
        <div class="result-field"><strong>Japanese:</strong> ${data.japanese}</div>
        <div class="result-field"><strong>Kana:</strong> ${data.kana}</div>
        <div class="result-field"><strong>Romaji:</strong> ${data.romaji}</div>
        <div class="result-field"><strong>Image:</strong><br><img src="${data.image}" width="200"></div>
      `;
      document.querySelector('.lookup').after(resultsSection);
    })
    .catch(err => alert('Error: ' + err));
});
