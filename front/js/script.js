document.addEventListener('DOMContentLoaded', function() {
    var audio = document.getElementById('audio');
    var playButton = document.getElementById('play');

    playButton.addEventListener('click', function() {
        if (audio.paused) {
            audio.play();
            playButton.textContent = 'Pause';
        } else {
            audio.pause();
            playButton.textContent = 'Play';
        }
    });

    // Add event listeners for 'prev' and 'next' buttons as needed
    // Update song information and cover art when changing tracks
});