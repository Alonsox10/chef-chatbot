// script.js - Lógica del chat y conexión API

const messages = document.getElementById('messages');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const botTyping = document.getElementById('botTyping');

function addMessage(text, sender) {
    const bubble = document.createElement('div');
    bubble.className = `bubble ${sender}`;
    // Reemplazar saltos de línea por <br> solo para mensajes del bot
    if (sender === 'bot') {
        // Eliminar * y # y reemplazar saltos de línea
        const cleanText = text.replace(/[\*#]/g, '').replace(/\n/g, '<br>');
        bubble.innerHTML = cleanText;
    } else {
        bubble.textContent = text;
    }
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const prompt = userInput.value.trim();
    if (!prompt) return;
    addMessage(prompt, 'user');
    userInput.value = '';
    botTyping.style.display = 'block';

    try {
        const response = await fetch('http://localhost:8000/bot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });
        if (!response.ok) throw new Error('Error en el servidor');
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (err) {
        addMessage('Hubo un problema de conexión.', 'bot');
    } finally {
        botTyping.style.display = 'none';
    }
});

// Auto-crecimiento del textarea
userInput.addEventListener('input', () => {
    userInput.style.height = 'auto';
    userInput.style.height = userInput.scrollHeight + 'px';
});
