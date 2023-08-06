const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, l as a, d as e, j as _get, k as _getPrototypeOf, n } from './main-dev.js';
import { a4 as validateConditionalConfig, a5 as checkConditionsMet } from './ha-more-info-dialog-dev.js';

let HuiConditionalBase=_decorate([n("hui-conditional-base")],function(_initialize,_ReactiveElement){class HuiConditionalBase extends _ReactiveElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiConditionalBase,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"editMode",value:void 0},{kind:"field",decorators:[e()],key:"_config",value:void 0},{kind:"field",decorators:[e({type:Boolean,reflect:true})],key:"hidden",value(){return false;}},{kind:"field",key:"_element",value:void 0},{kind:"method",key:"createRenderRoot",value:function createRenderRoot(){return this;}},{kind:"method",key:"validateConfig",value:function validateConfig(config){if(!config.conditions){throw new Error("No conditions configured");}if(!Array.isArray(config.conditions)){throw new Error("Conditions need to be an array");}if(!validateConditionalConfig(config.conditions)){throw new Error("Conditions are invalid");}if(this.lastChild){this.removeChild(this.lastChild);}this._config=config;}},{kind:"method",key:"update",value:function update(changed){_get(_getPrototypeOf(HuiConditionalBase.prototype),"update",this).call(this,changed);if(!this._element||!this.hass||!this._config){return;}this._element.editMode=this.editMode;const visible=this.editMode||checkConditionsMet(this._config.conditions,this.hass);this.hidden=!visible;this.style.setProperty("display",visible?"":"none");if(visible){this._element.hass=this.hass;if(!this._element.parentElement){this.appendChild(this._element);}}}}]};},a);

export { HuiConditionalBase as H };
