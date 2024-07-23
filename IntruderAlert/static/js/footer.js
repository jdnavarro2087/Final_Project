const quotes = [
    {
        text: 'We cannot solve problems with the kind of thinking we employed when we came up with them.',
        author: '—Albert Einstein',
      },
      {
        text: 'The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.',
        author: '—Winston Churchill',
      },
      {
        text: 'Perfection is not attainable. But if we chase perfection we can catch excellence.',
        author: '—Vince Lombardi',
      },
      {
        text: 'Success is not final; failure is not fatal: It is the courage to continue that counts.',
        author: '—Winston Churchill',
      },

];

let currentQuote = 0;

function changeFooter() {
    currentQuote = currentQuote + 1;
    if(currentQuote >= quotes.length) {
        currentQuote = 0; // go back to first
    }

    let quote = quotes[currentQuote];
    document.getElementById("footer-quote").innerText = quote.text;
    document.getElementById("footer-quote-author").innerText = quote.author;
}


function start_footer() {
    console.log("footer logic started");

    changeFooter();

    // timer
    setInterval(changeFooter, 4000);
}