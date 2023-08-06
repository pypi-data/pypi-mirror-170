const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, n } from './main-dev.js';
import { H as HuiConditionalBase } from './hui-conditional-base-dev.js';
import { a3 as createRowElement } from './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './auth-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

_decorate([n("hui-conditional-row")],function(_initialize,_HuiConditionalBase){class HuiConditionalRow extends _HuiConditionalBase{constructor(...args){super(...args);_initialize(this);}}return {F:HuiConditionalRow,d:[{kind:"method",key:"setConfig",value:function setConfig(config){this.validateConfig(config);if(!config.row){throw new Error("No row configured");}this._element=createRowElement(config.state_color?{state_color:true,...config.row}:config.row);}}]};},HuiConditionalBase);
