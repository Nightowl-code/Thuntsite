console.log("js file")
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'I') {
        // Prevent the default behavior (opening developer tools)
        e.preventDefault();
    }
});

document.addEventListener('keydown', function (e) {
    if ((e.key === 'F12') ) {
        // Prevent the default behavior (opening developer tools)
        e.preventDefault();
    }
});