console.log("JS is running")
const sendButton = document.getElementById('sendButton');
const r1 = document.getElementById('r1');
const r2 = document.getElementById('r2');
const ques = document.getElementById('ques');
const qBox = document.getElementById('q-box');
const ans = document.getElementById('ans');
const aBox = document.getElementById('a-box');

sendButton.addEventListener("click", async () => {
    const question = document.getElementById('question').value;
    document.getElementById('question').value = "";
    r2.style.display = "block";
    r1.style.display = "none";
    ques.innerHTML = question;

    // Call the postData function here, inside the click event listener
    let result = await postData("/api", { "question": `Answer of ${question} : ` });
    ans.innerHTML = result.result
});

// Define the postData function here
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    return response.json();
}
