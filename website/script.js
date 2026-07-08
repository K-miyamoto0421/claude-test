const button = document.getElementById("greet-btn");
const greetText = document.getElementById("greet-text");

const messages = [
  "こんにちは！訪問ありがとう😊",
  "今日もコーディングがんばろう！",
  "カレーライス食べたくなってきた…",
];

button.addEventListener("click", () => {
  const message = messages[Math.floor(Math.random() * messages.length)];
  greetText.textContent = message;
});
