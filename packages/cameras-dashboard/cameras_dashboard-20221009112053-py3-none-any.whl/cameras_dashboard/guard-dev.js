const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { e as e$1, i as i$1, O as b } from './main-dev.js';

/**
 * @license
 * Copyright 2018 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */const e={},i=e$1(class extends i$1{constructor(){super(...arguments),this.nt=e;}render(r,t){return t();}update(t,[s,e]){if(Array.isArray(s)){if(Array.isArray(this.nt)&&this.nt.length===s.length&&s.every((r,t)=>r===this.nt[t]))return b;}else if(this.nt===s)return b;return this.nt=Array.isArray(s)?Array.from(s):s,this.render(s,e);}});

export { i };
