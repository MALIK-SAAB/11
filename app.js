const questions = [
  {
    question: "Which city is called the Silicon Valley of India?",
    options: ["Bangalore", "Chennai", "Pune", "Hyderabad", "Kolkata"],
    answer: 0
  },
  {
    question: "Which city is known as the Pink City?",
    options: ["Jaipur", "Agra", "Lucknow", "Bhopal", "Surat"],
    answer: 0
  },
  {
    question: "Which city is famous for the Gateway of India?",
    options: ["Mumbai", "Delhi", "Goa", "Chennai", "Kolkata"],
    answer: 0
  },
  {
    question: "Which city is called the City of Joy?",
    options: ["Kolkata", "Bangalore", "Hyderabad", "Chennai", "Pune"],
    answer: 0
  },
  {
    question: "Which city is known as the Garden City of India?",
    options: ["Bangalore", "Chandigarh", "Mysore", "Delhi", "Ahmedabad"],
    answer: 0
  }
];

let currentQuestion = 0;
let answered = false;

const quizDiv = document.getElementById('quiz');
const nextBtn = document.getElementById('next-btn');

function showQuestion() {
  answered = false;
  nextBtn.style.display = 'none';
  const q = questions[currentQuestion];
  quizDiv.innerHTML = `
    <div class="question">${q.question}</div>
    <ul class="options">
      ${q.options.map((opt, i) => `<li><label><input type="radio" name="option" value="${i}"> ${opt}</label></li>`).join('')}
    </ul>
    <button id="submit-btn">Submit</button>
    <div id="result"></div>
  `;
  document.getElementById('submit-btn').onclick = submitAnswer;
}

function submitAnswer() {
  if (answered) return;
  const selected = document.querySelector('input[name="option"]:checked');
  const resultDiv = document.getElementById('result');
  if (!selected) {
    resultDiv.innerHTML = '<span class="incorrect">Please select an option.</span>';
    return;
  }
  answered = true;
  const selectedIndex = parseInt(selected.value);
  const correctIndex = questions[currentQuestion].answer;
  if (selectedIndex === correctIndex) {
    resultDiv.innerHTML = '<span class="correct">Correct!</span>';
  } else {
    resultDiv.innerHTML = `<span class="incorrect">Incorrect. Correct answer: <b>${questions[currentQuestion].options[correctIndex]}</b></span>`;
  }
  nextBtn.style.display = currentQuestion < questions.length - 1 ? 'inline-block' : 'none';
}

nextBtn.onclick = function() {
  if (currentQuestion < questions.length - 1) {
    currentQuestion++;
    showQuestion();
  }
};

showQuestion();
