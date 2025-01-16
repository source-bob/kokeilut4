const div = document.querySelector('#target');
div.className = 'm-list';

const html = `
<li>First element</li>
<li>Second element</li>
<li>Third element</li>`;

div.innerHTML = html;