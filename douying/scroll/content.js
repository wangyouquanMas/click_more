console.log("Extension loaded.");

// Set a flag to indicate whether we're waiting for comments to load
let loadingComments = false;

let intervalId = window.setInterval(function() {
  // If we're waiting for comments to load, don't scroll
  if (loadingComments) {
    return;
  }

  console.log("Scrolling...");

  let commentsSection = document.querySelector('div.sX7gMtFl.comment-mainContent');

  if (commentsSection) {
    console.log("Comments section found. Current scrollTop:", commentsSection.scrollTop, "scrollHeight:", commentsSection.scrollHeight);
    let lastChild = commentsSection.lastElementChild;
    
    if (lastChild) {
      console.log("Scrolling into view of the last child of the comments section...");
      lastChild.scrollIntoView(false);

      // As there's no "show more" button and comments load automatically on scroll, 
      // just wait for a few seconds before the next scroll to give time for new comments to load
      loadingComments = true;
      setTimeout(() => {
        loadingComments = false;
      }, 1000);
    } else {
      console.log("No children found in the comments section.");
    }
  } else {
    console.log("Comments section not found.");
  }
}, 2000);

// Listen for the 'Esc' key press to stop the interval
window.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    clearInterval(intervalId);
    console.log("Stopped scrolling.");
  }
});
