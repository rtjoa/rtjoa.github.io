window.onload = function() {
    const s = "sukpbAdt/xbtijohupo/fev";
    const email = String.fromCharCode(...s.split('').map(c => c.charCodeAt(0) - 1));
    document.getElementById("email").innerHTML = email;
    document.getElementById("email").href = `mailto:${email}`;
}
