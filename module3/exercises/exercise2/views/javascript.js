document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    if (!username || !password) {
        errorMessage.textContent = "Please fill in all fields.";
        return;
    }

    if (username === 'username' && password === 'password') {
        window.location.href = 'dashboard.html';
    } else {
        errorMessage.textContent = "Provided credentials are not correct.";
    }
});