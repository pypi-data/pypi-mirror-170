const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, r, n } from './main-dev.js';
import { C as CheckboxBase, s as styles } from './mwc-checkbox.css-dev.js';

_decorate([n("ha-checkbox")],function(_initialize,_CheckboxBase){class HaCheckbox extends _CheckboxBase{constructor(...args){super(...args);_initialize(this);}}return {F:HaCheckbox,d:[{kind:"field",static:true,key:"styles",value(){return [styles,r`
      :host {
        --mdc-radio-unchecked-color: var(--primary-text-color);
        --mdc-theme-secondary: var(--primary-color);
      }
    `];}}]};},CheckboxBase);
