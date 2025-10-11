window.onload = function() {
    const s = "szboAsukpb/dpn";
    const email = String.fromCharCode(...s.split('').map(c => c.charCodeAt(0) - 1));
    document.getElementById("email").innerHTML = email;
    document.getElementById("email").href = `mailto:${email}`;
}
