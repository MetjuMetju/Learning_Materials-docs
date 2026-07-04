let nodes = 0;
let pods = 0;
let services = 0;

function updateDiagram() {
    const out = document.getElementById("diagram");

    let txt = "";

    txt += "Internet\n";
    txt += "   |\n";
    txt += "LoadBalancer\n";
    txt += "   |\n";
    txt += "Kubernetes API\n";
    txt += "   |\n";

    for (let i = 1; i <= nodes; i++) {
        txt += " +-- Node " + i + "\n";

        for (let p = 1; p <= pods; p++) {
            txt += " |     +-- Pod " + p + "\n";
        }

        for (let s = 1; s <= services; s++) {
            txt += " |     +-- Service " + s + "\n";
        }
    }

    out.textContent = txt;
}

function addNode() {
    nodes++;
    updateDiagram();
}

function addPod() {
    pods++;
    updateDiagram();
}

function addService() {
    services++;
    updateDiagram();
}

window.onload = updateDiagram;
