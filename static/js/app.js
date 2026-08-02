let syncing = false;

async function loadGraph(){

    const response = await fetch("/api/history");

    const history = await response.json();

    if(history.length===0){

        return;

    }

    const prices = history.map(item=>item.price);

    const min = Math.min(...prices);

    const max = Math.max(...prices);

    const width = 860;

    const height = 180;

    const step = width/(prices.length-1 || 1);

    let points="";

    prices.forEach((price,index)=>{

        const x=index*step;

        const y=height-((price-min)/(max-min || 1))*height;

        points+=`${x},${y} `;

    });

    document
        .getElementById("graphLine")
        .setAttribute("points",points);

}

async function syncAtlas(){

    if(syncing)return;

    syncing=true;

    const button=document.getElementById("sync-btn");

    const terminal=document.getElementById("sync-status");

    button.disabled=true;

    button.innerHTML="SYNCING...";

    terminal.innerHTML="";

    log("Connecting to Amazon...");

    const response=await fetch("/api/sync",{

        method:"POST"

    });

    if(response.ok){

        log("Collecting latest price...");

        await wait(500);

        log("Updating database...");

        await wait(500);

        log("Refreshing recommendation...");

        await wait(500);

        log("Done.");

        await loadGraph();

        setTimeout(()=>{

            location.reload();

        },1200);

    }

}

function log(text){

    const terminal=document.getElementById("sync-status");

    const time=new Date().toLocaleTimeString();

    terminal.innerHTML+=`<div>[${time}] ${text}</div>`;

}

function wait(ms){

    return new Promise(resolve=>setTimeout(resolve,ms));

}

loadGraph();