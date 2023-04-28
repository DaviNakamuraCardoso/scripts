
const wills = [
    "https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2022/03/will-smith-oscar.jpg?w=876&h=484&crop=1",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/TechCrunch_Disrupt_2019_%2848834434641%29_%28cropped%29.jpg/323px-TechCrunch_Disrupt_2019_%2848834434641%29_%28cropped%29.jpg",
    "https://www.istoedinheiro.com.br/wp-content/uploads/sites/17/Reuters_Direct_Media/BrazilOnlineReportTopNews/tagreuters.com2022binary_LYNXNPEI2R0I6-BASEIMAGE-418x235.jpg",
    "https://br.web.img2.acsta.net/pictures/17/02/08/16/50/452749.jpg",
    "https://claudia.abril.com.br/wp-content/uploads/2020/01/will-smith-lanca-linha-de-roupas-inspirada-em-um-maluco-no-pedaco-1.jpg?quality=85&strip=info&w=680&h=453&crop=1",
    "https://sm.ign.com/t/ign_pt/news/i/i-am-legen/i-am-legend-sequel-starring-will-smith-and-michael-b-jordan_ugmg.1200.jpg",
];


function main() {

    setWikiTrashProperIcon();

}

function isBedtime() { 
    let today = new Date();
    return today.getHours() >= 20;
}

function setWikiTrashProperIcon() {
    if (!isWikiTrash()) return;

    let wikiLogo = document.querySelector('.mw-wiki-logo');
    let randomImage = wills[Math.floor(Math.random() * wills.length)]; 

    wikiLogo.className = ''; 
    wikiLogo.style.backgroundImage = `url("${randomImage}")`;

    document.title = 'Lies';
}


function isWikiTrash() { 
    return document.location.hostname.match('wikipedia.org') !== null;
}

main();
setInterval(main, 1000 * 2 * 60);
