console.log("Extension loaded.");

// Set a flag to indicate whether we're waiting for replies to load
let loadingReplies = false;

let intervalId = window.setInterval(function() {
  // If we're waiting for replies to load, don't scroll or click
  if (loadingReplies) {
    return;
  }

  console.log("Scrolling...");

  let commentsSection = document.querySelector('#comments');
  
  if (commentsSection) {
    console.log("Comments section found. Current scrollTop:", commentsSection.scrollTop, "scrollHeight:", commentsSection.scrollHeight);
    let lastChild = commentsSection.lastElementChild;
    if (lastChild) {
      console.log("Scrolling into view of the last child of the comments section...");
      lastChild.scrollIntoView(false);
      
      // Find all "show replies" buttons
      let showRepliesButtons = commentsSection.querySelectorAll('ytd-button-renderer#more-replies, ytd-continuation-item-renderer');
      console.log("Found", showRepliesButtons.length, '"show replies" buttons.');

      // Filter the buttons to include only those with more than 9 replies
      let buttonsWithMoreThan9Replies = Array.from(showRepliesButtons).filter(button => {
        let buttonText = button.innerText || "";
        let match = buttonText.match(/(\d+)/); // Extract the number from the text
        return match && parseInt(match[0]) > 9;
      });

      console.log("Found", buttonsWithMoreThan9Replies.length, '"show replies" buttons with more than 9 replies. Clicking...');
      buttonsWithMoreThan9Replies.forEach(button => button.click());

      // Wait for 5 seconds before scrolling or clicking again
      if (buttonsWithMoreThan9Replies.length > 0) {
        loadingReplies = true;
        setTimeout(() => {
          loadingReplies = false;
        }, 5000);
      }
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
    console.log("Stopped scrolling and clicking.");
  }
});
