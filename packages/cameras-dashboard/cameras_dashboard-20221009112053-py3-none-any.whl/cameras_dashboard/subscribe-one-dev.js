const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const subscribeOne=async(conn,subscribe)=>new Promise(resolve=>{const unsub=subscribe(conn,items=>{unsub();resolve(items);});});

export { subscribeOne as s };
