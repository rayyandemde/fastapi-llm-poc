const promptInput = document.getElementById('prompt-input');
const generateBtn = document.getElementById('generate-btn');
const resultBox = document.getElementById('result-box');

generateBtn.addEventListener('click', async () => {
    const userPrompt = promptInput.value;

    if (!userPrompt) {
        alert('Please enter a prompt.');
        return;
    }

    resultBox.textContent = 'Generating... Please wait.';
    generateBtn.disabled = true;

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt: userPrompt,
            }),
        });

        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();

        resultBox.textContent = data.generated_text;
    } catch (error) {
        console.error('Error:', error);
        resultBox.textContent = `An error occurred: ${error.message}`;
    } finally {
        generateBtn.disabled = false;
    }
});
