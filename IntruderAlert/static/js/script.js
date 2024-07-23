// Wait until entire DOM content is loaded until executing the script
document.addEventListener('DOMContentLoaded', function(){
    // Select the upload PCAP file link by its ID.
    var uploadlink = document.getElementById("upload-files")
    // Add a click event listener to the upload PCAP files link
    uploadlink.addEventListener('click', function(e){
        // Prevent the default action of the link. Nav to new page.
        // Select the content div by its id and add the hidden content class to it.
        // This class will hide the content div by using css.
        document.getElementById('content').classList.add('hidden-content');
    });
});


function init() {
    // start the footer logic
    start_footer();
}

window.onload = init;