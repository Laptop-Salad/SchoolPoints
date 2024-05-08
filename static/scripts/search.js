const searchResults = document.getElementById("searchResults");
const searchInput = document.getElementById("searchStudents");

searchInput.addEventListener("input", () => {
    let currTerm = searchInput.value;

    if (currTerm) {
        searchResults.style.display = "block";
        getSearchRes();
    } else {
        searchResults.style.display = "none";
    }
});

function getSearchRes() {
    let currTerm = searchInput.value;

    let xmlhttp = new XMLHttpRequest();

    // When xmlhttp client is ready, send request
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Clear previous search results
            searchResults.innerHTML = "";

            var data = JSON.parse(this.responseText);
            var student_ids = data.student_ids;
            var student_names = data.student_names;

            if (student_names && student_names.length > 0) {
                for (var i = 0; i < student_names.length; i++) {
                    var student_name = student_names[i];
                    var student_id = student_ids[i];

                    searchResults.innerHTML += `
                    <div class="findS">
                        <div class="student-info-box">
                        <p> ${student_name} </p>
                        <a href='/student/${student_id}'>Select</a>
                        </div>
                    </div>
                    `;
                }
            }
        }
    };

    xmlhttp.open("GET", `/searchstudents/` + currTerm, true);
    xmlhttp.send();
}

