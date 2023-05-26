function signUp() {
    var student_name = document.getElementById("student_name").value;
    var student_id = document.getElementById("student_id").value;
    var subject = document.getElementById("subject").value;
    var subject_marks = document.getElementById("subject_marks").value;

    console.log(student_name, student_id, subject, subject_marks);
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            accept: "application/json",
        },
        body: JSON.stringify({
            student_name: student_name,
            student_id: student_id,
            subject: subject,
            subject_marks: subject_marks,
        }),
    };
    const url = "http://localhost:3000/storeData/";
    fetch(url, options)
        .then((res) => res.json())
        .then((res) => {
            if (res.msg == 'add success') {
                alert("add info success")
            } else {
                alert("add info failed")
            }
        });
}