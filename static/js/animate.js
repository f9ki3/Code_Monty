// Function to animate the <p> tag
function animateP() {
    const pTag = document.getElementById('animatedP');
    let position = 0;

    // Move the <p> tag from left to right
    function move() {
      position += 2; // Adjust the speed by changing this value
      pTag.style.left = position + 'px';

      // Stop the animation when it reaches the right side of the screen
      if (position < window.innerWidth - pTag.clientWidth) {
        requestAnimationFrame(move);
      }
    }

    // Start the animation
    move();
  }

  // Call the animateP function when the page loads
  window.onload = animateP;