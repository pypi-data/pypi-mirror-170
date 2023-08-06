const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const stringCompare=(a,b)=>{if(a<b){return -1;}if(a>b){return 1;}return 0;};const caseInsensitiveStringCompare=(a,b)=>stringCompare(a.toLowerCase(),b.toLowerCase());

export { caseInsensitiveStringCompare as c, stringCompare as s };
