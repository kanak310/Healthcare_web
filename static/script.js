function sendMessage() {
  const userMessage = document.getElementById("userInput").value;

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: userMessage })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("chatBot").innerText = data.reply;
  });
}
