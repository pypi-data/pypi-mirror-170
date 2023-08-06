const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { f as fireEvent } from './main-dev.js';

const showMediaBrowserDialog=(element,dialogParams)=>{fireEvent(element,"show-dialog",{dialogTag:"dialog-media-player-browse",dialogImport:()=>import('./dialog-media-player-browse-dev.js').then(function (n) { return n.d; }),dialogParams});};

export { showMediaBrowserDialog as s };
