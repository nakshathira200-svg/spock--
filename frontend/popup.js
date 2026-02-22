const API = "http://127.0.0.1:8000";

let ws = new WebSocket("ws://127.0.0.1:8000/ws");

ws.onopen = () => {
  console.log("WebSocket connected");
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  document.getElementById("status").innerText = data.status;
};

document.getElementById("analyzeBtn").onclick = async () => {

  document.getElementById("status").innerText = "Starting analysis...";

  try {

    const res = await fetch(API + "/analyze");

    const data = await res.json();

    console.log(data);

  } catch (err) {

    document.getElementById("status").innerText = "Backend not reachable";

  }

};
