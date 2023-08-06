const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r } from './main-dev.js';
import { d as dynamicElement } from './dynamic-element-directive-dev.js';
import { c as computeStateDomain } from './auth-dev.js';
import { l as importMoreInfoControl, m as domainMoreInfoType } from './ha-more-info-dialog-dev.js';
import './stop_propagation-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

let MoreInfoGroup=_decorate(null,function(_initialize,_LitElement){class MoreInfoGroup extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoGroup,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e()],key:"stateObj",value:void 0},{kind:"field",decorators:[t()],key:"_groupDomainStateObj",value:void 0},{kind:"field",decorators:[t()],key:"_moreInfoType",value:void 0},{kind:"method",key:"updated",value:function updated(changedProperties){if(!this.hass||!this.stateObj||!changedProperties.has("hass")&&!changedProperties.has("stateObj")){return;}const states=this.stateObj.attributes.entity_id.map(entity_id=>this.hass.states[entity_id]).filter(entityState=>entityState);if(!states.length){this._groupDomainStateObj=undefined;this._moreInfoType=undefined;return;}const baseStateObj=states.find(s=>s.state==="on")||states[0];const groupDomain=computeStateDomain(baseStateObj);// Groups need to be filtered out or we'll show content of
// first child above the children of the current group
if(groupDomain!=="group"&&states.every(entityState=>groupDomain===computeStateDomain(entityState))){this._groupDomainStateObj={...baseStateObj,entity_id:this.stateObj.entity_id,attributes:{...baseStateObj.attributes}};const type=domainMoreInfoType(groupDomain);importMoreInfoControl(type);this._moreInfoType=type==="hidden"?undefined:`more-info-${type}`;}else {this._groupDomainStateObj=undefined;this._moreInfoType=undefined;}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`${this._moreInfoType?dynamicElement(this._moreInfoType,{hass:this.hass,stateObj:this._groupDomainStateObj}):""}
    ${this.stateObj.attributes.entity_id.map(entity_id=>{const entityState=this.hass.states[entity_id];if(!entityState){return "";}return $`
        <state-card-content
          .stateObj=${entityState}
          .hass=${this.hass}
        ></state-card-content>
      `;})}`;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      state-card-content {
        display: block;
        margin-top: 8px;
      }
    `;}}]};},s);customElements.define("more-info-group",MoreInfoGroup);
