
let countdownInterval;
let currentLetter = '';

function startGame() {
    fetch('/start_game')
        .then(response => response.json())
        .then(data => {
            if (data.running) {
                currentLetter = data.letter;
                document.getElementById("letter").innerText = `${currentLetter}`;
                document.getElementById("status").style.display = "none"; // Hide status message
                showConfirmationButtons();
            } else {
                alert("Már megy a játék!");
            }
        });
}

function showConfirmationButtons() {
    document.getElementById("confirmation-buttons").style.display = "block";
    document.getElementById("start-button").disabled = true; // Disable start button
}

function startCountdown() {
    document.getElementById("progress").style.display = "block"; // Show progress bar
    document.getElementById("countdown").innerText = `120 mp maradt`;
    document.getElementById("countdown").style.textAlign = "center";
    document.getElementById("confirmation-buttons").style.display = "none"; // Hide confirmation buttons
    document.getElementById("status").style.display = "none"; // Hide status during countdown

    let timeLeft = 120;
    countdownInterval = setInterval(() => {
        timeLeft--;
        const percentComplete = (timeLeft / 120) * 100;
        document.getElementById("progress-bar").style.width = `${percentComplete}%`;
        document.getElementById("countdown").innerText = `${timeLeft} mp maradt`;
        document.getElementById("countdown").style.textAlign = "center";

        if (timeLeft <= 0) {
            clearInterval(countdownInterval);
            document.getElementById("progress").style.display = "none"; // Hide progress bar
            document.getElementById("countdown").style.display = "none"; // Hide countdown text
            document.getElementById("status").innerText = "Lejárt az idő. Kérhetsz új betűt!"; // Display time's up message
            document.getElementById("status").style.display = "block"; // Show the status message
            document.getElementById("status").style.textAlign = "center";
            document.getElementById("start-button").disabled = false; // Enable the start button
            document.getElementById("letter").style.display = "block"; // Show letter again
        }
    }, 1000);
}

function confirmLetter(isOkay) {
    if (isOkay) {
        startCountdown(); // Start the countdown if the user confirms
        document.getElementById("letter").style.display = "block"; // Show the letter during the game
    } else {
        // Fetch a new letter without starting the countdown
        fetch('/start_game')
            .then(response => response.json())
            .then(data => {
                currentLetter = data.letter;
                document.getElementById("letter").innerText = `${currentLetter}`;
                document.getElementById("status").innerText = "Jó lesz?";
            });
    }
}