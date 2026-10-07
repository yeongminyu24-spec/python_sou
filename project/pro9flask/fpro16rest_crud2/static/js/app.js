const btnJikwon = document.querySelector("#btnJikwon");
const btnOne = document.querySelector("#btnOne");
const btnBuser = document.querySelector("#btnBuser");
const btnBuserPart = document.querySelector("#btnBuserPart");

const jikwonno = document.querySelector("#jikwonno");
const buserno = document.querySelector("#buserno");

const msg = document.querySelector("#msg");
const tbody = document.querySelector("#tbody");
const thead = document.querySelector("#thead");

function setMsg(text){
    msg.textContent = text;
}

function clearTable(){
    thead.innerHTML = "";
    tbody.innerHTML = "";
}

function makeTable(rows){
    clearTable();

    if(!rows || rows.length === 0){
        setMsg("자료 없음");
        return;
    }

    let header = "<tr>";
    Object.keys(rows[0]).forEach(key => {
        header += "<th>" + key + "</th>"
    })
    header += "</tr>"
    thead.innerHTML = header;

    rows.forEach(r => { 
        let tr = "<tr>";
        Object.values(r).forEach(v => {
            tr += "<td>" + v + "</td>"
        })
        tr += "</tr>"
        tbody.innerHTML += tr;
    })
}


// 전체 직원
async function loadJikwon(){
    const res = await fetch("/acorn/jikwon");
    const mydata = await res.json();
    makeTable(mydata.data);

    setMsg("전체 직원 조회 완료")
}


// 직원 1명
async function loadOne(){
    const no = jikwonno.value;
    // const res = await fetch("/acorn/jikwon/" + no);
    const res = await fetch("/acorn/jikwon/"+no, {
        method : "GET"
    });
    const mydataOne = await res.json();
    makeTable([mydataOne.data]);

    setMsg("직원 1명 조회 완료")
}

// 부서 전체
async function loadBuser(){
    const no = jikwonno.value;
    // const res = await fetch("/acorn/jikwon/" + no);
    const res = await fetch("/acorn/buser")

    const mydatabuser = await res.json();
    makeTable(mydatabuser.data);

    setMsg("부서 전체 조회 완료")
}

// 특정 부서 직원 조회
async function loadBuserOne(){

    const num = buserno.value;
    
    const res = await fetch("/acorn/buser/" + num);
    const mydataBuserOne = await res.json();
    makeTable(mydataBuserOne.data);

    setMsg("특정 부서 1명 조회 완료")
}

btnJikwon.onclick = loadJikwon;   // 괄호 치지말고 함수의 결과를 넘겨줘야 함
btnOne.onclick = loadOne;
btnBuser.onclick = loadBuser;
btnBuserPart.onclick = loadBuserOne;